/* 팀 언사일런트 — "들리는 것 같은" 파형 모션. 소리는 없다.
   <canvas data-wave="deck|eq|channels" data-bpm="124"></canvas>
   deck     : DJ 소프트웨어의 트랙 파형. 가운데 재생 헤드, 지나간 부분은 라임
   eq       : 비트에 맞춰 튀는 스펙트럼 바
   channels : 사일런트 디스코 헤드셋 3채널을 세 줄의 파형으로 */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const tok = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim() || '#C2EA8C';
  const rng = s => () => (s = (s * 16807) % 2147483647) / 2147483647;

  // 4/4 킥 + 페이즈(빌드/드롭)가 있는 가짜 트랙
  function track(n, seed) {
    const r = rng(seed), a = [];
    for (let i = 0; i < n; i++) {
      const step = i % 8, kick = Math.exp(-step / 1.6), snare = step === 4 ? .35 : 0;
      const phrase = .5 + .5 * Math.sin(i / 160) ** 2;
      a.push(Math.min(1, (.16 + .5 * kick + snare + .32 * r()) * (.45 + .55 * phrase)));
    }
    return a;
  }

  function setup(cv) {
    const kind = cv.dataset.wave, bpm = +cv.dataset.bpm || 124;
    const ctx = cv.getContext('2d');
    const data = track(6000, kind.length * 977 + 13);
    let W = 0, H = 0, dpr = 1, t0 = performance.now(), on = false, raf = 0;
    const eqBars = new Array(40).fill(0);

    function size() {
      dpr = Math.min(devicePixelRatio || 1, 2);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      draw(performance.now());
    }

    function draw(now) {
      const t = (now - t0) / 1000, beat = t * bpm / 60, ph = beat % 1;
      const lime = tok('--lime'), paper = tok('--paper'), mute = tok('--mute');
      ctx.clearRect(0, 0, W, H);

      if (kind === 'deck') {
        const step = 4, off = beat * 8 * step, mid = H / 2, head = W / 2;
        for (let x = 0; x < W; x += step) {
          const i = Math.floor((x + off) / step) % data.length;
          const h = Math.max(1, data[i] * (H * .46));
          ctx.fillStyle = x < head ? lime : mute;
          ctx.globalAlpha = x < head ? .85 : .45;
          ctx.fillRect(x, mid - h, step - 1.5, h * 2);
        }
        ctx.globalAlpha = 1; ctx.fillStyle = paper;
        ctx.fillRect(head - 1, 0, 2, H);
      }

      if (kind === 'eq') {
        const n = eqBars.length, gap = 4, bw = (W - gap * (n - 1)) / n;
        for (let k = 0; k < n; k++) {
          const low = 1 - k / n, kick = Math.exp(-ph * 5) * low;
          const wob = .5 + .5 * Math.sin(t * (2 + k * .37) + k);
          const target = Math.min(1, .12 + kick * .8 + wob * .35 * (1 - low * .5));
          eqBars[k] += (target - eqBars[k]) * (RM ? 1 : .25);
          const h = eqBars[k] * H;
          ctx.fillStyle = k % 9 === 0 ? lime : mute;
          ctx.globalAlpha = k % 9 === 0 ? .9 : .4;
          ctx.fillRect(k * (bw + gap), H - h, bw, h);
        }
        ctx.globalAlpha = 1;
      }

      if (kind === 'channels') {
        const cols = [lime, paper, mute], mid = H / 2;
        cols.forEach((c, ch) => {
          ctx.beginPath(); ctx.strokeStyle = c; ctx.globalAlpha = ch === 0 ? .9 : .45; ctx.lineWidth = ch === 0 ? 2 : 1.25;
          const amp = (H * .32) * (.35 + .65 * Math.exp(-((beat + ch / 3) % 1) * 3));
          for (let x = 0; x <= W; x += 3) {
            const u = x / W, env = Math.sin(Math.PI * u);
            const y = mid + (ch - 1) * H * .12 + Math.sin(u * (18 + ch * 7) - t * (3 + ch)) * Math.sin(u * 5 + t) * amp * env;
            x ? ctx.lineTo(x, y) : ctx.moveTo(x, y);
          }
          ctx.stroke();
        });
        ctx.globalAlpha = 1;
      }
    }

    function loop(now) { draw(now); if (on && !RM) raf = requestAnimationFrame(loop); }
    new ResizeObserver(size).observe(cv);
    new IntersectionObserver(([e]) => {
      on = e.isIntersecting; cancelAnimationFrame(raf);
      if (on && !RM) raf = requestAnimationFrame(loop);
    }).observe(cv);
    size();
  }

  document.querySelectorAll('canvas[data-wave]').forEach(setup);
})();
