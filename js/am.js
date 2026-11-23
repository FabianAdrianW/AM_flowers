(() => {
  const root = document.documentElement;
  if (root.classList.contains('arrive')) {
    setTimeout(() => root.classList.add('arrive-go'), 650);
    setTimeout(() => root.classList.remove('arrive', 'arrive-go'), 1800);
  }
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const head = document.querySelector('.site-head');
  const brand = head.querySelector('.brand img');
  const burger = head.querySelector('.burger');
  const mnav = document.getElementById('mnav');
  const mbar = document.querySelector('.mbar');
  const hero = document.querySelector('.hero');

  /* header: transparent over hero, solid after */
  const setSolid = solid => {
    head.classList.toggle('is-solid', solid);
    brand.src = solid ? brand.dataset.dark : brand.dataset.light;
    mbar && mbar.classList.toggle('show', solid);
  };
  new IntersectionObserver(([e]) => setSolid(!e.isIntersecting), { rootMargin: '-72px 0px 0px 0px' }).observe(hero);

  /* mobile menu: Esc, focus trap, close on link */
  const focusables = () => [burger, ...mnav.querySelectorAll('a')];
  const openMenu = open => {
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Zamknij menu' : 'Otwórz menu');
    if (open) { mnav.hidden = false; requestAnimationFrame(() => mnav.classList.add('open')); head.classList.add('is-solid'); brand.src = brand.dataset.dark; }
    else { mnav.classList.remove('open'); setTimeout(() => { if (burger.getAttribute('aria-expanded') === 'false') mnav.hidden = true; }, 320); setSolid(hero.getBoundingClientRect().bottom < 72); }
    document.body.style.overflow = open ? 'hidden' : '';
  };
  burger.addEventListener('click', () => openMenu(burger.getAttribute('aria-expanded') !== 'true'));
  mnav.addEventListener('click', e => { if (e.target.closest('a')) openMenu(false); });
  document.addEventListener('keydown', e => {
    if (burger.getAttribute('aria-expanded') !== 'true') return;
    if (e.key === 'Escape') { openMenu(false); burger.focus(); }
    if (e.key === 'Tab') {
      const f = focusables(), first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });

  /* active section in nav */
  const links = [...document.querySelectorAll('.nav a')];
  const map = new Map(links.map(a => [a.getAttribute('href').slice(1), a]));
  const navObs = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    links.forEach(a => a.removeAttribute('aria-current'));
    const a = map.get(e.target.id); a && a.setAttribute('aria-current', 'true');
  }), { rootMargin: '-45% 0px -50% 0px' });
  [...map.keys()].forEach(id => { const el = document.getElementById(id); el && navObs.observe(el); });

  /* reveal on scroll */
  const rv = document.querySelectorAll('.rv');
  if (reduce || !('IntersectionObserver' in window)) rv.forEach(el => el.classList.add('in'));
  else {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    rv.forEach(el => io.observe(el));
  }

  /* hero video: desktop only, not with reduced motion or save-data */
  const media = hero.querySelector('.hero-media');
  const saveData = navigator.connection && navigator.connection.saveData;
  if (!reduce && !saveData && matchMedia('(min-width: 48em)').matches) {
    const v = document.createElement('video');
    Object.assign(v, { muted: true, loop: true, playsInline: true, autoplay: true, preload: 'auto' });
    v.setAttribute('muted', ''); v.setAttribute('playsinline', ''); v.setAttribute('aria-hidden', 'true');
    v.poster = 'img/hero-poster.webp';
    v.src = media.dataset.video;
    v.addEventListener('canplay', () => { media.querySelector('picture').replaceWith(v); }, { once: true });
    v.load();
    const btn = document.createElement('button');
    btn.className = 'hero-toggle'; btn.type = 'button';
    const icons = { pause: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14"/><rect x="14" y="5" width="4" height="14"/></svg>', play: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M7 5v14l12-7z"/></svg>' };
    const sync = () => { btn.innerHTML = v.paused ? icons.play : icons.pause; btn.setAttribute('aria-label', v.paused ? 'Odtwórz wideo w tle' : 'Zatrzymaj wideo w tle'); };
    btn.addEventListener('click', () => { v.paused ? v.play() : v.pause(); sync(); });
    v.addEventListener('play', sync); v.addEventListener('pause', sync);
    hero.appendChild(btn); sync();
    new IntersectionObserver(([e]) => { if (!e.isIntersecting) v.pause(); else if (btn.dataset.user !== 'paused') v.play().catch(() => {}); }).observe(hero);
    btn.addEventListener('click', () => { btn.dataset.user = v.paused ? 'paused' : ''; });
  }
})();

/* occasion calendar: highlights the next occasion */
(() => {
  const list = document.getElementById('calList'); if (!list) return;
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const y = today.getFullYear();
  const easter = yr => { const a = yr % 19, b = Math.floor(yr / 100), c = yr % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451), mo = Math.floor((h + l - 7 * m + 114) / 31), da = ((h + l - 7 * m + 114) % 31) + 1; return new Date(yr, mo - 1, da); };
  const def = yr => [
    { n: 'Walentynki', d: new Date(yr, 1, 14), t: 'Czerwone róże, flowerboxy i bukiety z bilecikiem. Zamów kilka dni wcześniej.' },
    { n: 'Dzień Kobiet', d: new Date(yr, 2, 8), t: 'Tulipany i małe bukiety, także zamówienia hurtowe dla firm.' },
    { n: 'Wielkanoc', d: easter(yr), t: 'Stroiki wielkanocne, gałązki i kompozycje na stół.' },
    { n: 'Dzień Matki', d: new Date(yr, 4, 26), t: 'Najbardziej pracowity dzień w pracowni. Zamów co najmniej dzień wcześniej.' },
    { n: 'Dzień Nauczyciela', d: new Date(yr, 9, 14), t: 'Małe bukiety i rośliny w doniczce, także dla całej klasy.' },
    { n: 'Wszystkich Świętych', d: new Date(yr, 10, 1), t: 'Wiązanki na groby, kompozycje nagrobne i znicze. Przygotujemy na wybrany dzień.' },
    { n: 'Boże Narodzenie', d: new Date(yr, 11, 24), t: 'Stroiki, wieńce adwentowe i bukiety z gałązkami. Zamów wcześniej, w grudniu pracownia ma pełne ręce.' },
  ];
  const all = [...def(y), ...def(y + 1)].filter(o => o.d >= today).slice(0, 4);
  const fmt = d => d.toLocaleDateString('pl-PL', { day: 'numeric', month: 'long' });
  const days = d => Math.round((d - today) / 864e5);
  const when = n => n === 0 ? 'dzisiaj' : n === 1 ? 'jutro' : `za ${n} dni`;
  list.innerHTML = all.map((o, i) => `<li${i === 0 ? ' class="is-next"' : ''}><span>${fmt(o.d)}</span><b>${o.n}</b><small>${when(days(o.d))}</small></li>`).join('');
  const next = all[0];
  document.getElementById('calName').textContent = next.n;
  document.getElementById('calWhen').textContent = `${fmt(next.d)}, ${when(days(next.d))}`;
  document.getElementById('calTip').textContent = next.t;
})();
