// Intersection Observer for scroll animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    // Reveal animated cards on scroll
    const animatedCards = document.querySelectorAll('.service-card, .saas-card, .portfolio-item, .feature-card');
    animatedCards.forEach(card => {
        card.classList.add('fade-in-on-scroll');
        observer.observe(card);
    });

    // Mobile Hamburger Menu Toggle
    const hamburger = document.getElementById('hamburger-btn');
    const navLinks = document.getElementById('nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('open');
            navLinks.classList.toggle('active');
            const isExpanded = hamburger.classList.contains('open');
            hamburger.setAttribute('aria-expanded', isExpanded);
        });

        // Close mobile nav when link is clicked
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('open');
                navLinks.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // Fixed Navbar background shadow on scroll
    const navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    console.log('REALTEK ENGINEERING PTE. LTD. Website Initialized');
});
