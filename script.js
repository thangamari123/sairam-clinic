/**
 * Sairam Dental Care – Main JavaScript
 * Handles all interactions across the 13 sections
 */

'use strict';

/* ─────────── UTILS ─────────── */
const $ = (sel, ctx = document) => ctx ? ctx.querySelector(sel) : null;
const $$ = (sel, ctx = document) => ctx ? [...ctx.querySelectorAll(sel)] : [];
const clamp = (v, min, max) => Math.min(Math.max(v, min), max);
const lerp = (a, b, t) => a + (b - a) * t;

/* ─────────── NAVBAR SCROLL & MENU ─────────── */
function initNavbar() {
  const navbar = $('#navbar');
  const hamburger = $('#hamburger-btn');
  const mobileMenu = $('#mobile-menu');
  let lastScroll = 0;
  let ticking = false;

  // Scroll effect
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        if (window.scrollY > 20) navbar.classList.add('scrolled');
        else navbar.classList.remove('scrolled');
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });

  // Mobile menu toggle
  function toggleMenu(open) {
    hamburger.classList.toggle('open', open);
    mobileMenu.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', String(open));
  }

  hamburger?.addEventListener('click', () => {
    toggleMenu(!mobileMenu.classList.contains('open'));
  });

  const mbMoreBtn = $('#mb-more-btn');
  mbMoreBtn?.addEventListener('click', () => {
    toggleMenu(!mobileMenu.classList.contains('open'));
  });

  // Close menu on link click
  $$('.mobile-nav-link, .mob-cta', mobileMenu).forEach(link => {
    link.addEventListener('click', () => toggleMenu(false));
  });

  // Active Link Highlight
  const sections = $$('section[id]');
  const links = $$('.nav-link');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        links.forEach(l => l.classList.remove('active'));
        const activeLink = $(`a[href="#${entry.target.id}"].nav-link`);
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }, { threshold: 0.3, rootMargin: '-80px 0px 0px 0px' });

  sections.forEach(s => observer.observe(s));
}

