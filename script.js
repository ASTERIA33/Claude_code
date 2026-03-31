/* ============================================
   ELOPEMENT INTIME — Script
   ============================================ */

// ── Navigation scroll behaviour ──
const nav = document.getElementById('nav');

function onScroll() {
  if (window.scrollY > 60) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
}

window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// ── Burger menu ──
const burger = document.getElementById('burger');
const navLinks = document.getElementById('navLinks');

burger.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  burger.classList.toggle('open', isOpen);
  burger.setAttribute('aria-expanded', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
});

// Close menu when a link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    burger.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  });
});

// Close menu on outside click
navLinks.addEventListener('click', e => {
  if (e.target === navLinks) {
    navLinks.classList.remove('open');
    burger.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
});

// ── Scroll reveal ──
const revealEls = document.querySelectorAll(
  '.concept__text, .concept__visual, .service-card, .step, ' +
  '.galerie__item, .temoignage, .contact__text, .contact__form, ' +
  '.stat, .section-header'
);

revealEls.forEach((el, i) => {
  el.classList.add('reveal');
  // Stagger siblings at the same level
  const parent = el.parentElement;
  const siblings = [...parent.children].filter(c => c.classList.contains('reveal'));
  const idx = siblings.indexOf(el);
  if (idx > 0 && idx <= 3) {
    el.classList.add(`reveal-delay-${idx}`);
  }
});

const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);

revealEls.forEach(el => observer.observe(el));

// ── Smooth active nav link ──
const sections = document.querySelectorAll('section[id]');
const navAnchors = document.querySelectorAll('.nav__links a[href^="#"]');

const sectionObserver = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navAnchors.forEach(a => {
          a.classList.toggle('active', a.getAttribute('href') === `#${id}`);
        });
      }
    });
  },
  { threshold: 0.4 }
);

sections.forEach(s => sectionObserver.observe(s));

// ── Contact form ──
const form = document.getElementById('contactForm');

form.addEventListener('submit', e => {
  e.preventDefault();

  const btn = form.querySelector('button[type="submit"]');
  const original = btn.textContent;

  // Simple validation
  const email = form.querySelector('#email');
  if (!email.value || !email.value.includes('@')) {
    email.focus();
    email.style.borderColor = '#C0392B';
    setTimeout(() => email.style.borderColor = '', 2000);
    return;
  }

  // Simulate submission
  btn.textContent = 'Envoi en cours…';
  btn.disabled = true;

  setTimeout(() => {
    btn.textContent = 'Message envoyé ✓';
    btn.style.background = '#4A7C59';

    setTimeout(() => {
      btn.textContent = original;
      btn.style.background = '';
      btn.disabled = false;
      form.reset();
    }, 3500);
  }, 1200);
});

// ── Parallax hero (subtle, performance-safe) ──
const heroBg = document.querySelector('.hero__bg');

if (heroBg && window.matchMedia('(min-width: 1024px)').matches) {
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        heroBg.style.transform = `translateY(${scrollY * 0.25}px)`;
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}
