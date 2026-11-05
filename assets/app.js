// Keep older homepage bookmarks useful after consolidating the portfolio.
(() => {
  const redirectOldBookmark = () => {
    const path = location.pathname;
    if (!path.endsWith('/') && !path.endsWith('/index.html')) return;
    const destinations = { '#modules': 'course.html', '#work': 'projects.html' };
    const target = destinations[location.hash];
    if (target) location.replace(target);
  };
  window.addEventListener('hashchange', redirectOldBookmark);
  redirectOldBookmark();
})();
