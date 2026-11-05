"""Build one continuous portfolio with an expandable course record."""
import html
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parent
MODULES = json.loads((ROOT / 'data/modules.json').read_text())
AWARDS = json.loads((ROOT / 'data/awards.json').read_text())
TAKEAWAYS = json.loads((ROOT / 'data/takeaways.json').read_text())
SITE = 'https://iratt.github.io/MIT-AI-ML/'
REPO = 'https://github.com/IRATT/MIT-AI-ML'

def e(value):
    return html.escape(str(value), quote=True)

def page(path, title, description, body, active):
    prefix = '' if path == 'index.html' else 'index.html'
    css_version = hashlib.sha256((ROOT / 'assets/style.css').read_bytes()).hexdigest()[:10]
    js_version = hashlib.sha256((ROOT / 'assets/app.js').read_bytes()).hexdigest()[:10]
    nav = ''.join(f'<a href="{prefix}{anchor}">{label}</a>' for anchor, label in [('#projects', 'Projects'), ('#recognition', 'Recognition'), ('#course-record', 'Course record')])
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} | Ian Alleyne</title><meta name="description" content="{e(description)}"><meta name="theme-color" content="#102e38"><meta property="og:title" content="{e(title)} | Ian Alleyne"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website"><link rel="canonical" href="{SITE}{path}"><link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="stylesheet" href="assets/style.css?v={css_version}"><script defer src="assets/app.js?v={js_version}"></script></head><body><a class="skip" href="#main">Skip to content</a><header class="nav"><div class="wrap nav-inner"><a class="brand" href="{prefix}#about"><span class="monogram" aria-hidden="true">IA</span><span>Ian Alleyne<small>Applied AI & advanced analytics</small></span></a><nav aria-label="Main navigation">{nav}<a class="github-link" href="https://github.com/IRATT/">GitHub ↗</a></nav></div><div class="reading-progress" aria-hidden="true"></div></header><main id="main">{body}</main><footer class="footer"><div class="wrap footer-inner"><p>© 2026 Ian Alleyne · Independent learner portfolio<br>MIT xPRO Professional Certificate in Advanced Analytics with AI, ML, and Data Science</p><a href="{prefix}#evidence">Evidence & authorship</a></div></footer></body></html>'''
    (ROOT / path).write_text(doc)

def award_card(a):
    title = 'Professional certificate' if a['id'] == 'completion-certificate' else a['type']
    description = 'Advanced Analytics with AI, ML, and Data Science · 36 CEUs' if a['id'] == 'completion-certificate' else a['title']
    return f'''<article class="award"><a class="award-image" href="assets/awards/{a['image']}" aria-label="View {e(title)} image"><img src="assets/awards/{a['image']}" alt="{e(a['image_alt'])}" loading="lazy" width="600" height="464"></a><div class="award-copy"><h3>{e(title)}</h3><p>{e(description)}</p><span class="award-date">{e(a['date_label'])}</span><a href="{e(a['url'])}" target="_blank" rel="noopener">Verify credential ↗</a></div></article>'''

def home():
    summaries = ['Understand patterns, variation and uncertainty.', 'Estimate outcomes and the cost of errors.', 'Choose actions within real constraints.', 'Evaluate nonlinear patterns and ensembles.', 'Work with images, language and learned representations.']
    themes = ''.join(f'<li><span class="theme-number">{i:02}</span><h3>{e(t["title"])}</h3><p>{e(summary)}</p></li>' for i, (t, summary) in enumerate(zip(TAKEAWAYS, summaries), 1))
    body = f'''<section class="hero wrap" id="about"><div><span class="eyebrow">Ian Alleyne, PhD, MBA</span><h1>Data in context.<br>Decisions with value.</h1><p class="lead">I connect engineering judgment, advanced analytics and responsible AI to business decisions in healthcare and critical infrastructure.</p><p class="credential"><strong>MIT xPRO Professional Certificate</strong><br>Advanced Analytics with AI, ML, and Data Science<br>6-month program</p><div class="actions"><a class="button" href="#projects">Explore selected projects <span aria-hidden="true">→</span></a><a class="text-link" href="#course-record" data-expand-record>Explore the course record →</a></div></div><aside class="achievement" aria-label="Course achievement"><span class="eyebrow">6 months · Completed 2026</span><div class="score">100<span>%</span></div><p class="score-label">Full marks in every module.</p><div class="score-details"><div><strong>24 / 24</strong><span>modules</span></div><div><strong>813 / 813</strong><span>points earned</span></div><div><strong>144</strong><span>graded activities</span></div></div><a href="#course-record" data-expand-record>Expand the final grade record →</a></aside></section><section class="section pale" id="takeaways"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">Program takeaways</span><h2>Five capabilities. One purpose.</h2></div><p>Use data in context to inform business decisions and create economic value.</p></div><ol class="themes">{themes}</ol><p class="principle"><strong>My approach:</strong> frame the decision, examine the evidence, validate the method and measure the result—with human accountability throughout.</p></div></section>'''
    return body

