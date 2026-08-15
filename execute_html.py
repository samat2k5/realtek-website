import os
import shutil
import re

# Backup
shutil.copy('index.html', 'index.backup.r2.html')
shutil.copy('style.css', 'style.backup.r2.css')

html_mockup = """
    <!-- ================================================== -->
    <!-- MOCKUP IMPLEMENTATION (BELOW HERO)                 -->
    <!-- ================================================== -->
    
    <section id="engineering" class="m-capabilities">
        <div class="c-container m-cap-grid">
            <div class="m-cap-intro">
                <span class="m-eyebrow orange">OUR STRENGTH</span>
                <h2>ENGINEERING CAPABILITIES</h2>
                <div class="m-rule"></div>
                <p>Three core disciplines. Integrated expertise. End-to-end execution with engineering precision.</p>
                <a href="#contact" class="m-link orange-link">OUR APPROACH &rarr;</a>
            </div>
            
            <div class="m-cap-cards">
                <!-- Card 1 -->
                <div class="m-card">
                    <div class="m-card-left">
                        <img src="/projects/certis-solar.jpg" alt="C&I Solar PV">
                        <div class="m-card-num teal">01</div>
                    </div>
                    <div class="m-card-right">
                        <div class="m-card-icon teal-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
                        </div>
                        <h3>C&I<br>SOLAR PV</h3>
                        <p>Customised solar PV solutions for commercial and industrial facilities. From feasibility and design to installation and performance optimisation.</p>
                        <a href="#contact" class="m-link teal-link mt-auto">LEARN MORE &rarr;</a>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="m-card">
                    <div class="m-card-left">
                        <img src="/projects/ei-works.jpg" alt="E&I">
                        <div class="m-card-num orange">02</div>
                    </div>
                    <div class="m-card-right">
                        <div class="m-card-icon orange-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
                        </div>
                        <h3>ELECTRICAL &<br>INSTRUMENTATION<br>(E&I)</h3>
                        <p>Comprehensive E&I systems for power distribution, instrumentation, control and automation. Built for safety, reliability and operational excellence.</p>
                        <a href="#contact" class="m-link orange-link mt-auto">LEARN MORE &rarr;</a>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="m-card">
                    <div class="m-card-left">
                        <img src="/projects/hdb-solar.jpg" alt="HDB Solar PV">
                        <div class="m-card-num teal">03</div>
                    </div>
                    <div class="m-card-right">
                        <div class="m-card-icon teal-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                        </div>
                        <h3>HDB<br>SOLAR PV</h3>
                        <p>Delivering sustainable solar solutions for HDB communities. Improving energy efficiency, reducing carbon impact and creating long-term value for residents.</p>
                        <a href="#contact" class="m-link teal-link mt-auto">LEARN MORE &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="m-changi">
        <div class="m-changi-bg"></div>
        <div class="c-container m-changi-grid">
            <div class="m-changi-left">
                <span class="m-eyebrow teal-light">SIGNATURE PROJECT</span>
                <h2>CHANGI AIRPORT<br>T1 & T2</h2>
                <p>Powering one of the world's most iconic travel hubs with high-performance solar infrastructure. Engineering excellence at scale. Built for reliability. Designed for the future.</p>
                <a href="/projects/changi-airport/index.html" class="m-btn m-btn-orange mt-2">VIEW PROJECT DETAILS &rarr;</a>
            </div>
            <div class="m-changi-right">
                <div class="m-changi-stat">
                    <svg class="orange" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                    <div class="m-stat-content">
                        <span class="m-stat-val">4,141.8</span>
                        <span class="m-stat-lbl">kWp CAPACITY</span>
                    </div>
                </div>
                <div class="m-changi-stat">
                    <svg class="orange" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
                    <div class="m-stat-content">
                        <span class="m-stat-val">7,080</span>
                        <span class="m-stat-lbl">PV PANELS INSTALLED</span>
                    </div>
                </div>
                <div class="m-changi-built">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:0.5rem"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    <span class="m-stat-lbl">BUILT FOR<br>RELIABILITY</span>
                </div>
            </div>
        </div>
    </section>

    <section id="projects" class="m-projects">
        <div class="c-container m-proj-grid">
            <div class="m-proj-left">
                <span class="m-eyebrow orange">PROVEN PERFORMANCE</span>
                <h2>SELECTED<br>ENGINEERING WORK</h2>
                <p>Real projects. Real impact. Delivering value across industries and sectors.</p>
                <a href="#projects" class="m-link orange-link mt-2">VIEW ALL PROJECTS &rarr;</a>
            </div>
            <div class="m-proj-right">
                <div class="m-proj-feat">
                    <img src="/projects/vertical-pv-1.jpg" alt="Innovative Vertical PV">
                    <div class="m-proj-overlay">
                        <span class="m-proj-tag">FEATURED PROJECT</span>
                        <h4>INNOVATIVE VERTICAL PV<br><span class="m-proj-sub">Solar PV Integration</span></h4>
                    </div>
                </div>
                <div class="m-proj-grid-2x2">
                    <div class="m-proj-item">
                        <img src="/projects/esr-solar.jpg" alt="ESR REIT Properties">
                        <div class="m-proj-overlay"><h4>ESR REIT Properties<br><span class="m-proj-sub">Rooftop Solar PV System</span></h4></div>
                    </div>
                    <div class="m-proj-item">
                        <img src="/projects/ribar-solar.jpg" alt="Ribar Industries">
                        <div class="m-proj-overlay"><h4>Ribar Industries<br><span class="m-proj-sub">Rooftop Solar PV System</span></h4></div>
                    </div>
                    <div class="m-proj-item">
                        <img src="/projects/fugro-solar.jpg" alt="Fugro Singapore">
                        <div class="m-proj-overlay"><h4>Fugro Singapore<br><span class="m-proj-sub">Rooftop Solar PV System</span></h4></div>
                    </div>
                    <div class="m-proj-item">
                        <img src="/projects/geodis-solar.jpg" alt="GEODIS Singapore">
                        <div class="m-proj-overlay"><h4>GEODIS Singapore<br><span class="m-proj-sub">Rooftop Solar PV System</span></h4></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="ezy-saas" class="m-saas">
        <div class="c-container m-saas-grid">
            <div class="m-saas-left">
                <span class="m-eyebrow teal">FROM ENGINEERING TO INTELLIGENCE</span>
                <h2 style="font-size: 3.5rem; color: var(--color-teal); margin-bottom: 1rem;">ezy SaaS</h2>
                <p>Digital solutions that transform the way businesses manage people, operations and compliance.</p>
                <a href="#contact" class="m-btn m-btn-teal mt-2">Explore ezy SaaS &rarr;</a>
            </div>
            <div class="m-saas-center">
                <div class="m-device-wrapper">
                    <div class="m-desktop-frame">
                        <div class="m-browser-bar"><span></span><span></span><span></span></div>
                        <img src="/assets/images/ezy-saas/ezyHR.jpeg" alt="ezyHR Desktop">
                    </div>
                    <div class="m-mobile-frame">
                        <img src="/assets/images/ezy-saas/ezyHR_mobile1.jpeg" alt="ezyHR Mobile">
                    </div>
                </div>
            </div>
            <div class="m-saas-right">
                <div class="m-saas-feat">
                    <div class="m-s-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                    <div class="m-s-text">
                        <h4>ezyHR</h4>
                        <p>Comprehensive HR management from hire to retire.</p>
                    </div>
                </div>
                <div class="m-saas-feat">
                    <div class="m-s-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg></div>
                    <div class="m-s-text">
                        <h4>ezyBooks</h4>
                        <p>Accounting & Finance made simple and accurate.</p>
                    </div>
                </div>
                <div class="m-saas-feat">
                    <div class="m-s-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg></div>
                    <div class="m-s-text">
                        <h4>ezyCRM</h4>
                        <p>Manage customer relationships and business growth.</p>
                    </div>
                </div>
                <a href="#contact" class="m-link teal-link mt-2">Explore ezy SaaS &rarr;</a>
            </div>
        </div>
    </section>

    <section id="contact" class="m-contact">
        <div class="c-container m-contact-grid">
            <div class="m-contact-left">
                <span class="m-eyebrow orange">CONNECT WITH REALTEK</span>
                <h2>LET'S ENGINEER<br>WHAT'S NEXT.</h2>
                <p style="margin-bottom:2rem;">Tell us about your project or challenge. Our team will respond with the right engineering solution.</p>
                
                <div class="m-contact-info">
                    <div class="m-ci-item">
                        <svg class="orange" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        <span>+65 9029 1433</span>
                    </div>
                    <div class="m-ci-item">
                        <svg class="orange" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        <span>enquiry@realtekengg.com</span>
                    </div>
                    <div class="m-ci-item">
                        <svg class="orange" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        <span>18 Boon Lay Way #09-142<br>TradeHub 21, Singapore 609966</span>
                    </div>
                </div>
            </div>
            
            <div class="m-contact-mid">
                <form id="m-contact-form" onsubmit="event.preventDefault(); alert('Request Submitted!');">
                    <div class="m-f-row">
                        <div class="m-f-group"><label>Full Name <span class="req">*</span></label><input type="text" required></div>
                        <div class="m-f-group"><label>Company Name <span class="req">*</span></label><input type="text" required></div>
                    </div>
                    <div class="m-f-row">
                        <div class="m-f-group"><label>Email Address <span class="req">*</span></label><input type="email" required></div>
                        <div class="m-f-group"><label>Contact Number <span class="req">*</span></label><input type="tel" required></div>
                    </div>
                    <div class="m-f-group">
                        <label>Project Type / Service <span class="req">*</span></label>
                        <select required>
                            <option value="">Please select</option>
                            <option value="ci">C&I Solar PV</option>
                            <option value="ei">Electrical & Instrumentation</option>
                            <option value="hdb">HDB Solar PV</option>
                            <option value="saas">ezy SaaS</option>
                        </select>
                    </div>
                    <div class="m-f-group">
                        <label>Tell us about your project or requirements <span class="req">*</span></label>
                        <textarea rows="4" required placeholder="Your message..."></textarea>
                    </div>
                    <div class="m-f-actions">
                        <a href="https://wa.me/6590291433" target="_blank" class="m-btn m-btn-teal m-btn-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 2C6.494 2 2 6.493 2 12.03c0 1.77.464 3.498 1.344 5.02L2 22l5.086-1.332A9.975 9.975 0 0012.031 22c5.538 0 10.033-4.494 10.033-10.031S17.568 2 12.031 2zM12.031 20.32c-1.503 0-2.973-.404-4.26-1.168l-.306-.181-3.167.83 .842-3.086-.198-.316a8.315 8.315 0 01-1.272-4.43c0-4.606 3.748-8.354 8.355-8.354 4.608 0 8.356 3.748 8.356 8.354 0 4.607-3.748 8.356-8.356 8.356zm4.582-6.257c-.25-.125-1.486-.734-1.716-.818-.23-.083-.398-.125-.565.125-.168.25-.65 .818-.797.985-.148.167-.296.187-.547.062-1.07-.502-2.128-1.196-3.013-2.037-.624-.593-1.05-1.314-1.258-1.65-.041-.07-.061-.144-.061-.22 0-.214.124-.368.232-.497.108-.128.25-.333.375-.5.068-.09.112-.178.167-.291.104-.216.052-.405-.011-.53-.062-.125-.565-1.363-.774-1.867-.203-.49-.41-.424-.565-.432h-.481c-.167 0-.44.063-.67.313-.23.25-.88 .86-.88 2.096 0 1.237.902 2.434 1.027 2.602.126.167 1.776 2.71 4.3 3.8.599.258 1.066.413 1.432.528.602.191 1.15.164 1.58.1.48-.073 1.486-.607 1.696-1.194.21-.588.21-1.092.147-1.194-.062-.104-.23-.167-.481-.291z"/></svg>
                            CHAT ON WHATSAPP
                        </a>
                        <button type="submit" class="m-btn m-btn-orange">SUBMIT REQUEST &rarr;</button>
                    </div>
                </form>
            </div>
            
            <div class="m-contact-right">
                <button type="button" class="m-btn-auth">
                    <svg width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="currentColor" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="currentColor" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="currentColor" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>
                    Sign in with Google
                </button>
                <button type="button" class="m-btn-auth">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.05 20.28c-.98.68-2.05.8-3.08.8-1.09 0-2.09-.34-2.97-.81-1.03-.55-1.92-.81-3.08-.81-1.12 0-2.08.28-3.13.82-.9.48-1.92.83-3.04.83-1.16 0-2.26-.35-3.23-1.01-4.22-2.88-5.34-8.09-3.06-11.45C3.31 6.32 5.08 5.39 6.84 5.39c1.17 0 2.24.41 3.12.92.93.53 1.54.91 2.92.91 1.34 0 2.04-.38 2.93-.9 1.02-.59 2.13-1 3.32-1 1.72 0 3.39.95 4.39 2.45-3.41 1.95-2.81 7 1.04 8.51H24c-.81 1.48-1.89 2.87-3.21 4H17.05v.01zM12.03 5.25c-.09 0-.19.01-.28.01-1.28-.08-2.43-.6-3.26-1.52-.77-.87-1.25-2.04-1.25-3.27 0-.14.01-.27.02-.41C8.61.16 9.87.69 10.74 1.62c.73.78 1.18 1.83 1.18 2.96 0 .15-.01.3-.02.44.04.2.09.23.13.23z"/></svg>
                    Sign in with Apple
                </button>
                <p class="m-auth-desc">Quick sign in to auto-fill your details securely.</p>
                
                <div class="m-f-secure" style="margin-top:2rem;">
                    <svg style="color:var(--color-copper)" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                    Your information is secure and will not be shared.
                </div>
            </div>
        </div>
    </section>

    <!-- MOCKUP FOOTER -->
    <footer class="m-footer">
        <div class="c-container m-footer-grid">
            <div class="m-f-col m-f-brand">
                <div class="c-logo">
                    <img src="/Realtek_Logo.png" alt="Realtek Logo">
                </div>
                <p class="m-f-desc">REALTEK ENGINEERING PTE. LTD.<br>UEN: 20230693C</p>
                <p class="m-f-desc">18 Boon Lay Way #09-142,<br>TradeHub 21, Singapore 609966</p>
                <p class="m-f-desc">&copy; 2024 Realtek Engineering Pte. Ltd.<br>All rights reserved.</p>
            </div>
            
            <div class="m-f-col">
                <h4>COMPANY</h4>
                <a href="#about">About Us</a>
                <a href="#team">Our Team</a>
                <a href="#careers">Careers</a>
                <a href="#contact">Contact</a>
            </div>
            
            <div class="m-f-col">
                <h4>ENGINEERING</h4>
                <a href="#ci">C&I Solar PV</a>
                <a href="#ei">Electrical & Instrumentation (E&I)</a>
                <a href="#hdb">HDB Solar PV</a>
            </div>
            
            <div class="m-f-col">
                <h4>PROJECTS</h4>
                <a href="#projects">All Projects</a>
                <a href="#featured">Featured Project</a>
                <a href="#enquiries">Project Enquiries</a>
            </div>
            
            <div class="m-f-col">
                <h4>EZY SAAS</h4>
                <a href="#ezyhr">ezyHR</a>
                <a href="#ezybooks">ezyBooks</a>
                <a href="#ezycrm">ezyCRM</a>
            </div>
            
            <div class="m-f-col">
                <h4>SUPPORT & LEGAL</h4>
                <a href="#privacy">Privacy Policy</a>
                <a href="#terms">Terms of Service</a>
                <a href="#data">Data Protection</a>
            </div>

            <div class="m-f-col">
                <h4>FOLLOW US</h4>
                <a href="https://linkedin.com" target="_blank" class="m-f-social">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                </a>
            </div>
        </div>
    </footer>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace from <section id="engineering" ... to </footer>
import re
new_html = re.sub(r'<section id="engineering".*?</footer>', html_mockup, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
