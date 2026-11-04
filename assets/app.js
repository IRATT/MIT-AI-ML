(() => {
  const input = document.querySelector('#module-search');
  if (!input) return;
  const cards = [...document.querySelectorAll('.module-card')];
  const chips = [...document.querySelectorAll('.chip')];
  let category = 'All';
  const update = () => {
    const terms = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of cards) {
      const match = (category === 'All' || card.dataset.category === category) && terms.every(term => card.dataset.search.includes(term));
      card.hidden = !match;
      visible += Number(match);
    }
    document.querySelector('#module-count').textContent = `${visible} of 24 modules`;
    document.querySelector('#empty-state').hidden = visible !== 0;
  };
  input.addEventListener('input', update);
  for (const chip of chips) chip.addEventListener('click', () => {
    category = chip.dataset.filter;
    for (const item of chips) item.setAttribute('aria-pressed', String(item === chip));
    update();
  });
  document.querySelector('#clear-search').addEventListener('click', () => {
    input.value = ''; category = 'All';
    for (const item of chips) item.setAttribute('aria-pressed', String(item.dataset.filter === 'All'));
    update(); input.focus();
  });
})();
