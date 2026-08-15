import os
import re

# --- index.html ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_footer_html = """    <!-- MOCKUP FOOTER RESTORED -->
    <footer class="c-footer" style="background: #0f172a; padding: 4rem 0 2rem 0; color: #fff; font-family: var(--font-primary);">
        <div class="c-container footer-grid" style="display: grid; grid-template-columns: 2fr 1fr 1.2fr 1fr 1fr 1.2fr; gap: 3rem;">
            <div class="f-brand">
                <div style="margin-bottom:1.5rem;">
                    <img src="/Realtek_Logo.png" alt="Realtek Logo" style="filter: brightness(0) invert(1); height: 32px; display: inline-block; vertical-align: middle;">
                    <span style="font-family: var(--font-logo); font-size: 1.5rem; vertical-align: middle; margin-left:0.5rem; font-weight:700;">Realtek</span>
                </div>
                <p style="color: rgba(255,255,255,0.8); line-height: 1.8; font-size:0.9rem; margin-bottom:0;">REALTEK ENGINEERING PTE. LTD.<br>UEN: 201723665M<br>132 Gul Circle, Singapore 629597</p>
            </div>
            <div class="f-col">
                <h4 style="font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 1.5rem; color: #fff;">COMPANY</h4>
                <a href="#about" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">About Us</a>
                <a href="#team" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Our Team</a>
                <a href="#careers" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Careers</a>
                <a href="#contact" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Contact</a>
            </div>
            <div class="f-col">
                <h4 style="font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 1.5rem; color: #fff;">ENGINEERING</h4>
                <a href="#ci" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">C&I Solar PV</a>
                <a href="#ei" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Electrical & Inst. (E&I)</a>
                <a href="#hdb" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">HDB Solar PV</a>
            </div>
            <div class="f-col">
                <h4 style="font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 1.5rem; color: #fff;">PROJECTS</h4>
                <a href="#projects" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">All Projects</a>
                <a href="#featured" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Featured Project</a>
                <a href="#enquiries" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Enquiries</a>
            </div>
            <div class="f-col">
                <h4 style="font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 1.5rem; color: #fff;">EZY SAAS</h4>
                <a href="#ezyhr" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">ezyHR</a>
                <a href="#ezybooks" style="display:block; color:rgba(255,255,255,0.5); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem; cursor:default;">ezyBooks</a>
                <a href="#ezycrm" style="display:block; color:rgba(255,255,255,0.5); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem; cursor:default;">ezyCRM</a>
            </div>
            <div class="f-col">
                <h4 style="font-size: 0.9rem; font-weight: 800; letter-spacing: 0.1em; margin-bottom: 1.5rem; color: #fff;">SUPPORT</h4>
                <a href="#support" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">ezyHR Support</a>
                <a href="#privacy" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Privacy Policy</a>
                <a href="#terms" style="display:block; color:rgba(255,255,255,0.8); text-decoration:none; margin-bottom:0.8rem; font-size:0.9rem;">Terms of Use</a>
            </div>
        </div>
        <div class="c-container" style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255, 255, 255, 0.1); display: flex; justify-content: space-between; align-items: center;">
            <div style="font-family: 'Space Grotesk', sans-serif; font-size:0.85rem; font-weight:800; letter-spacing:0.1em;">
                ENGINEERING TODAY. <span style="color: var(--color-copper);">INTELLIGENCE FOR TOMORROW.</span>
            </div>
            <p style="color: rgba(255, 255, 255, 0.5); font-size: 0.85rem; margin:0;">&copy; 2024 Realtek Engineering Pte. Ltd. All rights reserved.</p>
        </div>
    </footer>"""

# Regex to match the entire m-footer
html = re.sub(r'<!-- MOCKUP FOOTER -->\s*<footer class="m-footer">.*?</footer>', new_footer_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Footer restored!")
