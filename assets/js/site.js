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

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-stagger, .pcard');
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

  /* ---------- Hero headline: rotating decision word ---------- */
  // Cycles through the list once and settles back on the first word, so the
  // headline doesn't keep moving while people read. Pauses on hover.
  var rotator = document.querySelector('.rotator');
  if (rotator && !reduceMotion) {
    var words = rotator.getAttribute('data-words').split('|');
    var wordEl = rotator.querySelector('.rotator-word');
    var idx = 0, paused = false, remaining = words.length;
    var measure = document.createElement('span');
    measure.setAttribute('aria-hidden', 'true');
    measure.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;left:-9999px;top:0';
    rotator.parentNode.appendChild(measure);
    var widthOf = function (w) {
      var cs = getComputedStyle(rotator);
      measure.style.font = cs.font;
      measure.style.letterSpacing = cs.letterSpacing;
      measure.textContent = w;
      return measure.getBoundingClientRect().width + parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight);
    };
    var setWidth = function () { rotator.style.width = widthOf(words[idx]) + 'px'; };
    var swap = function () {
      idx = (idx + 1) % words.length;
      wordEl.classList.add('out');
      setTimeout(function () {
        wordEl.textContent = words[idx];
        setWidth();
        wordEl.classList.remove('out');
        wordEl.classList.add('enter');
        void wordEl.offsetWidth;
        wordEl.classList.remove('enter');
      }, 380);
    };
    var loop = function () {
      if (remaining <= 0) return;
      if (!paused) { swap(); remaining--; }
      setTimeout(loop, 1900);
    };
    rotator.addEventListener('mouseenter', function () { paused = true; });
    rotator.addEventListener('mouseleave', function () { paused = false; });
    window.addEventListener('resize', setWidth);
    var start = function () { setWidth(); setTimeout(loop, 1600); };
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(start); else start();
  }

  /* ---------- Hero console: an agent asks, Flieber answers ---------- */
  var consoleEl = document.getElementById('console');
  if (consoleEl) {
    var steps = consoleEl.querySelectorAll('[data-step]');
    var typed = consoleEl.querySelector('.typed');
    var call = consoleEl.querySelector('.tool-call');
    var showAll = function () {
      steps.forEach(function (s) { s.classList.add('in'); });
      if (call) call.classList.add('done');
    };

    if (reduceMotion || !typed) {
      showAll();
    } else {
      var text = typed.getAttribute('data-text') || typed.textContent;
      typed.textContent = '';
      var run = function () {
        steps[0].classList.add('in');
        var i = 0;
        var tick = function () {
          typed.textContent = text.slice(0, ++i);
          if (i < text.length) { setTimeout(tick, 22 + Math.random() * 28); return; }
          setTimeout(function () { steps[1].classList.add('in'); }, 350);
          setTimeout(function () { call.classList.add('done'); steps[2].classList.add('in'); }, 1500);
          setTimeout(function () { steps[3].classList.add('in'); }, 2200);
        };
        setTimeout(tick, 400);
      };
      if ('IntersectionObserver' in window) {
        var cio = new IntersectionObserver(function (entries) {
          if (entries[0].isIntersecting) { cio.disconnect(); run(); }
        }, { threshold: 0.3 });
        cio.observe(consoleEl);
      } else { run(); }
    }
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
  // Links whose destination is not confirmed yet carry data-todo. Until the URL
  // is filled in, route them to the "Try it" section instead of a dead "#".
  document.querySelectorAll('a[data-todo][href="#"]').forEach(function (a) {
    if (document.getElementById('try')) a.setAttribute('href', '#try');
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