/* ─────────── SCROLL REVEAL ANIMATIONS ─────────── */
function initScrollReveal() {
  const elements = $$('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target); // Reveal only once
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

  elements.forEach(el => observer.observe(el));
}

/* ─────────── STAT COUNTERS ─────────── */
function initCounters() {
  const stats = $$('.sb-number[data-target]');
  if (!stats.length) return;

  function easeOutQuart(t) { return 1 - Math.pow(1 - t, 4); }

  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 2500;
    const start = performance.now();

    function tick(now) {
      const elapsed = now - start;
      const progress = clamp(elapsed / duration, 0, 1);
      const current = Math.round(easeOutQuart(progress) * target);
      el.textContent = current + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  stats.forEach(el => observer.observe(el));
}


/* ─────────── TESTIMONIAL SLIDER ─────────── */
function initTestimonials() {
  const slider = $('#testi-slider');
  const prevBtn = $('#testi-prev');
  const nextBtn = $('#testi-next');
  const dotsContainer = $('#testi-dots');
  const cards = $$('.testi-card');
  if (!slider || !cards.length) return;

  let currentIndex = 0;
  let autoplayInt;

  // Create dots
  cards.forEach((_, i) => {
    const dot = document.createElement('button');
    dot.className = `tdot ${i === 0 ? 'active' : ''}`;
    dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
    dot.addEventListener('click', () => goTo(i));
    dotsContainer.appendChild(dot);
  });
  const dots = $$('.tdot', dotsContainer);

  function updateActive() {
    dots.forEach((d, i) => d.classList.toggle('active', i === currentIndex));
  }

  function goTo(index) {
    currentIndex = (index + cards.length) % cards.length;
    const cardWidth = cards[0].offsetWidth;
    // Calculate gap
    const gap = parseInt(window.getComputedStyle(slider).gap) || 0;
    slider.scrollTo({ left: currentIndex * (cardWidth + gap), behavior: 'smooth' });
    updateActive();
    resetAutoplay();
  }

  prevBtn?.addEventListener('click', () => goTo(currentIndex - 1));
  nextBtn?.addEventListener('click', () => goTo(currentIndex + 1));

  // Sync scroll with dots
  slider.addEventListener('scroll', () => {
    const cardWidth = cards[0].offsetWidth;
    const index = Math.round(slider.scrollLeft / cardWidth);
    if (index !== currentIndex) {
      currentIndex = index;
      updateActive();
    }
  }, { passive: true });

  // Autoplay
  function resetAutoplay() {
    clearInterval(autoplayInt);
    autoplayInt = setInterval(() => goTo(currentIndex + 1), 6000);
  }
  
  slider.addEventListener('mouseenter', () => clearInterval(autoplayInt));
  slider.addEventListener('mouseleave', resetAutoplay);
  resetAutoplay();
}

/* ─────────── FAQ ACCORDION ─────────── */
function initFAQ() {
  const questions = $$('.faq-q');
  
  questions.forEach(q => {
    q.addEventListener('click', () => {
      const isExpanded = q.getAttribute('aria-expanded') === 'true';
      const answer = document.getElementById(q.getAttribute('aria-controls'));
      
      // Close all others
      questions.forEach(otherQ => {
        if (otherQ !== q) {
          otherQ.setAttribute('aria-expanded', 'false');
          const otherA = document.getElementById(otherQ.getAttribute('aria-controls'));
          otherA.style.maxHeight = null;
        }
      });

      // Toggle current
      if (isExpanded) {
        q.setAttribute('aria-expanded', 'false');
        answer.style.maxHeight = null;
      } else {
        q.setAttribute('aria-expanded', 'true');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });
}

/* ─────────── APPOINTMENT FORM ─────────── */
function initForm() {
  const form = $('#appointment-form');
  if (!form) return;

  // Set minimum date to today
  const dateInput = $('#f-date');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.min = today;
  }

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Basic validation
    const name = $('#f-name').value;
    const phone = $('#f-phone').value;
    
    if (!name || !phone) {
      showToast('⚠️ Please fill in all required fields.');
      return;
    }

    // Simulate API call
    const btn = $('#appt-submit-btn');
    const ogHtml = btn.innerHTML;
    btn.innerHTML = 'Booking...';
    btn.disabled = true;

    setTimeout(() => {
      showToast('✅ Appointment Request Sent! Our team will contact you shortly.');
      form.reset();
      btn.innerHTML = ogHtml;
      btn.disabled = false;
    }, 1500);
  });
}

/* ─────────── TOAST NOTIFICATION ─────────── */
function showToast(message, duration = 4000) {
  const existing = $('.sdc-toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.className = 'sdc-toast';
  toast.textContent = message;

  Object.assign(toast.style, {
    position: 'fixed', bottom: '28px', left: '50%', transform: 'translate(-50%, 20px)',
    background: 'var(--navy)', color: 'white', padding: '14px 24px',
    borderRadius: 'var(--radius-pill)', fontSize: '0.9rem', fontWeight: '500',
    boxShadow: 'var(--shadow-lg)', zIndex: '9999', opacity: '0',
    transition: 'all 0.3s cubic-bezier(0.34,1.56,0.64,1)',
    textAlign: 'center', minWidth: '300px'
  });

  document.body.appendChild(toast);

  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      toast.style.opacity = '1';
      toast.style.transform = 'translate(-50%, 0)';
    });
  });

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translate(-50%, 12px)';
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

/* ─────────── SMOOTH SCROLL & SCROLL TO TOP ─────────── */
function initScrollUtils() {
  // Smooth anchor scrolling
  $$('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#') return;
      const target = $(href);
      if (!target) return;
      e.preventDefault();
      const navH = 76;
      const top = target.getBoundingClientRect().top + window.scrollY - navH - 16;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
}

