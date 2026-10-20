/* 시안 v5 공용 동작: 상단 바, 등장, 카운트업, 타임랩스(시계 연동), 섭외 문의 폼, 시안 바꾸기 */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const pad = n => String(n).padStart(2, '0');

  const bar = document.querySelector('.top');
  if (bar) { const f = () => bar.classList.toggle('solid', scrollY > 30); addEventListener('scroll', f, { passive: true }); f(); }

  function count(el) {
    const to = +el.dataset.count, suf = el.dataset.suffix || '';
    if (RM) return;
    const t0 = performance.now();
    (function f(now) {
      const p = Math.min((now - t0) / 1300, 1);
      el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))) + suf;
      if (p < 1) requestAnimationFrame(f);
    })(t0);
  }
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    e.target.querySelectorAll('[data-count]').forEach(count);
    io.unobserve(e.target);
  }), { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  // 타임랩스: 18:05:50부터 20초 간격 563컷을 20fps로 → 영상 1초 = 현장 400초. 화면에 들어올 때만 받는다.
  const reel = document.getElementById('reel');
  if (reel) {
    const clk = document.getElementById('clk'), pp = document.getElementById('reelpp');
    const T0 = 18 * 3600 + 5 * 60 + 50, base = reel.dataset.base || '../../vid/v5/';
    const small = matchMedia('(max-width: 760px)').matches;
    let userPaused = false, loaded = false;
    reel.poster = base + 'tl.jpg';
    const load = () => {
      if (loaded) return; loaded = true;
      if (small) reel.src = base + 'tl-sm.mp4';
      else reel.innerHTML = `<source src="${base}tl.av1.mp4" type='video/mp4; codecs="av01.0.08M.08"'><source src="${base}tl.mp4" type="video/mp4">`;
      reel.load();
    };
    const tick = () => {
      if (reel.duration && clk) { const m = Math.floor((T0 + reel.currentTime * 400) / 60); clk.textContent = pad(Math.floor(m / 60)) + ':' + pad(m % 60); }
      requestAnimationFrame(tick);
    };
    if (RM) { reel.controls = true; if (pp) pp.hidden = true; }
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting) { load(); if (!RM && !userPaused) reel.play().catch(() => {}); }
      else reel.pause();
    }, { threshold: .3 }).observe(reel);
    if (pp) {
      pp.addEventListener('click', () => { userPaused = !reel.paused; userPaused ? reel.pause() : reel.play(); });
      reel.addEventListener('pause', () => pp.textContent = '재생');
      reel.addEventListener('play', () => pp.textContent = '일시정지');
    }
    requestAnimationFrame(tick);
  }

  // 섭외 문의 (연락처 공개 전: 전송하지 않고 안내만)
  const f = document.getElementById('f'), sent = document.getElementById('sent');
  if (f) f.addEventListener('submit', e => {
    e.preventDefault();
    sent.hidden = false;
    sent.textContent = '섭외 문의 연락처를 준비하고 있습니다. 입력하신 내용은 아직 전송되지 않았습니다.';
  });

  // 시안 바꾸기 (미리보기 전용)
  const here = location.pathname.split('/').pop();
  const sw = document.createElement('nav');
  sw.setAttribute('aria-label', '시안 바꾸기');
  sw.style.cssText = 'position:fixed;left:50%;bottom:14px;transform:translateX(-50%);z-index:90;display:flex;gap:4px;padding:5px;border-radius:99px;background:rgba(17,28,28,.88);backdrop-filter:blur(8px);font:700 12px/1 "JetBrains Mono",monospace;box-shadow:0 10px 30px -10px rgba(0,0,0,.5)';
  sw.innerHTML = [['a.html', 'A 포스터'], ['b.html', 'B 시네마'], ['c.html', 'C 브리프']].map(([h, l]) =>
    `<a href="${h}" style="text-decoration:none;padding:8px 12px;border-radius:99px;${h === here ? 'background:#C2EA8C;color:#1A2828' : 'color:#F4F7EF'}"${h === here ? ' aria-current="page"' : ''}>${l}</a>`).join('');
  document.body.appendChild(sw);
})();
