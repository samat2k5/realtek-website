import os

# --- index.html ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update ACTIVE badge
old_badge = '<span class="m-proj-tag tag-active" style="margin-left: 0.5rem; font-size: 0.6rem; vertical-align: middle;">ACTIVE</span>'
new_badge = '<span class="m-proj-tag tag-active" style="margin-left: 0.5rem; font-size: 0.6rem; vertical-align: middle; background: #fff; color: var(--color-teal); border: 1px solid var(--color-teal);">ACTIVE</span>'
html = html.replace(old_badge, new_badge)

# 2. Adjust Mobile 2 position
# It is currently style="bottom:-30px; left:-50px; z-index:9; width: 25%; box-shadow: 0 20px 40px rgba(0,0,0,0.2);"
# We will move it to left: 15% to shift it rightwards, off the left menu.
html = html.replace('bottom:-30px; left:-50px; z-index:9; width: 25%;', 'bottom:-40px; left: 18%; z-index:9; width: 25%;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# --- style.css ---
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Contact Section to have white left column and light-grey right columns
old_contact = """.m-contact { background: #fff; padding: 6rem 0; }
.m-contact-grid { display: grid; grid-template-columns: 28% 42% 25%; gap: 2.5rem; align-items: start; }
.m-contact-left { background: var(--color-space); color: #fff; padding: 3rem 2.5rem; border-radius: 8px; box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: -2rem; }
.m-contact-left h2 { font-size: 2.5rem; line-height: 1.1; color: #fff; margin: 0 0 1rem 0; }
.m-contact-info { display: flex; flex-direction: column; gap: 1.5rem; }
.m-ci-item { display: flex; gap: 1rem; align-items: flex-start; font-size: 0.95rem; font-weight: 600; color: #fff; }"""

new_contact = """.m-contact { background: #fdfcf9; padding: 6rem 0; }
.m-contact-grid { display: grid; grid-template-columns: 28% 42% 25%; gap: 2.5rem; align-items: start; }
.m-contact-left { background: #fff; color: var(--color-space); padding: 3rem 2.5rem; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-top: -2rem; }
.m-contact-left h2 { font-size: 2.5rem; line-height: 1.1; color: var(--color-space); margin: 0 0 1rem 0; }
.m-contact-info { display: flex; flex-direction: column; gap: 1.5rem; }
.m-ci-item { display: flex; gap: 1rem; align-items: flex-start; font-size: 0.95rem; font-weight: 600; color: var(--color-space); }"""

css = css.replace(old_contact, new_contact)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixes applied successfully!")