/* ─────────── HERO INTERACTIONS (Kept from prev) ─────────── */
function initHeroVisuals() {
  // Particles
  const container = $('#particles-container');
  if (container) {
    const colors = ['rgba(14,165,233,0.35)', 'rgba(26,79,160,0.25)', 'rgba(56,189,248,0.30)'];
    for (let i=0; i<28; i++) {
      const el = document.createElement('div');
      el.className = 'particle';
      const size = Math.random() * 7 + 3;
      Object.assign(el.style, {
        position: 'absolute', width: size+'px', height: size+'px',
        background: colors[Math.floor(Math.random()*colors.length)],
        left: (Math.random()*100)+'%', top: (Math.random()*100)+'%',
        borderRadius: '50%', pointerEvents: 'none',
        animation: `particleDrift ${Math.random()*14+14}s linear infinite`,
        animationDelay: `-${Math.random()*20}s`,
        '--dx': `${Math.random()*240-120}px`,
        '--dy': `${Math.random()*-140-60}px`,
        opacity: Math.random()*0.5+0.3
      });
      container.appendChild(el);
    }
  }

  // Tooth 3D Tilt
  const tooth = $('#tooth-model');
  const scene = $('#visual-scene');
  if (scene && tooth) {
    scene.addEventListener('mousemove', (e) => {
      const r = scene.getBoundingClientRect();
      const dx = (e.clientX - (r.left + r.width/2)) / (r.width/2);
      const dy = (e.clientY - (r.top + r.height/2)) / (r.height/2);
      tooth.style.transform = `perspective(600px) rotateY(${dx*12}deg) rotateX(${-dy*8}deg) translateZ(12px)`;
    });
    scene.addEventListener('mouseleave', () => tooth.style.transform = '');
  }

  // Orbit pause
  const orbit = $('#orbit-system');
  $$('.orbit-card').forEach(card => {
    card.addEventListener('mouseenter', () => orbit.style.animationPlayState = 'paused');
    card.addEventListener('mouseleave', () => orbit.style.animationPlayState = 'running');
  });
}

/* ─────────── BACKGROUND SLIDER ─────────── */
function initBackgroundSlider() {
  const slides = $$('.bg-slide');
  if (!slides.length) return;
  
  const dotsContainer = $('#slider-dots');
  const prevBtn = $('.slider-arrow.prev');
  const nextBtn = $('.slider-arrow.next');
  let current = 0;
  let timer;

  // Create dots
  if (dotsContainer) {
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = `slider-dot ${i === 0 ? 'active' : ''}`;
      dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
      dot.addEventListener('click', () => goToSlide(i));
      dotsContainer.appendChild(dot);
    });
  }

  const dots = $$('.slider-dot', dotsContainer);

  function goToSlide(index) {
    slides[current].classList.remove('active');
    if (dots.length) dots[current].classList.remove('active');
    
    current = (index + slides.length) % slides.length;
    
    slides[current].classList.add('active');
    if (dots.length) dots[current].classList.add('active');
    
    resetTimer();
  }

  function nextSlide() { goToSlide(current + 1); }
  function prevSlide() { goToSlide(current - 1); }

  function resetTimer() {
    clearInterval(timer);
    timer = setInterval(nextSlide, 5000);
  }

  if (prevBtn) prevBtn.addEventListener('click', prevSlide);
  if (nextBtn) nextBtn.addEventListener('click', nextSlide);

  resetTimer();
}

