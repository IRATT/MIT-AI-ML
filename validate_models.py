"""Independent checks of two educational LP results, not a Gurobi rerun."""
import ast,json,pathlib
from scipy.optimize import linprog
ROOT=pathlib.Path(__file__).parent
r=linprog([-15,-27,-40],A_ub=[[1,5,6],[2,3,7],[3,4,5]],b_ub=[115,280,670],bounds=(0,None),method='highs')
assert r.success and abs(-r.fun-1725)<1e-6
print('Product mix:',r.x.tolist(),'profit:',-r.fun)
nb=json.loads((ROOT/'evidence/Assignment_13_1.ipynb').read_text())
cell=next(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code' and 'supply = dict' in ''.join(c['source']))
values={}
for n in ast.parse(cell).body:
    if isinstance(n,ast.Assign):
        if isinstance(n.targets[0],ast.Name):values[n.targets[0].id]=ast.literal_eval(n.value.args[0])
        elif isinstance(n.targets[0],ast.Tuple):values['cost']=ast.literal_eval(n.value.args[0])
arcs=list(values['cost']); costs=[values['cost'][a] for a in arcs]
Aub=[];bub=[];Aeq=[];beq=[]
for center,limit in values['supply'].items():Aub.append([int(a==center) for a,b in arcs]);bub.append(limit)
for depot,limit in values['through'].items():
    Aub.append([int(b==depot) for a,b in arcs]);bub.append(limit)
    Aeq.append([int(b==depot)-int(a==depot) for a,b in arcs]);beq.append(0)
for landfill,demand in values['demand'].items():Aeq.append([int(b==landfill) for a,b in arcs]);beq.append(demand)
r=linprog(costs,A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs')
assert r.success and abs(r.fun-541000)<1e-6
print('Network flow objective:',r.fun,'variables:',len(arcs),'constraints:',len(Aub)+len(Aeq))
