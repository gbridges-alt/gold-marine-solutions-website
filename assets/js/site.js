/* Gold Marine Solutions — shared behaviour.
   Extracted from production index.html; guarded so every page can load it. */
(function () {
  'use strict';

  // Dynamic copyright year
  var yearEl = document.getElementById('year');
  if (yearEl) { yearEl.textContent = new Date().getFullYear(); }

  // Mobile hamburger menu
  var hamburger = document.getElementById('hamburger');
  var mobileMenu = document.getElementById('mobileMenu');

  function closeMenu() {
    if (!hamburger || !mobileMenu) { return; }
    hamburger.classList.remove('open');
    mobileMenu.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
  }

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      var open = hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open', open);
      hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    document.addEventListener('click', function (e) {
      if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) { closeMenu(); }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeMenu(); }
    });
  }

  // FAQ accordion
  var faqButtons = document.querySelectorAll('.faq-q');
  faqButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var answer = btn.nextElementSibling;
      var isOpen = btn.classList.contains('open');
      faqButtons.forEach(function (b) {
        b.classList.remove('open');
        b.setAttribute('aria-expanded', 'false');
        if (b.nextElementSibling) { b.nextElementSibling.classList.remove('open'); }
      });
      if (!isOpen) {
        btn.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
        if (answer) { answer.classList.add('open'); }
      }
    });
  });

  // Contact form: preselect the enquiry type from ?type= so a CTA carries its
  // originating intent through to the form. No separate booking pages — every
  // CTA posts to the same /contact/ enquiry form.
  var enquiryType = document.getElementById('c-enquiry-type');
  if (enquiryType) {
    var wanted = null;
    try {
      wanted = new URLSearchParams(window.location.search).get('type');
    } catch (e) { /* older browser — leave the field unset */ }
    if (wanted) {
      wanted = wanted.toLowerCase();
      for (var i = 0; i < enquiryType.options.length; i++) {
        if (enquiryType.options[i].value === wanted) {
          enquiryType.selectedIndex = i;
          break;
        }
      }
    }
  }
})();
