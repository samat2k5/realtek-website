import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # SECTION 02: Capabilities
    cap_html = """    <section id="engineering" class="c-capabilities tech-section">
        <div class="c-container">
            <div class="tech-intro">
                <span class="c-eyebrow verdigris">02 // CORE DISCIPLINES</span>
                <h2>ENGINEERING CAPABILITIES</h2>
                <div class="tech-rule"></div>
                <p>Integrated expertise. End-to-end execution with engineering precision.</p>
            </div>
            
            <div class="tech-systems">
                <!-- System 01 -->
                <div class="tech-system-row">
                    <div class="ts-media">
                        <img src="/projects/certis-solar.jpg" alt="C&I Solar PV" loading="lazy">
                        <div class="ts-number verdigris">01</div>
                    </div>
                    <div class="ts-specs">
                        <h3>C&I SOLAR PV</h3>
                        <p class="ts-desc">Customised solar PV solutions for commercial and industrial facilities. From feasibility and design to installation and performance optimisation.</p>
                        <ul class="spec-list">
                            <li><span class="spec-lbl">SYSTEM</span> Commercial & Industrial Solar PV</li>
                            <li><span class="spec-lbl">CAPABILITIES</span> Feasibility / Design / Engineering / Installation / Commissioning</li>
                            <li><span class="spec-lbl">APPLICATION</span> Rooftop / Industrial / Commercial</li>
                            <li><span class="spec-lbl">DELIVERY</span> End-to-end execution</li>
                        </ul>
                        <a href="#contact" class="tech-link verdigris-link">LEARN MORE &rarr;</a>
                    </div>
                </div>

                <!-- System 02 -->
                <div class="tech-system-row reverse">
                    <div class="ts-media">
                        <img src="/projects/ei-works.jpg" alt="Electrical & Instrumentation" loading="lazy">
                        <div class="ts-number orange">02</div>
                    </div>
                    <div class="ts-specs">
                        <h3>ELECTRICAL & INSTRUMENTATION (E&I)</h3>
                        <p class="ts-desc">Comprehensive E&I systems for power distribution, instrumentation, control and automation. Built for safety, reliability and operational excellence.</p>
                        <ul class="spec-list">
                            <li><span class="spec-lbl">SCOPE</span> Power Distribution</li>
                            <li><span class="spec-lbl">SYSTEMS</span> Instrumentation / Control / Automation</li>
                            <li><span class="spec-lbl">DELIVERY</span> Installation / Testing / Commissioning</li>
                            <li><span class="spec-lbl">PRIORITIES</span> Safety / Reliability / Operational Performance</li>
                        </ul>
                        <a href="#contact" class="tech-link orange-link">LEARN MORE &rarr;</a>
                    </div>
                </div>

                <!-- System 03 -->
                <div class="tech-system-row">
                    <div class="ts-media">
                        <img src="/projects/hdb-solar.jpg" alt="HDB Solar PV" loading="lazy">
                        <div class="ts-number teal">03</div>
                    </div>
                    <div class="ts-specs">
                        <h3>HDB SOLAR PV</h3>
                        <p class="ts-desc">Delivering sustainable solar solutions for HDB communities. Improving energy efficiency, reducing carbon impact and creating long-term value for residents.</p>
                        <ul class="spec-list">
                            <li><span class="spec-lbl">APPLICATION</span> HDB Communities</li>
                            <li><span class="spec-lbl">SCOPE</span> Solar PV Engineering & Installation</li>
                            <li><span class="spec-lbl">OBJECTIVE</span> Energy Efficiency / Carbon Reduction</li>
                            <li><span class="spec-lbl">DELIVERY</span> Reliable Long-Term Solar Infrastructure</li>
                        </ul>
                        <a href="#contact" class="tech-link teal-link">LEARN MORE &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
    html = re.sub(r'<section id="engineering" class="c-capabilities.*?</section>', cap_html, html, flags=re.DOTALL)

    # SECTION 03: Changi
    changi_html = """    <section class="c-changi tech-section dark">
        <div class="changi-background"></div>
        <div class="c-container changi-grid dossier-layout">
            <div class="changi-main">
                <span class="c-eyebrow teal-light">03 // ENGINEERING PROJECT DOSSIER</span>
                <h2>CHANGI AIRPORT T1 & T2</h2>
                <div class="tech-rule light"></div>
                <p>Powering one of the world's most iconic travel hubs with high-performance solar infrastructure. Engineering excellence at scale. Built for reliability. Designed for the future.</p>
                <a href="/projects/changi-airport/index.html" class="tech-link teal-link">VIEW PROJECT DOSSIER &rarr;</a>
            </div>
            <div class="changi-stats dossier-metrics">
                <div class="dossier-stat">
                    <span class="d-val">4,141.8</span>
                    <span class="d-lbl">kWp CAPACITY</span>
                </div>
                <div class="dossier-stat">
                    <span class="d-val">7,080</span>
                    <span class="d-lbl">PV PANELS INSTALLED</span>
                </div>
            </div>
        </div>
    </section>"""
    html = re.sub(r'<section class="c-changi.*?<\/section>', changi_html, html, count=1, flags=re.DOTALL)

    # SECTION 04: Projects
    projects_html = """    <section id="projects" class="c-projects tech-section">
        <div class="c-container">
            <div class="tech-intro">
                <span class="c-eyebrow orange">04 // PORTFOLIO</span>
                <h2>SELECTED ENGINEERING WORK</h2>
                <div class="tech-rule"></div>
                <p>Real projects. Real impact. Delivering value across industries and sectors.</p>
                <a href="#projects" class="tech-link orange-link">VIEW ALL PROJECTS &rarr;</a>
            </div>
            
            <div class="proj-wall">
                <div class="pw-featured">
                    <img src="/projects/vertical-pv-1.jpg" alt="Vertical PV Façade Installation" loading="lazy">
                    <div class="pw-meta">
                        <span class="pw-number orange">FEAT.</span>
                        <div class="pw-info">
                            <h3>INNOVATIVE VERTICAL PV INTEGRATION</h3>
                            <span class="pw-sys">Vertical PV Façade Installation</span>
                        </div>
                    </div>
                </div>
                
                <div class="pw-secondary">
                    <div class="pw-item">
                        <img src="/projects/geodis-solar.jpg" alt="GEODIS Singapore" loading="lazy">
                        <div class="pw-meta">
                            <span class="pw-number verdigris">01</span>
                            <div class="pw-info">
                                <h3>GEODIS Singapore</h3>
                                <span class="pw-sys">Rooftop Solar PV System</span>
                            </div>
                        </div>
                    </div>
                    <div class="pw-item">
                        <img src="/projects/esr-solar.jpg" alt="ESR REIT Properties" loading="lazy">
                        <div class="pw-meta">
                            <span class="pw-number verdigris">02</span>
                            <div class="pw-info">
                                <h3>ESR REIT Properties</h3>
                                <span class="pw-sys">Rooftop Solar PV System</span>
                            </div>
                        </div>
                    </div>
                    <div class="pw-item">
                        <img src="/projects/ribar-solar.jpg" alt="Ribar Industries" loading="lazy">
                        <div class="pw-meta">
                            <span class="pw-number verdigris">03</span>
                            <div class="pw-info">
                                <h3>Ribar Industries</h3>
                                <span class="pw-sys">Rooftop Solar PV System</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
    html = re.sub(r'<section id="projects".*?</section>', projects_html, html, flags=re.DOTALL)

    # SECTION 05: Ezy SaaS
    ezy_html = """    <section id="digital" class="c-ezy tech-section stone">
        <div class="c-container ezy-systems-layout">
            <div class="ezy-intro">
                <span class="c-eyebrow teal">05 // INTELLIGENCE</span>
                <h2>ezy SaaS</h2>
                <div class="tech-rule"></div>
                <div class="sys-flow">
                    <span>REAL ENGINEERING EXPERIENCE</span>
                    <span class="sys-arrow">&rarr;</span>
                    <span>OPERATIONAL KNOWLEDGE</span>
                    <span class="sys-arrow">&rarr;</span>
                    <span>DIGITAL SOLUTIONS</span>
                    <span class="sys-arrow">&rarr;</span>
                    <span class="sys-highlight">ezy SaaS</span>
                </div>
                <a href="https://ezy.sg/" target="_blank" class="tech-link teal-link">EXPLORE ezy SaaS &rarr;</a>
            </div>
            
            <div class="ezy-platform">
                <div class="ezy-screenshot">
                    <img src="/assets/images/ezyHR.jpeg" alt="ezyHR Interface" loading="lazy" class="master-ui">
                </div>
                <div class="ezy-modules">
                    <div class="sys-module active">
                        <span class="mod-cat">PEOPLE</span>
                        <h4>ezyHR <span class="status-tag active">ACTIVE</span></h4>
                    </div>
                    <div class="sys-module">
                        <span class="mod-cat">OPERATIONS</span>
                        <h4>ezyBooks <span class="status-tag">COMING SOON</span></h4>
                    </div>
                    <div class="sys-module">
                        <span class="mod-cat">CUSTOMERS</span>
                        <h4>ezyCRM <span class="status-tag">COMING SOON</span></h4>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
    html = re.sub(r'<section id="digital".*?</section>', ezy_html, html, flags=re.DOTALL)

    # SECTION 06: Contact
    contact_html = """    <section id="contact" class="c-contact tech-section">
        <div class="c-container contact-brief">
            <div class="contact-info">
                <span class="c-eyebrow orange">06 // INITIATE</span>
                <h2>LET'S ENGINEER<br>WHAT'S NEXT.</h2>
                <div class="tech-rule"></div>
                <p>Tell us about your project or challenge. Our team will respond with the right engineering solution.</p>
                
                <div class="brief-data">
                    <div class="bd-item">
                        <span class="bd-lbl">WHATSAPP</span>
                        <a href="https://wa.me/6590291433" class="bd-val">+65 9029 1433</a>
                    </div>
                    <div class="bd-item">
                        <span class="bd-lbl">HQ</span>
                        <span class="bd-val">132 Gul Circle<br>Singapore 629597</span>
                    </div>
                </div>
            </div>
            
            <div class="contact-form">
                <div class="form-header">
                    <h3>ENGINEERING PROJECT BRIEF</h3>
                    <p>Request a Quote</p>
                </div>
                <form action="#" method="POST" class="tech-form">
                    <div class="form-row">
                        <div class="form-group">
                            <label>Full Name</label>
                            <input type="text" name="name" required>
                        </div>
                        <div class="form-group">
                            <label>Company</label>
                            <input type="text" name="company" required>
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="form-group">
                            <label>Email</label>
                            <input type="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label>Contact Number</label>
                            <input type="tel" name="phone" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label>Service/Project Type</label>
                        <select name="service" required>
                            <option value="">Select an engineering discipline</option>
                            <option value="ci">C&I Solar PV</option>
                            <option value="ei">Electrical & Instrumentation (E&I)</option>
                            <option value="hdb">HDB Solar PV</option>
                            <option value="saas">ezy SaaS</option>
                            <option value="other">Other Inquiry</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>Message</label>
                        <textarea name="message" rows="4" required></textarea>
                    </div>
                    <div class="form-actions">
                        <button type="button" class="tech-btn outline-btn">CHAT ON WHATSAPP</button>
                        <button type="submit" class="tech-btn solid-btn">SUBMIT REQUEST</button>
                    </div>
                </form>
            </div>
        </div>
    </section>"""
    html = re.sub(r'<section id="contact".*?</section>', contact_html, html, flags=re.DOTALL)

    # Footer
    footer_bottom_html = """        <div class="footer-bottom">
            <div class="c-container">
                <div class="footer-statement">
                    <span>ENGINEERING TODAY.</span>
                    <span class="fs-orange">INTELLIGENCE FOR TOMORROW.</span>
                </div>
                <p>&copy; 2024 Realtek Engineering Pte. Ltd. All rights reserved.</p>
            </div>
        </div>"""
    html = re.sub(r'<div class="footer-bottom">.*?</div\s*>\s*</div\s*>', footer_bottom_html, html, flags=re.DOTALL)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)


def update_css():
    css_architectural = """