/* ─────────── SMILE GALLERY SLIDER & TABS ─────────── */
function initSmileGallery() {
  const container = $('.gallery-section');
  if (!container) return;

  const tabs = $$('.gallery-tab', container);
  const rangeInput = $('#slider-range-input', container);
  const afterWrapper = $('#slider-after-wrapper', container);
  const handle = $('#slider-handle', container);

  const beforeImg = $('#slider-before-img', container);
  const afterImg = $('#slider-after-img', container);
  const titleEl = $('#gallery-card-title', container);
  const descEl = $('#gallery-card-desc', container);
  const cardInfo = $('.gallery-card-info', container);
  const sliderContainer = $('.comparison-slider-container', container);

  if (!rangeInput || !afterWrapper || !handle || !beforeImg || !afterImg) return;

  // Data for each treatment category
  // Both before/after use the same source image;
  // CSS filters create the visual "before" look on the left side.
  const galleryData = {
    'smile-makeover': {
      beforeSrc: 'images/before and after/smile_makeover_before.png',
      afterSrc: 'images/before and after/smile_makeover_after.png',
      title: 'Complete Smile Makeover',
      desc: 'Full mouth rehabilitation with implants and porcelain crowns — see the dramatic before & after difference.',
      beforeFilter: 'none',
      afterFilter: 'none'
    },
    'teeth-whitening': {
      beforeSrc: 'images/before and after/teeth_whitening_before.png',
      afterSrc: 'images/before and after/teeth_whitening_after.png',
      title: 'Laser Teeth Whitening',
      desc: 'In-office laser whitening that brightened teeth by up to 8 shades in a single session.',
      beforeFilter: 'none',
      afterFilter: 'none'
    },
    'dental-implants': {
      beforeSrc: 'images/before and after/dental_implants_before.png',
      afterSrc: 'images/before and after/dental_implants_after.png',
      title: 'Dental Implants',
      desc: 'Premium titanium implants restoring a natural, confident smile where teeth were missing.',
      beforeFilter: 'none',
      afterFilter: 'none'
    },
    'invisalign': {
      beforeSrc: 'images/before and after/Invisalign Treatment before.jpeg',
      afterSrc: 'images/before and after/Invisalign Treatment after.jpeg',
      title: 'Invisalign Treatment',
      desc: 'Clear aligner therapy correcting crowding and bite issues — nearly invisible throughout.',
      beforeFilter: 'none',
      afterFilter: 'none'
    },
    'orthodontics': {
      beforeSrc: 'images/before and after/braces_before.png',
      afterSrc: 'images/before and after/braces_after.png',
      title: 'Orthodontic Treatment',
      desc: 'Traditional braces for comprehensive teeth alignment and bite correction.',
      beforeFilter: 'none',
      afterFilter: 'none'
    }
  };

  // FIX: Reveal "AFTER" from the LEFT as handle moves right.
  // clip-path: inset(0 X% 0 0) clips the right side — so at 50%, the right half is hidden.
  // As val increases toward 100, more of the after image is revealed from left.
  // We want: handle at left = show mostly BEFORE, handle at right = show mostly AFTER.
  // So: clip the after-wrapper from the RIGHT by (100 - val)%.
  function updateSlider(val) {
    const pct = parseFloat(val);
    // Clip right side of the after-wrapper: at val=0 → clip 100% (hidden), at val=100 → clip 0% (fully shown)
    afterWrapper.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
    handle.style.left = `${pct}%`;
    rangeInput.value = pct;
  }

  // Apply filters to loaded images
  function applyData(data, animate) {
    const doSwap = () => {
      beforeImg.src = data.beforeSrc || data.src;
      afterImg.src = data.afterSrc || data.src;
      beforeImg.style.filter = data.beforeFilter || 'none';
      afterImg.style.filter = data.afterFilter || 'none';
      titleEl.textContent = data.title;
      descEl.textContent = data.desc;
      updateSlider(50);
    };

    if (animate) {
      sliderContainer.style.transition = 'opacity 0.22s ease';
      cardInfo.style.transition = 'opacity 0.22s ease';
      sliderContainer.style.opacity = '0';
      cardInfo.style.opacity = '0';
      setTimeout(() => {
        doSwap();
        sliderContainer.style.opacity = '1';
        cardInfo.style.opacity = '1';
      }, 220);
    } else {
      doSwap();
    }
  }

  // Range input events — add dragging class to disable clip-path transition during live drag
  const dragHint = $('#slider-drag-hint', container);
  let hintHidden = false;

  function hideHint() {
    if (!hintHidden && dragHint) {
      hintHidden = true;
      dragHint.classList.add('hidden');
    }
  }

  rangeInput.addEventListener('mousedown', () => sliderContainer.classList.add('dragging'));
  rangeInput.addEventListener('touchstart', () => sliderContainer.classList.add('dragging'), { passive: true });
  window.addEventListener('mouseup', () => sliderContainer.classList.remove('dragging'));
  window.addEventListener('touchend', () => sliderContainer.classList.remove('dragging'));

  rangeInput.addEventListener('input', (e) => {
    updateSlider(e.target.value);
    hideHint();
  });
  rangeInput.addEventListener('change', (e) => updateSlider(e.target.value));

  // Tab switching
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      if (tab.classList.contains('active')) return;
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const data = galleryData[tab.dataset.treatment];
      if (data) applyData(data, true);
    });
  });

  // Initialize with default tab
  const defaultData = galleryData['smile-makeover'];
  applyData(defaultData, false);

  // Animate slider handle once on first intersection to hint draggability
  let hintDone = false;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !hintDone) {
        hintDone = true;
        observer.disconnect();
        // Animate: slide handle left then right then back to 50%, then hide hint
        setTimeout(() => {
          updateSlider(30);
          setTimeout(() => {
            updateSlider(70);
            setTimeout(() => {
              updateSlider(50);
              // Hide the hint after animation
              setTimeout(() => hideHint(), 600);
            }, 500);
          }, 500);
        }, 800);
      }
    });
  }, { threshold: 0.4 });
  observer.observe(sliderContainer);
}