def recognition():
    return f'''<section class="section wrap" id="recognition"><div class="section-heading"><div><span class="eyebrow">Credentials & recognition</span><h2>Completion. Excellence.</h2></div><p>One professional certificate and two awards for exemplary assignment work.</p></div><div class="awards">{''.join(award_card(a) for a in AWARDS)}</div></section>'''


def projects():
    body = '''<section class="section projects-section" id="projects"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">Selected projects</span><h2>Learning applied to decisions.</h2></div><p>Four examples connect analytical methods to practical choices, constraints and evidence.</p></div><div class="projects-grid">
<article class="project" id="production-optimization"><span class="eyebrow">Course case · Modules 9–10</span><h3>Production optimization</h3><div class="project-metric">$2,316<span>modeled weekly contribution</span></div><p>Choose a production mix under labor and capacity constraints. Linear optimization translates margins and resource limits into a feasible schedule; sensitivity analysis identifies where extra capacity could create value.</p><p class="project-insight"><strong>Key insight:</strong> invest where a binding constraint limits the objective, and revisit the recommendation when conditions change.</p><a href="#module-10">Related coursework →</a></article>
<article class="project" id="network-logistics"><span class="eyebrow">Submitted notebook · Module 13</span><h3>Network logistics</h3><div class="project-metric">$541,000<span>minimum cost in the course model</span></div><p>Allocate flows through a supply and disposal network while respecting supply limits, depot capacities and landfill requirements. The Gurobipy model makes the feasible routes and cost trade-offs explicit.</p><p class="project-insight"><strong>Key insight:</strong> a recommendation must reconcile with the executed flow table and the constraints it satisfies.</p><a href="#module-13">Related coursework →</a></article>
<article class="project" id="clinical-ai"><span class="eyebrow">Course proposal + portfolio extension · Modules 23–24</span><h3>Clinical AI</h3><div class="project-metric words">Clinician-led<span>from conversation to structured records</span></div><p>Use speech recognition and NLP to draft structured clinical documentation in PAN Enterprise. Practitioners review, correct and approve the record; governed data can then support operational analytics.</p><p class="project-insight"><strong>Evaluation:</strong> compare documentation time, completeness and correction rates with a baseline before claiming benefit.</p><a href="#module-24">Related coursework →</a></article>
<article class="project" id="alarm-intelligence"><span class="eyebrow">Independent strategy extension · Modules 16, 22–24</span><h3>Alarm intelligence</h3><div class="project-metric words">Observe. Prove.<span>accountable AI for critical infrastructure</span></div><p>Apply contextual recommendations to alarm triage across power and data-center operations. A staged approach combines local resilience, clear operator authority and evaluation before any bounded automation.</p><p class="project-insight"><strong>Evaluation:</strong> test operational usefulness and failure modes while preserving human control over consequential actions.</p><a href="#module-22">Related coursework →</a></article>
</div><div class="supporting" id="downloads"><p class="scope-note">Financial figures are educational model results. Clinical AI and alarm intelligence describe proposals or portfolio extensions, with no measured deployment benefits claimed.</p><details><summary>Supporting course files · 4 model extracts + 1 notebook</summary><div class="download-list"><a href="evidence/production-model-extract.csv" download>Module 9 · Product-mix extract (CSV) ↓</a><a href="evidence/coal-procurement-extract.csv" download>Module 9 · Coal-procurement extract (CSV) ↓</a><a href="evidence/advertising-ppc-extract.csv" download>Module 12 · Price-per-click extract (CSV) ↓</a><a href="evidence/advertising-slate-extract.csv" download>Module 12 · Slate-allocation extract (CSV) ↓</a><a href="evidence/Assignment_13_1.ipynb" download>Module 13 · Network-flow notebook (IPYNB) ↓</a></div><p class="scope-note">These are separate course exercises. The Module 9 product-mix extract is not the source of the Module 10 $2,316 result. The notebook retains course starter code and static outputs; it has not been rerun in the original Gurobi environment.</p></details></div></div></section>'''
    return body

