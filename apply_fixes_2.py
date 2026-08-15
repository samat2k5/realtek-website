import os

# --- index.html ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update ezyHR Badges
html = html.replace('<h4>ezyHR</h4>', '<h4>ezyHR <span class="m-proj-tag tag-active" style="margin-left: 0.5rem; font-size: 0.6rem; vertical-align: middle;">ACTIVE</span></h4>')
html = html.replace('<h4>ezyBooks</h4>', '<h4>ezyBooks <span class="m-proj-tag" style="margin-left: 0.5rem; font-size: 0.6rem; background: #cbd5e1; color: #0a192f; vertical-align: middle;">COMING SOON</span></h4>')
html = html.replace('<h4>ezyCRM</h4>', '<h4>ezyCRM <span class="m-proj-tag" style="margin-left: 0.5rem; font-size: 0.6rem; background: #cbd5e1; color: #0a192f; vertical-align: middle;">COMING SOON</span></h4>')

# 2. Adjust ezy SaaS Mobile 2 position
old_m2 = '<div class="m-mobile-frame" style="bottom:-50px; left:-30px; z-index:9; width: 25%; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">'
new_m2 = '<div class="m-mobile-frame" style="bottom:-30px; left:-50px; z-index:9; width: 25%; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">'
html = html.replace(old_m2, new_m2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# --- style.css ---
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix Changi Background
css = css.replace("url('/assets/images/hero/changi-flagship.jpg')", "url('/projects/changi-flagship.jpg')")

# 2. Fix Footer Grid
css = css.replace(".m-footer-grid { display: grid; grid-template-columns: 1.5fr repeat(6, 1fr); gap: 2rem; }", ".m-footer-grid { display: grid; grid-template-columns: 2fr repeat(5, 1fr); gap: 2rem; }")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updates applied successfully!")
