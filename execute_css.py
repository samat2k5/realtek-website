import os

css_mockup = """
/* ================================================== */
/* MOCKUP IMPLEMENTATION (R1.3)                      */
/* ================================================== */

.m-eyebrow {
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.1em;
    display: block;
    margin-bottom: 0.5rem;
}
.m-eyebrow.orange { color: var(--color-copper); }
.m-eyebrow.teal { color: var(--color-teal); }
.m-eyebrow.teal-light { color: #38B2AC; }

.m-rule { background: var(--color-copper); height: 2px; width: 40px; margin: 1.5rem 0; }
.m-link { font-size: 0.9rem; font-weight: 800; letter-spacing: 0.05em; text-decoration: none; display: inline-block; }
.m-link.orange-link { color: var(--color-copper); }
.m-link.teal-link { color: var(--color-teal); }
.mt-auto { margin-top: auto; }
.mt-2 { margin-top: 2rem; }
.m-btn { font-size: 0.9rem; font-weight: 800; letter-spacing: 0.05em; padding: 1rem 2rem; border: none; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; }
.m-btn-orange { background: var(--color-copper); color: #fff; }
.m-btn-teal { background: var(--color-teal); color: #fff; }

/* 1. ENGINEERING CAPABILITIES */
.m-capabilities { background: #fdfdfd; padding: 6rem 0; }
.m-cap-grid { display: grid; grid-template-columns: 25% 75%; gap: 3rem; align-items: start; }
.m-cap-intro h2 { font-size: 2.5rem; line-height: 1.1; color: var(--color-space); margin: 0; }
.m-cap-intro p { font-size: 1.1rem; color: #4a5568; margin-bottom: 2rem; }

.m-cap-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.m-card { display: flex; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.08); overflow: hidden; height: 100%; min-height: 480px; }
.m-card-left { width: 50%; position: relative; }
.m-card-left img { width: 100%; height: 100%; object-fit: cover; }
.m-card-num { position: absolute; top: 0; right: 0; padding: 0.8rem; font-family: 'Space Grotesk', sans-serif; font-weight: 800; font-size: 1.2rem; color: #fff; }
.m-card-num.teal { background: var(--color-teal); }
.m-card-num.orange { background: var(--color-copper); }

.m-card-right { width: 50%; padding: 2rem 1.5rem; display: flex; flex-direction: column; }
.m-card-icon { align-self: flex-end; margin-bottom: 1.5rem; }
.m-card-icon.teal-icon { color: var(--color-teal); }
.m-card-icon.orange-icon { color: var(--color-copper); }
.m-card-right h3 { font-size: 1.25rem; font-weight: 800; line-height: 1.2; margin-bottom: 1rem; color: var(--color-space); }
.m-card-right p { font-size: 0.85rem; line-height: 1.5; color: #4a5568; margin-bottom: 1.5rem; }

/* 2. CHANGI */
.m-changi { position: relative; padding: 6rem 0; color: #fff; }
.m-changi-bg { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: url('/assets/images/hero/changi-flagship.jpg') center/cover; z-index: 1; }
.m-changi-bg::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(90deg, rgba(10,25,47,0.95) 0%, rgba(10,25,47,0.8) 40%, rgba(10,25,47,0.4) 100%); }
.m-changi-grid { position: relative; z-index: 2; display: grid; grid-template-columns: 45% 55%; gap: 4rem; align-items: center; }
.m-changi-left h2 { font-size: 3rem; margin: 0 0 1.5rem 0; }
.m-changi-left p { font-size: 1.1rem; opacity: 0.9; margin-bottom: 2rem; }
.m-changi-right { display: flex; gap: 3rem; align-items: center; }
.m-changi-stat { display: flex; align-items: center; gap: 1rem; }
.m-changi-stat svg { color: var(--color-copper); }
.m-stat-content { display: flex; flex-direction: column; }
.m-stat-val { font-size: 2.5rem; font-weight: 300; line-height: 1; margin-bottom: 0.25rem; }
.m-stat-lbl { font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; opacity: 0.8; }
.m-changi-built { padding-left: 2rem; border-left: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; }

/* 3. PROJECTS */
.m-projects { background: #f5f2ed; padding: 6rem 0; position: relative; overflow: hidden; }
/* Simulated curved wavy background */
.m-projects::before {
    content: ''; position: absolute; top: -50px; left: -10%; width: 60%; height: 120%;
    background: #e8e4db; border-radius: 50%; opacity: 0.5; z-index: 0;
}
.m-proj-grid { position: relative; z-index: 1; display: grid; grid-template-columns: 25% 75%; gap: 3rem; align-items: start; }
.m-proj-left h2 { font-size: 2.5rem; color: var(--color-space); margin: 0 0 1rem 0; }
.m-proj-left p { font-size: 1.1rem; color: #4a5568; }

.m-proj-right { display: grid; grid-template-columns: 1fr 1.5fr; gap: 1rem; }
.m-proj-feat { position: relative; height: 100%; min-height: 500px; overflow: hidden; }
.m-proj-feat img { width: 100%; height: 100%; object-fit: cover; }
.m-proj-overlay { position: absolute; bottom: 0; left: 0; width: 100%; padding: 2rem; background: linear-gradient(0deg, rgba(0,0,0,0.8) 0%, transparent 100%); color: #fff; }
.m-proj-tag { display: inline-block; background: var(--color-teal); color: #fff; font-size: 0.7rem; font-weight: 800; padding: 0.3rem 0.6rem; margin-bottom: 0.8rem; }
.m-proj-overlay h4 { font-size: 1.25rem; margin: 0; }
.m-proj-sub { font-size: 0.9rem; font-weight: 400; opacity: 0.8; }

.m-proj-grid-2x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.m-proj-item { position: relative; height: 245px; overflow: hidden; }
.m-proj-item img { width: 100%; height: 100%; object-fit: cover; }

/* 4. EZY SAAS */
.m-saas { background: #fff; padding: 6rem 0; }
.m-saas-grid { display: grid; grid-template-columns: 25% 45% 25%; gap: 2.5rem; align-items: center; }
.m-saas-left p { font-size: 1.1rem; color: #4a5568; }
.m-device-wrapper { position: relative; width: 100%; max-width: 600px; margin: 0 auto; }
.m-desktop-frame { background: #f0f0f0; border-radius: 8px; padding: 2rem 0.5rem 0.5rem; position: relative; box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.m-browser-bar { position: absolute; top: 0; left: 0; width: 100%; height: 2rem; display: flex; align-items: center; padding: 0 1rem; gap: 6px; }
.m-browser-bar span { width: 10px; height: 10px; border-radius: 50%; background: #ccc; }
.m-browser-bar span:nth-child(1) { background: #ff5f56; }
.m-browser-bar span:nth-child(2) { background: #ffbd2e; }
.m-browser-bar span:nth-child(3) { background: #27c93f; }
.m-desktop-frame img { width: 100%; border-radius: 4px; display: block; }
.m-mobile-frame { position: absolute; bottom: -20px; right: -20px; width: 30%; background: #fff; border-radius: 12px; padding: 6px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
.m-mobile-frame img { width: 100%; border-radius: 6px; display: block; }

.m-saas-right { display: flex; flex-direction: column; gap: 2rem; }
.m-saas-feat { display: flex; gap: 1rem; align-items: flex-start; }
.m-s-icon { color: var(--color-teal); flex-shrink: 0; }
.m-s-text h4 { font-size: 1.1rem; color: var(--color-space); margin: 0 0 0.5rem 0; }
.m-s-text p { font-size: 0.9rem; color: #4a5568; margin: 0; }

/* 5. CONTACT */
.m-contact { background: #fdfcf9; padding: 6rem 0; }
.m-contact-grid { display: grid; grid-template-columns: 25% 45% 25%; gap: 2.5rem; align-items: start; }
.m-contact-left h2 { font-size: 2.5rem; line-height: 1.1; color: var(--color-space); margin: 0 0 1rem 0; }
.m-contact-info { display: flex; flex-direction: column; gap: 1.5rem; }
.m-ci-item { display: flex; gap: 1rem; align-items: flex-start; font-size: 0.95rem; font-weight: 600; color: var(--color-space); }

.m-contact-mid form { display: flex; flex-direction: column; gap: 1.5rem; }
.m-f-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
.m-f-group { display: flex; flex-direction: column; gap: 0.5rem; }
.m-f-group label { font-size: 0.8rem; font-weight: 800; color: var(--color-space); letter-spacing: 0.05em; }
.m-f-group .req { color: #e53e3e; }
.m-f-group input, .m-f-group select, .m-f-group textarea { padding: 0.8rem 1rem; border: 1px solid #e2e8f0; border-radius: 2px; font-family: inherit; font-size: 0.95rem; outline: none; transition: border-color 0.2s; background: #fff; }
.m-f-group input:focus, .m-f-group select:focus, .m-f-group textarea:focus { border-color: var(--color-copper); }

.m-f-actions { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.5rem; }
.m-btn-wa { background: var(--color-teal); color: #fff; border: 1px solid var(--color-teal); display: flex; justify-content: center; }

.m-contact-right { display: flex; flex-direction: column; gap: 1rem; padding-top: 2rem; }
.m-btn-auth { display: flex; align-items: center; justify-content: center; gap: 0.75rem; padding: 0.8rem; background: #fff; border: 1px solid #e2e8f0; border-radius: 4px; font-size: 0.95rem; font-weight: 600; cursor: pointer; transition: background 0.2s; color: var(--color-space); }
.m-btn-auth:hover { background: #f7fafc; }
.m-auth-desc { font-size: 0.85rem; color: #718096; text-align: center; margin-top: 0.5rem; }
.m-f-secure { display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: #718096; }

/* FOOTER */
.m-footer { background: var(--color-space); color: #fff; padding: 4rem 0 2rem; }
.m-footer-grid { display: grid; grid-template-columns: 1.5fr repeat(5, 1fr); gap: 2rem; }
.m-f-brand .c-logo img { filter: brightness(0) invert(1); width: 140px; margin-bottom: 1.5rem; }
.m-f-desc { font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-bottom: 1rem; line-height: 1.5; }
.m-f-col h4 { font-size: 0.85rem; font-weight: 800; letter-spacing: 0.1em; color: #fff; margin-bottom: 1.5rem; }
.m-f-col a { display: block; color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.9rem; margin-bottom: 0.8rem; transition: color 0.2s; }
.m-f-col a:hover { color: #fff; }
.m-f-social { display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 4px; background: rgba(255,255,255,0.1); color: #fff; }
.m-f-social:hover { background: var(--color-teal); }

/* MOBILE RESPONSIVE */
@media (max-width: 1024px) {
    .m-cap-grid, .m-changi-grid, .m-proj-grid, .m-saas-grid, .m-contact-grid, .m-footer-grid { grid-template-columns: 1fr; gap: 2rem; }
    .m-cap-cards { grid-template-columns: 1fr; }
    .m-card { min-height: auto; flex-direction: column; }
    .m-card-left, .m-card-right { width: 100%; }
    .m-card-left img { height: 250px; }
    .m-proj-right { grid-template-columns: 1fr; }
    .m-proj-feat { min-height: 300px; }
    .m-changi-right { flex-direction: column; align-items: flex-start; gap: 1.5rem; }
    .m-changi-built { padding-left: 0; border-left: none; }
    .m-f-row, .m-f-actions { grid-template-columns: 1fr; }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_mockup)
