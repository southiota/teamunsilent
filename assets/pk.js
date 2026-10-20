/* 프레스킷 영상: 화면에 들어올 때만 받아서 재생, 멈춤 버튼 (WCAG 2.2.2) */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const vio = new IntersectionObserver(es => es.forEach(e => {
    const v = e.target;
    if (e.isIntersecting && e.intersectionRatio >= .6) {
      if (!LITE && !v.src) v.src = v.dataset.src;
      if (!LITE && !v.dataset.user) { vids.forEach(o => { if (o !== v) o.pause(); }); v.play().catch(() => {}); }
    } else v.pause();
  }), { threshold: [0, .6] });
  const LITE = RM || navigator.connection?.saveData;
  const vids = [...document.querySelectorAll('video[data-src]')];
  vids.forEach(v => {
    vio.observe(v);
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'pp'; b.textContent = '재생';
    const name = v.getAttribute('aria-label') || '영상', label = t => { b.textContent = t; b.setAttribute('aria-label', `${name} ${t}`); };
    label('재생');
    b.addEventListener('click', () => { if (!v.src) v.src = v.dataset.src; if (v.paused) { delete v.dataset.user; vids.forEach(o => { if (o !== v) o.pause(); }); v.play(); } else { v.dataset.user = '1'; v.pause(); } });
    v.addEventListener('pause', () => label('재생')); v.addEventListener('play', () => label('일시정지'));
    v.after(b);
  });
})();
