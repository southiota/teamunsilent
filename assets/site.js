/* 팀 언사일런트 v3 공용 동작: 상단 바, 등장, 카운트업, 사진 레일 */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;

  const nav = document.querySelector('.nav');
  if (nav) {
    const solid = () => nav.classList.toggle('solid', scrollY > 40 || nav.dataset.solid === '1');
    addEventListener('scroll', solid, { passive: true }); solid();
  }

  function count(el) {
    const to = +el.dataset.count, suf = el.dataset.suffix || '';
    if (RM) { el.textContent = to + suf; return; }
    const t0 = performance.now();
    (function f(now) {
      const p = Math.min((now - t0) / 1400, 1);
      el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))) + suf;
      if (p < 1) requestAnimationFrame(f);
    })(t0);
  }

  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    e.target.querySelectorAll('[data-count]').forEach(count);
    io.unobserve(e.target);
  }), { rootMargin: '0px 0px -12% 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  // 사진 레일: data-photos="이름:h|v,..." → img/live/이름.webp, 끊김 없이 돌도록 두 번 넣는다
  document.querySelectorAll('.track[data-photos]').forEach(t => {
    const items = t.dataset.photos.split(',').map(x => x.trim().split(':'));
    const figs = hide => items.map(([n, o], i) =>
      `<figure class="${o === 'v' ? 'v' : ''}"${hide ? ' aria-hidden="true"' : ''}><img src="${t.dataset.base || 'img/live/'}${n}.webp" alt=""${hide || i > 5 ? ' loading="lazy"' : ''} decoding="async"></figure>`).join('');
    t.innerHTML = figs(false) + figs(true);
  });

  if (RM) document.querySelectorAll('video[autoplay]').forEach(v => { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });
})();
