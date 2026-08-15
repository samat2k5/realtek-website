from playwright.sync_api import sync_playwright
import os

sizes = [
    (1920, 1080),
    (1440, 900),
    (430, 932),
    (390, 844)
]

output_dir = r"C:\Users\mathi\.gemini\antigravity-ide\brain\40299fcc-46c6-483d-80f0-59946802aed9"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://localhost:5174/")
    
    for width, height in sizes:
        page.set_viewport_size({"width": width, "height": height})
        page.wait_for_timeout(1000)
        
        # Get computed styles for reporting
        if width == 1920:
            header_height = page.evaluate("window.getComputedStyle(document.querySelector('.c-nav')).height")
            hero_height = page.evaluate("window.getComputedStyle(document.querySelector('.hero-r13')).height")
            title_font = page.evaluate("window.getComputedStyle(document.querySelector('.hero-r13__title')).fontSize")
            trust_icon = page.evaluate("window.getComputedStyle(document.querySelector('.hero-r13__trust .trust-item svg')).width")
            trust_heading = page.evaluate("window.getComputedStyle(document.querySelector('.hero-r13__trust .trust-text strong')).fontSize")
            trust_sub = page.evaluate("window.getComputedStyle(document.querySelector('.hero-r13__trust .trust-text span')).fontSize")
            
            print("--- 1920px REPORT ---")
            print(f"Header Height: {header_height}")
            print(f"Hero Height: {hero_height}")
            print(f"Headline Font Size: {title_font}")
            print(f"Trust Icon Size: {trust_icon}")
            print(f"Trust Heading Size: {trust_heading}")
            print(f"Trust Secondary Text Size: {trust_sub}")
            print("---------------------")

        filename = f"screenshot_{width}x{height}.png"
        filepath = os.path.join(output_dir, filename)
        page.screenshot(path=filepath, full_page=True)
        print(f"Saved {filepath}")

    browser.close()
