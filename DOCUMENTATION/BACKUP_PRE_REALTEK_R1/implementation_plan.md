# Realtek Engineering Website Upgrade — EZY SaaS & ezyHR Integration Plan

Implementation plan to upgrade the existing **REALTEK ENGINEERING PTE. LTD.** website according to the official developer specification (`REALTEK_EZY_SaaS_Website_Developer_Specification.docx`).

## Executive Summary & Objectives

The goal is to upgrade the current website so that it:
1. Retains **REALTEK ENGINEERING PTE. LTD.**'s primary identity as a modern, high-tech industrial engineering firm.
2. Explicitly establishes **EZY SaaS** as its official technology initiative and **ezyHR** as its flagship Singapore HRMS & Payroll cloud product.
3. Fully satisfies **Apple Developer Organization** and **Google Play Organization** verification requirements by establishing an unmistakable legal entity relationship:  
   `REALTEK ENGINEERING PTE. LTD.` → `EZY SaaS` → `ezyHR`
4. Enhances SEO, legal compliance (Privacy Policy, Terms of Use, IRAS AIS vendor messaging), and mobile responsiveness without throwing away existing visual styles.

---

## Technical Architecture & Approach

* **Framework & Engine**: Vite + Multi-Page HTML5 structure (`index.html`, `ezy-saas/index.html`, `ezyhr/index.html`, `privacy/index.html`, `terms/index.html`).
* **Styling**: Modular CSS (`style.css`) using existing dark theme tokens (`#04090E` background, `#00B4D8` cyan glow, `#0D1B2A` navy, Audiowide & Plus Jakarta Sans fonts).
* **Interactivity**: Pure ES module JavaScript (`main.js`) with IntersectionObserver for animations, smooth scrolling, and accessible mobile hamburger navigation.

---

## Proposed Changes & Roadmap

### Priority 0 (P0) — Essential Brand & Verification Requirements

#### 1. Header & Navigation (`index.html`, `style.css`, `main.js`)
- [MODIFY] [index.html](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/index.html)
  - Add `EZY SaaS` link to main desktop navbar between `Projects` and `Contact`.
  - Implement mobile hamburger menu toggle for small screens (`aria-expanded`, `aria-controls`).

#### 2. Hero Section Update (`index.html`)
- Add Eyebrow: `INTEGRATED ENGINEERING & DIGITAL SOLUTIONS`
- Update H1: `POWERING INDUSTRY, DRIVING INTELLIGENCE.`
- Update Body Text: `REALTEK ENGINEERING PTE. LTD. delivers integrated Solar, Electrical, Digital and Technology Solutions for a smarter, more sustainable future.`
- CTAs: Primary `Explore Services` (`#services`) | Secondary `Explore EZY SaaS` (`/ezy-saas`).

#### 3. Core Expertise Cards (`index.html`)
- Update Card 3 title to `Digital Solutions & EZY SaaS`.
- Update bullet points: `ezyHR — HRMS & Payroll`, `ezyBooks — Accounting (Coming Soon)`, `Enterprise Software`, `Premium Web Development`.
- Add inline link: `Explore EZY SaaS →` (`/ezy-saas`).

#### 4. New `#ezy-saas` Homepage Section (`index.html`, `style.css`)
- Insert new section between Core Expertise and Recent Projects.
- Eyebrow: `OUR TECHNOLOGY INITIATIVE` | H2: `EZY SaaS` | Subtitle: `Business Software. Simplified.`
- Products Grid:
  - **ezyHR Card**: Cloud HRMS & Payroll for Singapore Businesses + CTA `Explore ezyHR →` (`/ezyhr`).
  - **ezyBooks Card**: Cloud Accounting & Finance (`Coming Soon`).
  - **ezyCRM Card**: Customer Relationship Management (`Coming Soon`).
- Legal ownership notice: *"EZY SaaS products are developed and operated by REALTEK ENGINEERING PTE. LTD., Singapore."*

#### 5. Dedicated Pages [NEW]
- [NEW] [ezy-saas/index.html](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/ezy-saas/index.html) — Dedicated crawlable page for EZY SaaS initiative.
- [NEW] [ezyhr/index.html](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/ezyhr/index.html) — Product page for ezyHR with 8-part feature grid (Employee Mgmt, Self-Service, Attendance, Leave, Payroll, Claims, Reports, SG Statutory), CTAs to `https://hr.ezy.sg/` and `support@hr.ezy.sg`.
- [NEW] [privacy/index.html](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/privacy/index.html) — Legal Privacy Policy for corporate & EZY SaaS.
- [NEW] [terms/index.html](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/terms/index.html) — Terms of Use.

#### 6. Contact Section & Footer Update (`index.html`, `style.css`)
- Standardize corporate legal entity name: `REALTEK ENGINEERING PTE. LTD.`
- Add contact channels:
  - Corporate: `admin@realtekengg.com`
  - EZY SaaS Support: `support@ezy.sg`
  - ezyHR Support: `support@hr.ezy.sg`
  - ezyHR Portal: `https://hr.ezy.sg/`
- Footer layout: Legal entity branding, 4-column link structure (Company, EZY SaaS, Support, Legal), Copyright 2026.

---

### Priority 1 (P1) — SEO, Compliance & Technical QA

#### 1. SEO & Metadata Integration
- Title tags, meta descriptions, canonical URLs, and OpenGraph/Twitter cards for `/`, `/ezy-saas`, `/ezyhr`, `/privacy`, `/terms`.
- [NEW] [public/sitemap.xml](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/public/sitemap.xml)
- [NEW] [public/robots.txt](file:///c:/Users/mathi/Desktop/AntiGravity%20Demos/Realtek%20Website/public/robots.txt)
- JSON-LD Organization Schema for `REALTEK ENGINEERING PTE. LTD.`.

#### 2. Compliance Audit
- Verify **IRAS AIS messaging**: Use *"Designed for Singapore payroll requirements"* instead of "IRAS Certified".

---

### Priority 2 (P2) — Polish & Build Optimization
- Multi-page configuration in `vite.config.js` to build all routes seamlessly.
- Responsive QA across mobile (320px, 375px, 390px), tablet (768px), and desktop (1024px+).

---

## Verification Plan

### Automated Build Verification
```powershell
npm run build
```
Ensure Vite correctly bundles all multi-page entry points (`index.html`, `ezy-saas/index.html`, `ezyhr/index.html`, `privacy/index.html`, `terms/index.html`) into `dist/` without broken asset paths or bundling errors.

### Manual Verification & Audit
1. **Link & Navigation Check**: Verify all header, body, section, and footer links point to valid targets.
2. **Mobile Hamburger Menu**: Verify menu toggle on <768px viewports with keyboard/touch accessibility.
3. **App Store Readiness Check**: Confirm `REALTEK ENGINEERING PTE. LTD.` legal entity text is consistent across headers, footers, JSON-LD, privacy policy, and product pages.
4. **IRAS Compliance**: Ensure no prohibited claims ("IRAS Certified") exist.