/* ─────────── INIT ALL ─────────── */
document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initScrollReveal();
  initCounters();
  initTestimonials();
  initFAQ();
  initForm();
  initScrollUtils();
  initHeroVisuals();
  initBackgroundSlider();
  initSmileGallery();
  initDoctorSlider();
  initBlogSlider();
});

/* ─────────── DOCTOR CARD MOBILE SLIDER ─────────── */
function initDoctorSlider() {
  const slider = $('#dc-slider');
  const dots = $$('.dc-dot', document);
  if (!slider || !dots.length) return;

  // Only run on mobile (≤700px)
  const mq = window.matchMedia('(max-width: 700px)');

  function syncDots() {
    if (!mq.matches) return;
    const cards = $$('.doctor-card--photo', slider);
    if (!cards.length) return;
    const cardW = cards[0].offsetWidth + 16; // width + gap
    const index = Math.round(slider.scrollLeft / cardW);
    dots.forEach((dot, i) => dot.classList.toggle('active', i === index));
  }

  // Dot tap → scroll to card
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      if (!mq.matches) return;
      const cards = $$('.doctor-card--photo', slider);
      if (!cards[i]) return;
      cards[i].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    });
  });

  slider.addEventListener('scroll', syncDots, { passive: true });
  window.addEventListener('resize', syncDots, { passive: true });
  syncDots();
}

// Particle Keyframes fallback
if (!$('#particle-styles')) {
  const style = document.createElement('style');
  style.id = 'particle-styles';
  style.textContent = `@keyframes particleDrift { to { transform: translate(var(--dx), var(--dy)) scale(0.5); opacity: 0; } }`;
  document.head.appendChild(style);
}

// Footer Accordion on Mobile
document.addEventListener('DOMContentLoaded', () => {
  const footerCols = document.querySelectorAll('.footer-col h4');
  footerCols.forEach(col => {
    col.addEventListener('click', () => {
      if (window.innerWidth <= 768) {
        col.parentElement.classList.toggle('active');
      }
    });
  });
});