def course():
    short_titles = {2: 'Probability & uncertainty', 14: 'Classification & regression trees', 15: 'Ensemble learning', 16: 'Fairness & bias in predictions', 22: 'Interpretability & causality'}
    rows = ''
    for m in MODULES:
        n = m['number']
        recognition = f'<a class="module-award" href="#recognition">Exemplary assignment {n}.1 ↗</a>' if n in (16, 22) else ''
        rows += f'''<tr id="module-{n:02}" data-module="{n}"><th scope="row"><div class="module-topic"><span class="module-number">{n:02}</span><span>{e(short_titles.get(n, m['title']))}{recognition}</span></div></th><td class="module-insight">{e(m['headline'])}</td><td class="module-score"><strong>100%</strong><span>{m['earned']} / {m['possible']}</span></td></tr>'''
    body = f'''<section class="section wrap course-section" id="course-record"><details class="course-disclosure" id="module-record"><summary><span class="record-info"><span class="eyebrow">Course record</span><strong class="record-title">24 modules. 100% throughout.</strong><span class="record-meta">813 / 813 points · 144 graded activities</span></span><span class="record-toggle"><span class="when-closed">Expand record</span><span class="when-open">Collapse record</span><span class="record-plus" aria-hidden="true">+</span></span></summary><div class="record-body"><p class="scope-note">A complete summary of the module topics, key learning and final grades.</p><table class="course-table"><caption class="visually-hidden">All 24 modules, their key learning and final grade</caption><thead><tr><th scope="col">Module</th><th scope="col">Key learning</th><th scope="col">Final result</th></tr></thead><tbody>{rows}</tbody></table><p class="scope-note record-note">Final gradebook results, including accepted resubmissions, were reviewed on 4 November 2026. The certificate verifies completion; it does not display these grades.</p></div></details></section><section class="wrap supporting evidence-section" id="evidence"><details id="evidence-notes"><summary>Evidence, sources & authorship</summary><div class="evidence-copy"><p>This independent learner portfolio summarizes the course catalogue, module overviews, final gradebook and available submissions. The review covered 19 submitted files and five text responses, retained privately. Public downloads contain four reviewed numerical extracts and one screened notebook; Codio-only assignments are summarized in line with the program’s export guidance.</p><p>The five program takeaways and closing message are adapted from the supplied “Key Takeaways” slide and 1:17 “Program Wrap-Up.” Their application to business decisions is Ian’s portfolio synthesis. Award images and issue dates come from the linked official credential pages.</p><p>Course cases, templates and starter code retain their original attribution. AI assistance was used to organize, edit and build this portfolio. Proposed benefits are not measured deployment outcomes. Private learner identifiers, session links and patient records are excluded.</p><p><strong>Model review notes:</strong> the Module 13 notebook routes 80,000 units from Staten Island to C3; its written dashboard incorrectly labels C4. The portfolio follows the notebook. Module 9.2’s saved Solver report names B14 as the objective while profit is calculated in B8; an independent check reproduces its submitted mix (115, 0, 0) and profit of 1,725. Original workbooks remain private.</p><p><a href="{REPO}">View portfolio source and version history ↗</a></p></div></details></section>'''
    return body

def redirect(path, target):
    depth = len(Path(path).parts) - 1
    relative = '../' * depth + target
    destinations = {f'#module-{n:02}': f'index.html#module-{n:02}' for n in range(1, 25)} if path == 'course.html' else {}
    if path == 'course.html': destinations.update({'#results': 'index.html#course-record', '#evidence': 'index.html#evidence'})
    if path == 'projects.html': destinations.update({f'#{name}': f'index.html#{name}' for name in ['clinical-ai', 'alarm-intelligence', 'production-optimization', 'network-logistics', 'downloads']})
    redirect_script = f'location.replace(({json.dumps(destinations)})[location.hash] || {json.dumps(relative)});'
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Portfolio moved | Ian Alleyne</title><meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{target}"><meta http-equiv="refresh" content="0;url={e(relative)}"><script>{redirect_script}</script></head><body><h1>This content is now in the continuous portfolio.</h1><p><a href="{e(relative)}">Continue to the relevant section →</a></p></body></html>'''
    (ROOT / path).write_text(doc)

def legacy_redirects():
    targets = {'achievement.html': 'index.html#course-record', 'projects.html': 'index.html#projects', 'course.html': 'index.html#course-record', 'credentials.html': 'index.html#recognition', 'learning.html': 'index.html#takeaways', 'methodology.html': 'index.html#evidence', 'plan.html': 'index.html#evidence'}
    for m in MODULES:
        targets[f'modules/{m["number"]:02}.html'] = f'index.html#module-{m["number"]:02}'
    for name in ['clinical-ai', 'alarm-intelligence', 'production-optimization', 'network-logistics']:
        targets[f'cases/{name}.html'] = f'index.html#{name}'
    for path in (ROOT / 'evidence').glob('*.html'):
        targets[str(path.relative_to(ROOT))] = 'index.html#downloads'
    for path, target in targets.items():
        redirect(path, target)

if __name__ == '__main__':
    body = home() + projects() + recognition() + course()
    page('index.html', 'Applied AI & Advanced Analytics', 'Ian Alleyne: 100% across 24 MIT xPRO modules, applied projects, program takeaways and verified awards in one continuous portfolio.', body, 'overview')
    legacy_redirects()
    page('404.html', 'Page not found', 'Return to the portfolio.', '<section class="page-heading wrap"><span class="eyebrow">404</span><h1>Return to the portfolio.</h1><p class="lead">Explore the projects, recognition and expandable course record using the navigation above.</p></section>', 'overview')
    print('Built one continuous portfolio with a collapsed course record; legacy page links redirect to sections.')
