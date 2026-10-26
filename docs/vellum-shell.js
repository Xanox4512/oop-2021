/* Viewport scaling and accessible hold-to-exit. No server callback names are assumed. */
(() => {
  const fit = () => {
    const stage = document.querySelector('.t4k');
    if (!stage) return;
    stage.querySelectorAll('img[data-portrait]').forEach(image => {
      const source = image.dataset.portrait;
      if (source && !source.includes('{{') && image.getAttribute('src') !== source) image.setAttribute('src', source);
    });
    const scale = Math.min(innerWidth / 1920, innerHeight / 1080);
    stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
  };
  let holdTimer, activeButton;
  const cancel = () => {
    clearTimeout(holdTimer);
    activeButton?.classList.remove('holding');
    activeButton = null;
  };
  const start = (button) => {
    if (activeButton) return;
    activeButton = button;
    button.classList.add('holding');
    holdTimer = setTimeout(() => {
      window.dispatchEvent(new CustomEvent('vellum:action', { detail: { action: 'exit-request', slot: null, character: null } }));
      if (typeof window.GetParentResourceName !== 'function') {
        const feedback = document.querySelector('.action-feedback');
        if (feedback) feedback.textContent = 'Podgląd interfejsu · zdarzenie: exit-request';
      }
      cancel();
    }, 1500);
  };
  document.addEventListener('pointerdown', e => {
    const button = e.target.closest('.exit-control');
    if (button && e.button === 0) {
      button.setPointerCapture(e.pointerId);
      start(button);
    }
  });
  document.addEventListener('keydown', e => {
    if ((e.key === ' ' || e.key === 'Enter') && e.target.matches('.exit-control')) {
      e.preventDefault();
      if (!e.repeat) start(e.target);
    }
  });
  document.addEventListener('keyup', e => { if (e.key === ' ' || e.key === 'Enter') cancel(); });
  ['pointerup', 'pointercancel', 'lostpointercapture'].forEach(event => document.addEventListener(event, cancel));
  window.addEventListener('blur', cancel);
  document.addEventListener('visibilitychange', () => { if (document.hidden) cancel(); });
  addEventListener('resize', fit);
  new MutationObserver(fit).observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ['data-portrait'] });
  fit();
  // Warm all five sheets before the first turn; assets remain local to the resource.
  const warmPages = () => {
    for (let page = 1; page <= 5; page++) {
      const image = new Image();
      image.src = './assets/book-paper' + (page === 1 ? '' : '-' + page) + '.png';
    }
  };
  if (document.readyState === 'complete') warmPages();
  else window.addEventListener('load', warmPages, { once: true });
})();
