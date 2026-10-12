(function () {
    'use strict';

    // Same Google Apps Script endpoint as the root index.html. The script must be
    // updated to store the extra fields sent below (see flieber/README.md).
    var LEAD_ENDPOINT = 'https://script.google.com/macros/s/AKfycbyxJqxpm8cC45rl2Bi5i0KYGoETb6wOgzrAgQSdgnMMK3ojXCzwii_GRGSrAztOauGmlg/exec';

    var body = document.body;
    var path = body.dataset.path || 'home'; // home | build | run | neutral

    // ---------- Analytics hook (§15/§16): no-op until a tag manager is installed ----------
    window.dataLayer = window.dataLayer || [];
    function track(event, props) {
        var payload = Object.assign({ event: event, journey: path, page: location.pathname }, props || {});
        window.dataLayer.push(payload);
    }
    document.addEventListener('click', function (e) {
        var el = e.target.closest('[data-track]');
        if (!el) return;
        var to = el.getAttribute('data-track-path');
        track(el.getAttribute('data-track'), {
            label: (el.getAttribute('data-track-label') || el.textContent || '').trim().slice(0, 80),
            to_journey: to || undefined,
            cross_journey: !!(to && path !== 'home' && path !== 'neutral' && to !== path)
        });
    });

    // ---------- Local preview: make directory links work over file:// ----------
    if (location.protocol === 'file:') {
        document.querySelectorAll('a[href]').forEach(function (a) {
            var href = a.getAttribute('href');
            if (/^(https?:|mailto:|#)/.test(href)) return;
            var parts = href.split(/([?#].*)/);
            if (parts[0].endsWith('/')) a.setAttribute('href', parts[0] + 'index.html' + (parts[1] || ''));
            else if (parts[0] === '.' || parts[0] === '..') a.setAttribute('href', parts[0] + '/index.html' + (parts[1] || ''));
        });
    }

    // ---------- Navigation ----------
    var nav = document.querySelector('.site-nav');
    var triggers = Array.prototype.slice.call(document.querySelectorAll('.nav-trigger'));

    function closeAll(except) {
        triggers.forEach(function (t) {
            if (t === except) return;
            t.setAttribute('aria-expanded', 'false');
            var panel = document.getElementById(t.getAttribute('aria-controls'));
            if (panel) panel.classList.remove('open');
        });
    }

    triggers.forEach(function (t) {
        t.addEventListener('click', function () {
            var open = t.getAttribute('aria-expanded') === 'true';
            closeAll(t);
            t.setAttribute('aria-expanded', String(!open));
            document.getElementById(t.getAttribute('aria-controls')).classList.toggle('open', !open);
        });
    });

    document.addEventListener('click', function (e) {
        if (!e.target.closest('.nav-menu > li')) closeAll();
    });

    document.addEventListener('keydown', function (e) {
        if (e.key !== 'Escape') return;
        var openTrigger = triggers.find(function (t) { return t.getAttribute('aria-expanded') === 'true'; });
        closeAll();
        if (openTrigger) openTrigger.focus();
        if (nav && nav.classList.contains('open')) setMobile(false);
    });

    var toggle = document.querySelector('.nav-toggle');
    function setMobile(open) {
        nav.classList.toggle('open', open);
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
        document.documentElement.style.overflow = open ? 'hidden' : '';
    }
    if (toggle) {
        toggle.addEventListener('click', function () {
            setMobile(!nav.classList.contains('open'));
        });
    }

    // ---------- Verify markers: append ?verify to any URL to highlight unverified claims ----------
    if (/[?&]verify\b/.test(location.search)) body.classList.add('show-verify');

    // ---------- Scroll reveal ----------
    var reveals = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
            });
        }, { rootMargin: '0px 0px -8% 0px' });
        reveals.forEach(function (el) { io.observe(el); });
    } else {
        reveals.forEach(function (el) { el.classList.add('in'); });
    }

    // ---------- Toast ----------
    function toast(msg, isError) {
        var t = document.getElementById('toast');
        if (!t) return;
        t.textContent = msg;
        t.classList.toggle('error', !!isError);
        t.classList.add('show');
        setTimeout(function () { t.classList.remove('show'); }, 3500);
    }

    // ---------- Contact page: prefill from query string ----------
    var params = new URLSearchParams(location.search);
    var contactForm = document.getElementById('contact-form');
    if (contactForm) {
        var intent = params.get('intent');
        var journey = params.get('path');
        var app = params.get('app');
        if (intent) {
            // Narrower intents from CTAs map onto the three visible choices; the original is kept in "requested".
            var requested = contactForm.querySelector('input[name="requested"]');
            if (requested) requested.value = intent;
            intent = { walkthrough: 'demo', templates: 'expert' }[intent] || intent;
            var radio = contactForm.querySelector('input[name="intent"][value="' + intent + '"]');
            if (radio) radio.checked = true;
        }
        if (journey) {
            var sel = contactForm.querySelector('select[name="path"]');
            if (sel && sel.querySelector('option[value="' + journey + '"]')) sel.value = journey;
        }
        if (app) {
            var uc = contactForm.querySelector('input[name="useCase"][value="' + app + '"]');
            if (uc) uc.checked = true;
        }
        var from = contactForm.querySelector('input[name="originPage"]');
        if (from) from.value = params.get('from') || document.referrer.replace(location.origin, '') || '';
    }

    // ---------- Lead forms ----------
    document.querySelectorAll('form[data-lead]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var button = form.querySelector('button[type="submit"]');
            var label = button.textContent;
            var err = form.querySelector('.form-error');
            if (err) err.textContent = '';

            var fd = new FormData(form);
            var data = {};
            fd.forEach(function (value, key) {
                data[key] = data[key] ? data[key] + ', ' + value : value;
            });
            data.intent = data.intent || form.dataset.intent || '';
            data.path = data.path || form.dataset.path || path;
            data.originPage = data.originPage || location.pathname;
            data.submittedAt = new Date().toISOString();
            data.source = 'flieber-site';

            button.disabled = true;
            button.textContent = 'Sending…';

            fetch(LEAD_ENDPOINT, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            }).then(function () {
                track('lead_submit', { intent: data.intent, lead_path: data.path });
                var success = form.dataset.success && document.getElementById(form.dataset.success);
                if (success) {
                    form.hidden = true;
                    success.hidden = false;
                    success.focus();
                } else {
                    form.reset();
                    toast("Thanks — we'll be in touch shortly.");
                }
            }).catch(function (ex) {
                console.error(ex);
                if (err) err.textContent = 'Something went wrong. Please try again.';
                else toast('Something went wrong. Please try again.', true);
            }).then(function () {
                button.disabled = false;
                button.textContent = label;
            });
        });
    });
})();
