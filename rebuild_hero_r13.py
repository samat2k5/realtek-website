import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_html = """    <section class="hero-r13">
        <div class="hero-r13__content">
            <div class="hero-r13__copy">
                <p class="hero-r13__eyebrow">INTEGRATED ENGINEERING & DIGITAL SOLUTIONS</p>
                <h1 class="hero-r13__title">
                    <span>POWERING</span><br>
                    <span>INDUSTRY.</span><br>
                    <span class="accent">DRIVING</span><br>
                    <span class="accent">INTELLIGENCE<span class="dot">.</span></span>
                </h1>
                <p class="hero-r13__description">
                    REALTEK ENGINEERING PTE. LTD. delivers integrated Solar, Electrical, Digital and Technology Solutions for businesses in Singapore.
                </p>
                <div class="hero-r13__actions">
                    <a href="#engineering" class="c-btn btn-primary">Explore Engineering &rarr;</a>
                    <a href="#digital" class="c-btn btn-outline">Explore ezy SaaS &rarr;</a>
                </div>
            </div>
        </div>
        
        <div class="hero-r13__media">
            <img src="/Realtek_R1.3_Approved_Singapore_Solar_Hero_HD.png" alt="Realtek Singapore Solar Engineering">
        </div>
        
        <div class="hero-r13__message">
            Building a sustainable future through engineering excellence and smart technology.
        </div>
    </section>"""

# Replace anything starting with <header class="c-hero"> and ending with </header>
html = re.sub(r'    <header class="c-hero">.*?</header>', hero_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hero_css = """/* HERO R1.3 */
.hero-r13 {
  display: grid;
  grid-template-columns: minmax(0, 44%) minmax(0, 56%);
  min-height: 760px;
  position: relative;
  overflow: hidden;
  background: #F7F3EA;
}

.hero-r13__content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  background: #F7F3EA;
  /* Align to the site grid (max-width 1280px) */
  padding-left: max(2rem, calc((100vw - 1280px) / 2 + 2rem));
  padding-right: 3rem;
  padding-top: 6rem;
  padding-bottom: 6rem;
}

/* The curved transition */
.hero-r13__content::after {
  content: "";
  position: absolute;
  top: 0;
  right: -90px;
  width: 180px;
  height: 100%;
  background: #F7F3EA;
  border-radius: 0 50% 50% 0;
  z-index: -1;
}

.hero-r13__copy {
  width: 100%;
  max-width: 540px;
}

.hero-r13__eyebrow {
  color: #065E55;
  font-weight: 700;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin: 0 0 1.5rem 0;
}

.hero-r13__title {
  font-size: clamp(54px, 4.1vw, 74px);
  line-height: 0.96;
  margin: 0 0 24px 0;
  font-weight: 800;
}

.hero-r13__title span {
  display: inline-block;
  color: #171D1C;
}

.hero-r13__title span.accent {
  color: #065E55;
}

.hero-r13__title .dot {
  color: #D96F27;
  display: inline;
}

.hero-r13__description {
  max-width: 420px;
  font-size: 1.125rem;
  line-height: 1.6;
  color: #171D1C;
  margin: 0 0 40px 0;
  font-weight: 500;
}

.hero-r13__actions {
  display: flex;
  gap: 1rem;
}

.hero-r13__media {
  position: relative;
  overflow: hidden;
  z-index: 1;
}

.hero-r13__media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 52% center;
  display: block;
}

.hero-r13__message {
  position: absolute;
  bottom: 3rem;
  right: 3rem;
  background: #065E55;
  color: #fff;
  padding: 1.5rem;
  max-width: 260px;
  border-radius: 4px;
  z-index: 3;
  font-size: 0.95rem;
  line-height: 1.5;
  font-weight: 500;
}

/* RESPONSIVE */
@media (max-width: 1280px) {
  .hero-r13 {
    grid-template-columns: minmax(0, 48%) minmax(0, 52%);
  }
}

@media (max-width: 1024px) {
  .hero-r13 {
    min-height: 600px;
  }
  .hero-r13__title {
    font-size: clamp(42px, 5vw, 54px);
  }
  .hero-r13__content::after {
    right: -60px;
    width: 120px;
  }
}

@media (max-width: 768px) {
  .hero-r13 {
    display: flex;
    flex-direction: column;
    min-height: auto;
  }
  .hero-r13__content {
    padding: 6rem 2rem 4rem;
    align-items: flex-start;
  }
  .hero-r13__content::after {
    display: none;
  }
  .hero-r13__media {
    width: 100%;
    height: 50vh;
    min-height: 400px;
  }
  .hero-r13__copy {
    max-width: 100%;
  }
  .hero-r13__description {
    max-width: 100%;
  }
  .hero-r13__message {
    bottom: 1.5rem;
    right: 1.5rem;
    max-width: 240px;
  }
}

@media (max-width: 480px) {
  .hero-r13__actions {
    flex-direction: column;
  }
  .hero-r13__title {
    font-size: clamp(38px, 9vw, 46px);
  }
}

"""

# Regex replacement: delete everything from /* HERO to the next section like /* CAPABILITIES
# Using lookahead to ensure we stop before the next section
css = re.sub(r'/\*\s*HERO(.*?)\*/.*?((?=/\*\s*CAPABILITIES)|(?=/\*\s*CHANGI))', hero_css, css, flags=re.DOTALL | re.IGNORECASE)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
