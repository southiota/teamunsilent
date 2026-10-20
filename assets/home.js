/* 팀 언사일런트 홈 (v6): 헤드셋 스위치, 그날 밤 타임랩스, 장소로 고르기, 구성 탭, 현장 영상, 섭외 문의 */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const small = matchMedia('(max-width: 760px)').matches;
  const pad = n => String(n).padStart(2, '0');
  const $ = id => document.getElementById(id);

  // 섭외 문의 받을 곳. 정해지면 여기만 채운다 (지금은 자리표시)
  const CONTACT_EMAIL = '';

  const bar = document.querySelector('.top');
  const solid = () => bar.classList.toggle('solid', scrollY > 30);
  addEventListener('scroll', solid, { passive: true }); solid();

  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { rootMargin: '0px 0px -10% 0px' });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  // 히어로: 잠깐 꺼진 채(흑백)로 보여 준 뒤 헤드셋이 켜진다. 스위치로 끄고 켤 수 있다.
  const hero = document.querySelector('.hero'), sw = $('sw');
  const set = on => { hero.classList.toggle('on', on); sw.setAttribute('aria-pressed', on); };
  let touched = false;
  sw.addEventListener('click', () => { touched = true; set(!hero.classList.contains('on')); });
  if (RM) set(true); else setTimeout(() => { if (!touched) set(true); }, 1800);

  // 그날 밤: 18:03:10부터 20초 간격 컷을 20fps로. 19:28~20:00(99컷)은 뺐다 → 영상 프레임 번호로 실제 시각을 계산한다.
  const reel = $('reel'), hh = $('hh'), mm = $('mm'), rb = $('reelbar'), pp = $('reelpp'), night = $('night');
  const rows = [...document.querySelectorAll('#tlist li')], T0 = 18 * 3600 + 3 * 60 + 10, GAP = 255, SKIP = 99;
  const at = t => { const i = Math.floor(t * 20); return T0 + (i < GAP ? i : i + SKIP) * 20; };
  const show = sec => {
    const m = Math.floor(sec / 60);
    hh.textContent = pad(Math.floor(m / 60)); mm.textContent = pad(m % 60);
    let cur = 0;
    rows.forEach((r, i) => { if (m >= +r.dataset.at) cur = i; });
    rows.forEach((r, i) => r.classList.toggle('cur', i === cur));
  };
  show(T0);
  let loaded = false, userPaused = false;
  const load = () => {
    if (loaded) return; loaded = true;
    reel.poster = 'vid/v6/tl.jpg';
    if (small) reel.src = 'vid/v6/tl-sm.mp4';
    else reel.innerHTML = '<source src="vid/v6/tl.av1.mp4" type=\'video/mp4; codecs="av01.0.08M.08"\'><source src="vid/v6/tl.mp4" type="video/mp4">';
    reel.load();
  };
  if (RM || navigator.connection?.saveData) {
    show(at(20)); pp.hidden = true; rb.style.width = '85%'; night.classList.add('paused');
  } else {
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting) { load(); if (!userPaused) reel.play().catch(() => {}); }
      else reel.pause();
    }, { threshold: .25 }).observe(reel.parentElement);
    const tick = () => {
      if (reel.duration && !reel.paused) { show(at(reel.currentTime)); rb.style.width = (reel.currentTime / reel.duration * 100) + '%'; }
      requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
    pp.addEventListener('click', () => { userPaused = !reel.paused; userPaused ? reel.pause() : reel.play(); });
    reel.addEventListener('pause', () => { pp.textContent = '재생'; night.classList.add('paused'); });
    reel.addEventListener('play', () => { pp.textContent = '일시정지'; night.classList.remove('paused'); });
  }

  // 장소로 고르기 → 맞는 볼륨 카드 강조
  const vols = $('vols'), picks = [...document.querySelectorAll('.pick [role=radio]')], cards = [...vols.querySelectorAll('.volc')];
  const choose = (b, scroll) => {
    picks.forEach(x => { x.setAttribute('aria-checked', x === b); x.tabIndex = x === b ? 0 : -1; });
    vols.classList.add('has');
    cards.forEach(c => { const on = c.dataset.v === b.dataset.v; c.classList.toggle('sel', on); c.querySelector('.fit').hidden = !on; });
    if (scroll && small) cards.find(c => c.dataset.v === b.dataset.v).scrollIntoView({ behavior: RM ? 'auto' : 'smooth', block: 'center' });
  };
  picks.forEach((b, i) => {
    b.tabIndex = i ? -1 : 0;
    b.addEventListener('click', () => choose(b, true));
    b.addEventListener('keydown', e => {
      const d = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
      if (!d) return;
      e.preventDefault(); const n = picks[(i + d + picks.length) % picks.length]; n.focus(); choose(n, false);
    });
  });
  document.querySelectorAll('.ask-b').forEach(b => b.addEventListener('click', () => {
    $('ftype').value = b.dataset.type;
    $('ask').scrollIntoView({ behavior: RM ? 'auto' : 'smooth', block: 'start' });
  }));

  // 구성 비교표: 모바일에서는 한 방식씩
  const cmp = $('cmp'), tb = [...document.querySelectorAll('.tabs button')];
  tb.forEach(b => b.addEventListener('click', () => { cmp.dataset.show = b.dataset.show; tb.forEach(x => x.setAttribute('aria-pressed', x === b)); }));

  // 현장 영상: 화면에 들어올 때만 받아서 재생, 멈춤 버튼 (WCAG 2.2.2)
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

  // 사진 레일 멈춤 (WCAG 2.2.2)
  const rail = document.querySelector('.rail'), rp = $('railpp');
  rp.addEventListener('click', () => { const s = rail.classList.toggle('stop'); rp.textContent = s ? '사진 흐르기' : '사진 멈춤'; });
  if (RM) rp.hidden = true;

  // 섭외 문의
  const f = $('f'), sent = $('sent');
  f.addEventListener('submit', e => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(f));
    if (!CONTACT_EMAIL) { sent.hidden = false; sent.textContent = '섭외 문의 연락처를 준비하고 있습니다. 입력하신 내용은 아직 전송되지 않았습니다.'; return; }
    const body = `행사 날짜: ${d.date}\n장소: ${d.place}\n예상 인원: ${d.people}\n관심 있는 방식: ${d.type}\n회신 연락처: ${d.reply}\n\n${d.memo}`;
    location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent('[섭외 문의] ' + (d.place || '행사'))}&body=${encodeURIComponent(body)}`;
    sent.hidden = false; sent.textContent = '메일 앱이 열립니다. 내용을 확인하고 보내 주세요.';
  });
})();

// 보도: 방송/기사 탭, 더 보기
(() => {
  const box = document.getElementById('press'), more = document.getElementById('pressmore');
  if (!box) return;
  const tabs = [...document.querySelectorAll('.press-tabs button')];
  tabs.forEach(b => b.addEventListener('click', () => { box.dataset.f = b.dataset.f; tabs.forEach(x => x.setAttribute('aria-pressed', x === b)); }));
  more.addEventListener('click', () => { const on = box.classList.toggle('all'); more.setAttribute('aria-expanded', on); more.textContent = on ? '접기' : '더 보기'; });
})();
