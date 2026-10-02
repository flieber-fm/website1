/* Flieber — site interactions. No dependencies. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Nav: scrolled state + mobile menu ---------- */
  var nav = document.getElementById('nav');
  if (nav) {
    var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });

    var toggle = nav.querySelector('.nav-toggle');
    if (toggle) {
      toggle.addEventListener('click', function () {
        var open = nav.classList.toggle('open');
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      });
      nav.querySelectorAll('.nav-links a').forEach(function (a) {
        a.addEventListener('click', function () {
          nav.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
    }
  }

  /* ---------- Nav: Solutions menu (Option 2) ---------- */
  // Click or Enter opens it; Escape, a click outside or focus leaving closes it.
  // In the collapsed phone menu the list is always shown (CSS), so the button does nothing there.
  document.querySelectorAll('.nav-drop').forEach(function (drop) {
    var btn = drop.querySelector('.nav-drop-btn');
    var set = function (open) {
      drop.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
    };
    btn.addEventListener('click', function () { set(!drop.classList.contains('open')); });
    drop.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drop.classList.contains('open')) { set(false); btn.focus(); }
    });
    drop.addEventListener('focusout', function (e) { if (!drop.contains(e.relatedTarget)) set(false); });
    document.addEventListener('click', function (e) { if (!drop.contains(e.target)) set(false); });
  });

  /* ---------- How Flieber is built: scroll-driven layer stack (Option 2, after legora.com) ---------- */
  // Scroll position maps to x: plate i drops while x goes from i to i+1, then the plates close up
  // into one block (x from n to n+1). Reduced motion keeps the static, fully open version.
  var ls = document.getElementById('layerstack');
  if (ls) {
    if (reduceMotion) {
      ls.classList.add('ls-static');
    } else {
      var iso = document.getElementById('iso');
      var pin = ls.querySelector('.ls-pin');
      var plates = [].slice.call(ls.querySelectorAll('.iso-plate'));
      var steps = [].slice.call(ls.querySelectorAll('.ls-step'));
      var bar = ls.querySelector('.ls-progress');
      var n = plates.length, X0 = 0.8, X1 = n + 1.3;
      var GAP = 46, T = 12, DROP = 420;
      var clamp = function (v, a, b) { return Math.max(a, Math.min(b, v)); };
      var ease = function (v) { return 1 - Math.pow(1 - v, 3); };
      var current = -1, ticking = false;

      var setActive = function (k) {
        if (k === current) return;
        current = k;
        steps.forEach(function (s, i) {
          var on = i === k;
          s.classList.toggle('is-active', on);
          s.querySelector('.ls-pill').setAttribute('aria-expanded', String(on));
        });
      };
      var render = function () {
        ticking = false;
        var total = ls.offsetHeight - pin.offsetHeight;
        var p = total > 0 ? clamp(-ls.getBoundingClientRect().top / total, 0, 1) : 0;
        var x = X0 + p * (X1 - X0);
        var f = ease(clamp(x - n, 0, 1));
        var gap = GAP * (1 - f) + T * f;
        var top = 0;
        plates.forEach(function (pl, i) {
          var d = ease(clamp(x - i, 0, 1));
          var rest = i * gap;
          pl.style.setProperty('--z', (rest + (1 - d) * DROP).toFixed(1));
          pl.style.setProperty('--o', clamp(d * 2.2, 0, 1).toFixed(3));
          top = Math.max(top, rest * d);
        });
        var k = clamp(Math.floor(x), 0, n - 1);
        plates.forEach(function (pl, i) { pl.classList.toggle('is-active', i === k && f < 0.05); });
        iso.style.setProperty('--lift', (-(top + T) / 2).toFixed(1));
        iso.style.setProperty('--f', f.toFixed(3));
        iso.classList.toggle('fused', f > 0.5);
        bar.style.setProperty('--p', p.toFixed(3));
        setActive(k);
      };
      var request = function () { if (!ticking) { ticking = true; requestAnimationFrame(render); } };
      window.addEventListener('scroll', request, { passive: true });
      window.addEventListener('resize', request);
      // A pill jumps to the point where its layer has just landed.
      steps.forEach(function (s, i) {
        s.querySelector('.ls-pill').addEventListener('click', function () {
          var total = ls.offsetHeight - pin.offsetHeight;
          var p = clamp((i + 0.95 - X0) / (X1 - X0), 0, 1);
          window.scrollTo({ top: window.scrollY + ls.getBoundingClientRect().top + p * total, behavior: 'smooth' });
        });
      });
      render();
    }
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in-view'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in-view'); });
  }

  /* ---------- Hero decision simulation: four sample scenarios ---------- */
  // Tabs work on click and arrow keys. Autoplay advances when the active tab's
  // progress bar finishes, so pausing the bar (hover, focus, off screen) also
  // pauses the rotation. The pause button stops it; reduced motion disables it.
  var sim = document.getElementById('sim');
  if (sim) {
    var tabs = [].slice.call(sim.querySelectorAll('.sim-tab'));
    var panels = [].slice.call(sim.querySelectorAll('.sim-panel'));
    var pauseBtn = sim.querySelector('.sim-pause');
    var cur = 0, userPaused = reduceMotion, holds = {};

    var show = function (n, focus) {
      cur = (n + tabs.length) % tabs.length;
      tabs.forEach(function (t, i) {
        var on = i === cur;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
      });
      panels.forEach(function (p, i) {
        var on = i === cur;
        p.classList.toggle('active', on);
        if (on) p.removeAttribute('aria-hidden'); else p.setAttribute('aria-hidden', 'true');
      });
      if (focus) tabs[cur].focus();
    };
    var sync = function () {
      var held = Object.keys(holds).some(function (k) { return holds[k]; });
      sim.classList.toggle('playing', !userPaused);
      sim.classList.toggle('paused', held);
      pauseBtn.setAttribute('aria-pressed', String(userPaused));
      pauseBtn.setAttribute('aria-label', userPaused ? 'Play rotation' : 'Pause rotation');
    };
    var hold = function (key, on) { holds[key] = on; sync(); };

    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { show(i); });
      t.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); show(i + 1, true); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); show(i - 1, true); }
      });
      t.querySelector('.sim-progress').addEventListener('animationend', function () {
        if (i === cur && !userPaused) show(cur + 1);
      });
    });
    pauseBtn.addEventListener('click', function () { userPaused = !userPaused; sync(); });
    sim.addEventListener('mouseenter', function () { hold('hover', true); });
    sim.addEventListener('mouseleave', function () { hold('hover', false); });
    sim.addEventListener('focusin', function () { hold('focus', true); });
    sim.addEventListener('focusout', function (e) { if (!sim.contains(e.relatedTarget)) hold('focus', false); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) { hold('offscreen', !entries[0].isIntersecting); }, { threshold: 0.25 }).observe(sim);
    }
    document.addEventListener('visibilitychange', function () { hold('hidden', document.hidden); });
    show(0);
    sync();
  }

  /* ---------- Quotes carousel ---------- */
  var carousel = document.getElementById('quotes');
  if (carousel) {
    var slides = carousel.querySelectorAll('.quote');
    var dotsWrap = carousel.querySelector('.quote-dots');
    var current = 0, timer = null;
    var dots = [];

    slides.forEach(function (_, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Show quote ' + (i + 1));
      b.addEventListener('click', function () { go(i); restart(); });
      dotsWrap.appendChild(b);
      dots.push(b);
    });

    var go = function (n) {
      current = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) {
        var on = i === current;
        s.classList.toggle('active', on);
        s.setAttribute('aria-hidden', String(!on));
      });
      dots.forEach(function (d, i) { d.setAttribute('aria-current', String(i === current)); });
    };
    var restart = function () {
      if (timer) clearInterval(timer);
      if (!reduceMotion) timer = setInterval(function () { go(current + 1); }, 7000);
    };

    carousel.querySelectorAll('[data-dir]').forEach(function (btn) {
      btn.addEventListener('click', function () { go(current + Number(btn.getAttribute('data-dir'))); restart(); });
    });
    carousel.addEventListener('mouseenter', function () { if (timer) clearInterval(timer); });
    carousel.addEventListener('mouseleave', restart);
    carousel.addEventListener('focusin', function () { if (timer) clearInterval(timer); });

    go(0);
    restart();
  }

  /* ---------- Logo strip: drop any logo file that fails to load ---------- */
  document.querySelectorAll('.logos-track img').forEach(function (img) {
    var drop = function () { img.remove(); };
    if (img.complete && img.naturalWidth === 0 && img.getAttribute('src')) drop();
    else img.addEventListener('error', drop);
  });

  /* ---------- Copy to clipboard ---------- */
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var src = document.querySelector(btn.getAttribute('data-copy'));
      if (!src || !navigator.clipboard) return;
      navigator.clipboard.writeText(src.textContent.trim()).then(function () {
        var label = btn.textContent;
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = label; }, 1600);
      });
    });
  });

  /* ---------- Placeholder links (see README "Open items") ---------- */
  // Links whose destination is still a [BRACKET] placeholder stay on the page
  // and show the pending placeholder on hover instead of jumping to "#".
  document.querySelectorAll('a[data-placeholder]').forEach(function (a) {
    a.setAttribute('title', 'Destination pending: ' + a.getAttribute('data-placeholder'));
    a.addEventListener('click', function (e) { e.preventDefault(); });
  });

  /* ---------- Agents page: highlight current section in TOC ---------- */
  var toc = document.querySelectorAll('.doc-toc nav a');
  if (toc.length && 'IntersectionObserver' in window) {
    var map = {};
    toc.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && map[e.target.id]) {
          toc.forEach(function (a) { a.classList.remove('active'); });
          map[e.target.id].classList.add('active');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) tio.observe(el); });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = String(new Date().getFullYear());
})();
