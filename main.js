import { projectsData, projectCategories } from './src/data/projects.js';

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

// Dynamic Project Portfolio Initialization
function initPortfolio() {
    const portfolioContainer = document.getElementById('portfolio-container');
    if (!portfolioContainer) return;

    // Create Banner & Structure
    const bannerHtml = `
        <div class="portfolio-dev-banner">
            ⚠️ <strong>PORTFOLIO CONTENT UNDER DEVELOPMENT</strong> — Project details and photographs will be updated as confirmed data is supplied.
        </div>
        <div class="portfolio-filter-tabs" id="filter-tabs">
            ${projectCategories.map((cat, idx) => `
                <button class="filter-tab ${idx === 0 ? 'active' : ''}" data-category="${cat.id}">
                    ${cat.label}
                </button>
            `).join('')}
        </div>
        <div class="portfolio-grid" id="projects-grid"></div>
        <div id="project-modal-root"></div>
    `;
    portfolioContainer.innerHTML = bannerHtml;

    const gridEl = document.getElementById('projects-grid');
    const tabsEl = document.getElementById('filter-tabs');

    let currentFilter = 'all';

    function renderProjects(filter) {
        const filtered = filter === 'all' 
            ? projectsData 
            : projectsData.filter(p => p.category === filter);

        gridEl.innerHTML = filtered.map(project => `
            <div class="portfolio-item">
                <div class="portfolio-img-wrapper">
                    <img src="${project.images[0]}" alt="${project.title}">
                    ${project.isDemo 
                        ? `<span class="badge-demo">DEMO / SAMPLE</span>` 
                        : `<span class="badge-genuine">GENUINE PROJECT</span>`
                    }
                </div>
                <div class="portfolio-item-body">
                    <div class="portfolio-label">${project.categoryLabel}</div>
                    <h3>${project.title}</h3>
                    <div class="portfolio-meta">
                        <span>📍 ${project.location}</span>
                        <span>📅 ${project.year}</span>
                    </div>
                    <p class="portfolio-desc">${project.description}</p>
                    <div class="portfolio-item-footer">
                        <button class="btn btn-outline btn-sm view-project-btn" data-id="${project.id}" style="width: 100%;">
                            View Project Details &rarr;
                        </button>
                    </div>
                </div>
            </div>
        `).join('');

        // Attach modal triggers
        gridEl.querySelectorAll('.view-project-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const projId = btn.getAttribute('data-id');
                openProjectModal(projId);
            });
        });
    }

    // Tab Filter Listener
    tabsEl.querySelectorAll('.filter-tab').forEach(tab => {
        tab.addEventListener('click', () => {
            tabsEl.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            currentFilter = tab.getAttribute('data-category');
            renderProjects(currentFilter);
        });
    });

    renderProjects('all');
}

function openProjectModal(id) {
    const project = projectsData.find(p => p.id === id);
    if (!project) return;

    const modalRoot = document.getElementById('project-modal-root');
    const modalHtml = `
        <div class="project-modal-backdrop open" id="modal-backdrop">
            <div class="project-modal">
                <div class="project-modal-header">
                    <img src="${project.images[0]}" alt="${project.title}">
                    <button class="modal-close-btn" id="close-modal-btn" aria-label="Close Modal">&times;</button>
                </div>
                <div class="project-modal-body">
                    <span class="portfolio-label">${project.categoryLabel}</span>
                    <h2>${project.title}</h2>
                    
                    ${project.isDemo ? `
                        <div class="modal-demo-notice">
                            ⚠️ <strong>DEMO / SAMPLE PROJECT:</strong> This layout is provided for visualization. Real project specifications will be updated upon client authorization.
                        </div>
                    ` : `
                        <div style="background: #ECFDF5; border: 1px solid #A7F3D0; color: #065F46; padding: 0.8rem 1.2rem; border-radius: 6px; font-size: 0.88rem; font-weight: 600; margin-bottom: 1.5rem;">
                            ✔ <strong>CONFIRMED REALTEK PROJECT:</strong> ${project.status}.
                        </div>
                    `}

                    <div class="modal-grid-meta">
                        <div class="meta-box"><span>Category</span><strong>${project.categoryLabel}</strong></div>
                        <div class="meta-box"><span>Location</span><strong>${project.location}</strong></div>
                        <div class="meta-box"><span>Year</span><strong>${project.year}</strong></div>
                        <div class="meta-box"><span>Status</span><strong>${project.status}</strong></div>
                    </div>

                    <div class="modal-section-title">Project Overview</div>
                    <p style="color: var(--color-text-secondary); line-height: 1.6;">${project.description}</p>

                    <div class="modal-section-title">Scope of Work</div>
                    <ul class="modal-scope-list">
                        ${project.scope.map(item => `<li>${item}</li>`).join('')}
                    </ul>

                    ${Object.keys(project.specifications).length > 0 ? `
                        <div class="modal-section-title">Specifications & Highlights</div>
                        <div class="modal-grid-meta" style="margin-bottom: 1.5rem;">
                            ${Object.entries(project.specifications).map(([k, v]) => `
                                <div class="meta-box"><span>${k}</span><strong>${v}</strong></div>
                            `).join('')}
                        </div>
                    ` : ''}

                    <div class="modal-section-title">Project Gallery</div>
                    <div class="modal-gallery-grid">
                        ${project.images.map(img => `<img src="${img}" alt="Project Photo">`).join('')}
                    </div>

                    <div style="margin-top: 2rem; text-align: right;">
                        <button class="btn btn-primary" id="close-modal-bottom-btn">Close Details</button>
                    </div>
                </div>
            </div>
        </div>
    `;

    modalRoot.innerHTML = modalHtml;

    function closeModal() {
        const backdrop = document.getElementById('modal-backdrop');
        if (backdrop) {
            backdrop.classList.remove('open');
            setTimeout(() => { modalRoot.innerHTML = ''; }, 250);
        }
    }

    document.getElementById('close-modal-btn')?.addEventListener('click', closeModal);
    document.getElementById('close-modal-bottom-btn')?.addEventListener('click', closeModal);
    document.getElementById('modal-backdrop')?.addEventListener('click', (e) => {
        if (e.target.id === 'modal-backdrop') closeModal();
    });
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Portfolio
    initPortfolio();

    // Reveal animated cards on scroll
    const animatedCards = document.querySelectorAll('.service-card, .saas-card, .feature-card');
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

    console.log('REALTEK ENGINEERING PTE. LTD. Website & Portfolio Initialized');
});
