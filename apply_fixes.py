import os

# --- index.html ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update UEN and Address
html = html.replace('18 Boon Lay Way #09-142<br>TradeHub 21, Singapore 609966', '132 Gul Circle<br>Singapore 629597')
html = html.replace('UEN: 20230693C', 'UEN: 201723665M')
html = html.replace('18 Boon Lay Way #09-142,<br>TradeHub 21, Singapore 609966', '132 Gul Circle,<br>Singapore 629597')

# 2. Update SaaS screenshots
old_saas = """                    <div class="m-desktop-frame">
                        <div class="m-browser-bar"><span></span><span></span><span></span></div>
                        <img src="/assets/images/ezyHR.jpeg" alt="ezyHR Desktop">
                    </div>
                    <div class="m-mobile-frame">
                        <img src="/assets/images/ezyHR_mobile1.jpeg" alt="ezyHR Mobile">
                    </div>"""

new_saas = """                    <div class="m-desktop-frame">
                        <div class="m-browser-bar"><span></span><span></span><span></span></div>
                        <img src="/assets/images/ezyHR.jpeg" alt="ezyHR Desktop">
                    </div>
                    <div class="m-mobile-frame" style="bottom:-20px; right:-30px; z-index:10; width: 28%; box-shadow: 0 30px 60px rgba(0,0,0,0.3);">
                        <img src="/assets/images/ezyHR_mobile1.jpeg" alt="ezyHR Mobile 1">
                    </div>
                    <div class="m-mobile-frame" style="bottom:-50px; left:-30px; z-index:9; width: 25%; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">
                        <img src="/assets/images/ezyHR_mobile2.jpeg" alt="ezyHR Mobile 2">
                    </div>"""

if old_saas in html:
    html = html.replace(old_saas, new_saas)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# --- style.css ---
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Contact Background to 2 colors
old_contact = """.m-contact { background: #eaf1f1; padding: 6rem 0; }
.m-contact-grid { display: grid; grid-template-columns: 25% 45% 25%; gap: 2.5rem; align-items: start; }
.m-contact-left h2 { font-size: 2.5rem; line-height: 1.1; color: var(--color-space); margin: 0 0 1rem 0; }
.m-contact-info { display: flex; flex-direction: column; gap: 1.5rem; }
.m-ci-item { display: flex; gap: 1rem; align-items: flex-start; font-size: 0.95rem; font-weight: 600; color: var(--color-space); }"""

new_contact = """.m-contact { background: #fff; padding: 6rem 0; }
.m-contact-grid { display: grid; grid-template-columns: 28% 42% 25%; gap: 2.5rem; align-items: start; }
.m-contact-left { background: var(--color-space); color: #fff; padding: 3rem 2.5rem; border-radius: 8px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: -2rem; }
.m-contact-left h2 { font-size: 2.5rem; line-height: 1.1; color: #fff; margin: 0 0 1rem 0; }
.m-contact-info { display: flex; flex-direction: column; gap: 1.5rem; }
.m-ci-item { display: flex; gap: 1rem; align-items: flex-start; font-size: 0.95rem; font-weight: 600; color: #fff; }"""

if old_contact in css:
    css = css.replace(old_contact, new_contact)

# 2. Update Footer Background & Text Opacity
old_footer = """/* FOOTER */
.m-footer { background: var(--color-space); color: #fff; padding: 4rem 0 2rem; }
.m-footer-grid { display: grid; grid-template-columns: 1.5fr repeat(6, 1fr); gap: 2rem; }
.m-f-brand .c-logo img { filter: brightness(0) invert(1); width: 140px; margin-bottom: 1.5rem; }
.m-f-desc { font-size: 0.85rem; color: rgba(255,255,255,0.6); margin-bottom: 1rem; line-height: 1.5; }
.m-f-col h4 { font-size: 0.85rem; font-weight: 800; letter-spacing: 0.1em; color: #fff; margin-bottom: 1.5rem; }
.m-f-col a { display: block; color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.9rem; margin-bottom: 0.8rem; transition: color 0.2s; }"""

new_footer = """/* FOOTER */
.m-footer { background: #000000; color: #fff; padding: 4rem 0 2rem; }
.m-footer-grid { display: grid; grid-template-columns: 1.5fr repeat(6, 1fr); gap: 2rem; }
.m-f-brand .c-logo img { filter: brightness(0) invert(1); width: 140px; margin-bottom: 1.5rem; }
.m-f-desc { font-size: 0.85rem; color: rgba(255,255,255,0.9); margin-bottom: 1rem; line-height: 1.5; }
.m-f-col h4 { font-size: 0.85rem; font-weight: 800; letter-spacing: 0.1em; color: #fff; margin-bottom: 1.5rem; }
.m-f-col a { display: block; color: rgba(255,255,255,0.9); text-decoration: none; font-size: 0.9rem; margin-bottom: 0.8rem; transition: color 0.2s; }"""

if old_footer in css:
    css = css.replace(old_footer, new_footer)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates applied successfully!")
