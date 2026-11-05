(() => {
  const record = document.querySelector('#module-record');
  if (!record) return;
  const aliases = {'#work':'#projects', '#modules':'#course-record', '#results':'#course-record'};
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const revealTarget = ({expandRecord = false, focus = false} = {}) => {
    let hash = location.hash;
    if (aliases[hash]) {
      hash = aliases[hash];
      history.replaceState(null, '', hash);
    }
    if (!hash) return;
    let id;
    try { id = decodeURIComponent(hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (!target) return;
    if (expandRecord) record.open = true;
    if (id === 'evidence') document.querySelector('#evidence-notes').open = true;
    let parent = target.closest('details');
    while (parent) {
      parent.open = true;
      parent = parent.parentElement?.closest('details');
    }
    requestAnimationFrame(() => {
      target.scrollIntoView({behavior: reducedMotion.matches ? 'instant' : 'smooth', block: 'start'});
      if (focus) {
        const focusTarget = expandRecord ? record.querySelector('summary') : target;
        if (!focusTarget.matches('summary')) focusTarget.setAttribute('tabindex', '-1');
        focusTarget.focus({preventScroll:true});
      }
    });
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || link.classList.contains('skip') || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const hash = link.getAttribute('href');
    if (!hash || hash === '#') return;
    event.preventDefault();
    if (location.hash !== hash) history.pushState(null, '', hash);
    revealTarget({expandRecord:link.hasAttribute('data-expand-record'), focus:true});
  });
  window.addEventListener('hashchange', () => revealTarget());
  revealTarget();

  const progress = document.querySelector('.reading-progress');
  const nav = [...document.querySelectorAll('nav a[href^="#"]')];
  const sections = nav.map(link => document.querySelector(link.getAttribute('href')));
  let scheduled = false;
  const updateReadingState = () => {
    scheduled = false;
    const distance = document.documentElement.scrollHeight - innerHeight;
    progress.style.transform = `scaleX(${distance > 0 ? Math.min(1, Math.max(0, scrollY / distance)) : 0})`;
    const offset = document.querySelector('.nav').getBoundingClientRect().height + 70;
    let active = -1;
    sections.forEach((section, index) => { if (section && section.getBoundingClientRect().top <= offset) active = index; });
    if (distance > 0 && scrollY >= distance - 2) active = nav.length - 1;
    nav.forEach((link, index) => {
      if (index === active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };
  const scheduleUpdate = () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(updateReadingState); }
  };
  addEventListener('scroll', scheduleUpdate, {passive:true});
  addEventListener('resize', scheduleUpdate);
  document.addEventListener('toggle', scheduleUpdate, true);
  updateReadingState();
})();