/* ─────────── BLOG CAROUSEL ─────────── */
function initBlogSlider() {
  const track      = document.getElementById('blog-carousel-track');
  const dotsWrap   = document.getElementById('blog-carousel-dots');
  const prevBtn    = document.getElementById('blog-prev-btn');
  const nextBtn    = document.getElementById('blog-next-btn');
  if (!track) return;

  const cards      = Array.from(track.querySelectorAll('.blog-card'));
  const total      = cards.length;
  let current      = 0;
  let autoTimer    = null;

  /* How many cards visible at once? */
  function perView() {
    if (window.innerWidth <= 600)  return 1;
    if (window.innerWidth <= 900)  return 2;
    return 3;
  }

  /* Total number of "pages" */
  function totalPages() {
    return total - perView() + 1;
  }

  /* Build dot buttons */
  function buildDots() {
    dotsWrap.innerHTML = '';
    const pages = totalPages();
    for (let i = 0; i < pages; i++) {
      const d = document.createElement('button');
      d.className = 'blog-cdot' + (i === 0 ? ' active' : '');
      d.setAttribute('aria-label', `Go to slide ${i + 1}`);
      d.addEventListener('click', () => goTo(i));
      dotsWrap.appendChild(d);
    }
  }

  function updateDots() {
    const dots = dotsWrap.querySelectorAll('.blog-cdot');
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
  }

  /* Translate track to show card at [current] index */
  function goTo(index) {
    const pages = totalPages();
    current = Math.max(0, Math.min(index, pages - 1));

    /* Calculate translate: move by card width + gap */
    const cardWidth = cards[0].offsetWidth;
    const gap = parseInt(window.getComputedStyle(track).gap) || 24;
    const offset = current * (cardWidth + gap);
    track.style.transform = `translateX(-${offset}px)`;
    track.style.transition = 'transform 0.45s cubic-bezier(0.4,0,0.2,1)';

    updateDots();
    /* Update arrow state */
    if (prevBtn) prevBtn.style.opacity = current === 0 ? '0.4' : '1';
    if (nextBtn) nextBtn.style.opacity = current >= pages - 1 ? '0.4' : '1';
  }

  function next() { goTo(current + 1 >= totalPages() ? 0 : current + 1); }
  function prev() { goTo(current - 1 < 0 ? totalPages() - 1 : current - 1); }

  /* Auto-play */
  function startAuto() {
    clearInterval(autoTimer);
    autoTimer = setInterval(next, 4000);
  }
  function stopAuto() { clearInterval(autoTimer); }

  /* Wire buttons */
  nextBtn?.addEventListener('click', () => { next(); startAuto(); });
  prevBtn?.addEventListener('click', () => { prev(); startAuto(); });

  /* Pause on hover */
  track.addEventListener('mouseenter', stopAuto);
  track.addEventListener('mouseleave', startAuto);
  track.addEventListener('touchstart', stopAuto, { passive: true });
  track.addEventListener('touchend', startAuto, { passive: true });

  /* Re-init on resize */
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      current = 0;
      buildDots();
      goTo(0);
    }, 200);
  });

  /* Init */
  /* Make track not wrap */
  track.style.display = 'flex';
  track.style.flexWrap = 'nowrap';
  track.style.overflow = 'visible';

  buildDots();
  goTo(0);
  startAuto();
}

/* Booking Form Logic */
const GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwVXpjZjVdqZPIvNfpcW06R8WDnGCKLVXvnJy_5BAGO8DehYt836Pt9ZdcZo0_Hf_eRbg/exec";

const appointmentForm = document.getElementById("appointment-form");
const submitBtn = document.getElementById("appt-submit-btn");
const thankYouPopup = document.getElementById("thankYouPopup");
const closePopupBtn = document.getElementById("closePopupBtn");

if (appointmentForm) {
  appointmentForm.addEventListener("submit", function (e) {
      e.preventDefault();

      if (!appointmentForm.checkValidity()) {
        appointmentForm.reportValidity();
        return;
      }

      submitBtn.disabled = true;
      submitBtn.innerHTML = "Submitting...";

      const formData = new FormData(appointmentForm);

      fetch(GOOGLE_SCRIPT_URL, {
          method: "POST",
          body: new URLSearchParams(formData)
      })
      .then(response => response.json())
      .then(data => {
          if (data.result === "success") {
              if (thankYouPopup) {
                thankYouPopup.classList.add('active');
              } else {
                alert("Appointment Booked Successfully!");
              }
              appointmentForm.reset();
          } else {
              alert("Booking Failed!");
              console.log(data);
          }
      })
      .catch(error => {
          console.error(error);
          alert("Something went wrong!");
      })
      .finally(() => {
          submitBtn.disabled = false;
          submitBtn.innerHTML = "Confirm Appointment";
      });
  });

  if (closePopupBtn && thankYouPopup) {
    closePopupBtn.addEventListener('click', () => {
      thankYouPopup.classList.remove('active');
    });
    thankYouPopup.addEventListener('click', (e) => {
      if (e.target === thankYouPopup) {
        thankYouPopup.classList.remove('active');
      }
    });
  }
}