/* =========================================================
   POST-HERO ARCHITECTURAL DESIGN REFINEMENT
   ========================================================= */

/* Common Technical Components */
.tech-section { padding: 8rem 0; background: #ffffff; }
.tech-section.dark { background: #0B1F33; color: #fff; }
.tech-section.stone { background: #F7F3EA; }

.tech-rule { height: 1px; background: rgba(0,0,0,0.1); width: 100%; margin: 2rem 0; }
.tech-rule.light { background: rgba(255,255,255,0.1); }

.tech-link {
    display: inline-block;
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.1em;
    text-decoration: none;
    text-transform: uppercase;
    transition: opacity 0.3s ease;
    margin-top: 1rem;
}
.tech-link:hover { opacity: 0.7; }

/* 02. Engineering Systems (Capabilities) */
.tech-intro { margin-bottom: 4rem; max-width: 800px; }
.tech-intro h2 { font-size: 3rem; margin: 1rem 0 0 0; line-height: 1.1; }

.tech-systems { display: flex; flex-direction: column; gap: 6rem; }
.tech-system-row { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
.tech-system-row.reverse .ts-media { order: 2; }
.tech-system-row.reverse .ts-specs { order: 1; }

.ts-media { position: relative; }
.ts-media img { width: 100%; aspect-ratio: 16/9; object-fit: cover; }
.ts-number {
    position: absolute;
    top: -2rem;
    left: -2rem;
    font-size: 6rem;
    font-weight: 900;
    line-height: 1;
    font-family: 'Space Grotesk', sans-serif;
    opacity: 0.9;
}
.ts-number.verdigris { color: var(--clr-verdigris); }
.ts-number.orange { color: var(--clr-orange); }
.ts-number.teal { color: var(--clr-teal); }

.ts-specs h3 { font-size: 2rem; margin-bottom: 1rem; }
.ts-desc { font-size: 1.1rem; color: #4A5568; margin-bottom: 2.5rem; line-height: 1.6; }

.spec-list { list-style: none; padding: 0; margin: 0 0 2rem 0; border-top: 1px solid rgba(0,0,0,0.1); }
.spec-list li {
    padding: 1rem 0;
    border-bottom: 1px solid rgba(0,0,0,0.1);
    display: flex;
    font-size: 0.95rem;
    color: #2D3748;
}
.spec-lbl { width: 140px; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.05em; color: #718096; flex-shrink: 0; }

/* 03. Changi Dossier */
.dossier-layout { display: grid; grid-template-columns: 1.5fr 1fr; gap: 6rem; align-items: end; }
.changi-main p { font-size: 1.1rem; color: rgba(255,255,255,0.8); margin-bottom: 2rem; max-width: 600px; }
.dossier-metrics { display: flex; flex-direction: column; gap: 3rem; border-left: 1px solid rgba(255,255,255,0.2); padding-left: 3rem; }
.dossier-stat { display: flex; flex-direction: column; }
.d-val { font-size: 4rem; font-weight: 300; line-height: 1; margin-bottom: 0.5rem; color: var(--clr-teal-light); }
.d-lbl { font-size: 0.85rem; font-weight: 700; letter-spacing: 0.1em; color: rgba(255,255,255,0.6); }

/* 04. Selected Engineering Work (Wall) */
.proj-wall { display: grid; grid-template-columns: 1.2fr 1fr; gap: 4rem; }
.pw-featured img { width: 100%; aspect-ratio: 4/5; object-fit: cover; }
.pw-meta { display: flex; gap: 1.5rem; margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(0,0,0,0.1); }
.pw-number { font-size: 1.5rem; font-weight: 800; }
.pw-number.orange { color: var(--clr-orange); }
.pw-number.verdigris { color: var(--clr-verdigris); }
.pw-info h3 { font-size: 1.5rem; margin-bottom: 0.25rem; }
.pw-featured .pw-info h3 { font-size: 2.2rem; margin-bottom: 0.5rem; }
.pw-sys { font-size: 0.95rem; color: #718096; font-weight: 500; }

.pw-secondary { display: flex; flex-direction: column; gap: 4rem; }
.pw-item img { width: 100%; aspect-ratio: 16/9; object-fit: cover; }

/* 05. Ezy SaaS */
.ezy-systems-layout { display: flex; flex-direction: column; gap: 5rem; }
.sys-flow { display: flex; flex-wrap: wrap; gap: 1rem; align-items: center; font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 2rem; color: #4A5568; }
.sys-arrow { color: var(--clr-teal); }
.sys-highlight { color: var(--clr-verdigris); font-size: 1rem; }

.ezy-platform { display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: center; }
.master-ui { width: 100%; box-shadow: 0 10px 40px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); }

.ezy-modules { display: flex; flex-direction: column; gap: 2rem; border-left: 1px solid rgba(0,0,0,0.1); padding-left: 3rem; }
.sys-module { display: flex; flex-direction: column; gap: 0.5rem; }
.sys-module:not(.active) { opacity: 0.5; }
.mod-cat { font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em; color: #718096; }
.sys-module h4 { font-size: 1.5rem; display: flex; align-items: center; gap: 1rem; margin: 0; }
.status-tag { font-size: 0.7rem; padding: 0.2rem 0.5rem; background: #E2E8F0; color: #4A5568; font-weight: 800; border-radius: 2px; }
.status-tag.active { background: var(--clr-verdigris); color: #fff; }

/* 06. Contact */
.contact-brief { display: grid; grid-template-columns: 1fr 1fr; gap: 6rem; align-items: flex-start; }
.brief-data { margin-top: 4rem; display: flex; flex-direction: column; gap: 2rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 2rem; }
.bd-item { display: flex; flex-direction: column; gap: 0.5rem; }
.bd-lbl { font-size: 0.8rem; font-weight: 800; letter-spacing: 0.1em; color: var(--clr-orange); }
.bd-val { font-size: 1.25rem; font-weight: 500; color: #2D3748; text-decoration: none; }

.contact-form { background: #F7F3EA; padding: 4rem; }
.form-header { margin-bottom: 3rem; border-bottom: 1px solid rgba(0,0,0,0.1); padding-bottom: 2rem; }
.form-header h3 { font-size: 1.5rem; margin-bottom: 0.5rem; }
.form-header p { color: #718096; margin: 0; }

.tech-form { display: flex; flex-direction: column; gap: 1.5rem; }
.tech-form label { font-size: 0.85rem; font-weight: 700; letter-spacing: 0.05em; color: #4A5568; margin-bottom: 0.5rem; display: block; }
.tech-form input, .tech-form select, .tech-form textarea { width: 100%; padding: 1rem; border: 1px solid rgba(0,0,0,0.15); background: #fff; font-family: inherit; font-size: 1rem; border-radius: 0; }
.form-actions { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem; }
.tech-btn { padding: 1.25rem; font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em; border: none; cursor: pointer; text-align: center; transition: all 0.3s ease; }
.outline-btn { background: transparent; border: 2px solid var(--clr-verdigris); color: var(--clr-verdigris); }
.outline-btn:hover { background: var(--clr-verdigris); color: #fff; }
.solid-btn { background: var(--clr-orange); color: #fff; }
.solid-btn:hover { background: #d0531c; }

/* Footer */
.footer-statement { display: flex; flex-direction: column; font-size: 2rem; font-weight: 800; line-height: 1.1; margin-bottom: 2rem; letter-spacing: -0.02em; }
.fs-orange { color: var(--clr-orange); }

/* Responsive Adjustments */
@media (max-width: 1200px) {
    .tech-system-row { gap: 2rem; }
    .ts-number { top: -1rem; left: -1rem; font-size: 4rem; }
    .dossier-layout { grid-template-columns: 1fr; gap: 3rem; }
    .dossier-metrics { flex-direction: row; border-left: none; padding-left: 0; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 3rem; }
    .proj-wall { grid-template-columns: 1fr; gap: 4rem; }
    .ezy-platform { grid-template-columns: 1fr; gap: 3rem; }
    .ezy-modules { border-left: none; padding-left: 0; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 3rem; flex-direction: row; flex-wrap: wrap; }
    .contact-brief { grid-template-columns: 1fr; gap: 4rem; }
}

@media (max-width: 768px) {
    .tech-section { padding: 4rem 0; }
    .tech-system-row { grid-template-columns: 1fr; }
    .tech-system-row.reverse .ts-media { order: 1; }
    .tech-system-row.reverse .ts-specs { order: 2; }
    .tech-intro h2 { font-size: 2.2rem; }
    .ts-specs h3 { font-size: 1.5rem; }
    
    .dossier-metrics { grid-template-columns: 1fr 1fr; display: grid; }
    .d-val { font-size: 2.5rem; }
    
    .sys-flow { flex-direction: column; align-items: flex-start; gap: 0.5rem; }
    .sys-arrow { display: none; }
    
    .contact-form { padding: 2rem; }
    .form-row { grid-template-columns: 1fr; }
    .form-actions { grid-template-columns: 1fr; }
    
    .footer-statement { font-size: 1.5rem; }
}
"""

    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(css_architectural)

update_html()
update_css()
