# Gold Marine Solutions — Website

Static website for **Gold Marine Solutions** — mobile marine mechanic and auto electrician serving the Gold Coast and SEQ.

Live site: [goldmarinesolutions.com](https://goldmarinesolutions.com)

---

## Tech Stack

- **Plain HTML / CSS / JavaScript** — no build step, no framework, no dependencies
- **Netlify** — hosting and form handling
- **Netlify Forms** — contact form submissions (free, built-in)
- **Google Analytics 4** — tracking ID `G-6W754KYH0C`
- **Google Fonts** — Inter (loaded via CDN)

---

## Running Locally

No build process needed. Open any HTML file directly in your browser:

```bash
# Option 1 — double-click index.html in Finder

# Option 2 — local dev server (recommended)
npx serve .
# then open http://localhost:3000
```

> Note: The contact form will **not** work locally — Netlify Forms only processes submissions on the live Netlify domain.

---

## Deploying a Change

### Drag & Drop (simplest)
1. Go to [app.netlify.com](https://app.netlify.com) → your site → **Deploys**
2. Drag the entire project folder onto the deploy dropzone
3. Live in ~30 seconds

### Git-connected deploy (recommended)
1. Connect this GitHub repo to your Netlify site
2. Push any change to the `main` branch
3. Netlify auto-deploys within ~1 minute

---

## File Structure

```
/
├── index.html              ← Homepage (main file — edit this most)
├── coomera.html            ← Suburb SEO landing page
├── hope-island.html        ← Suburb SEO landing page
├── runaway-bay.html        ← Suburb SEO landing page
├── southport.html          ← Suburb SEO landing page
├── links.html              ← Link-in-bio / social links page
├── privacy.html            ← Privacy policy
├── netlify.toml            ← Netlify config
├── robots.txt              ← Search engine crawl rules
├── sitemap.xml             ← XML sitemap for SEO
├── googlea6d39f31da54cb95.html  ← Google Search Console verification (do not delete)
├── logo.png
├── geordie.jpg             ← Owner photo (About section)
└── [various .jpg images]   ← Hero, gallery, and service card photos
```

---

## Contact Form

Uses **Netlify Forms** natively — no third-party service, no API keys.

Submissions appear in: Netlify dashboard → Forms

To receive email notifications: Site settings → Forms → Form notifications → Add notification → Email

---

## Gotchas

- All CSS and JS is **inline** in each HTML file — no separate stylesheet or script files
- Suburb pages share the same nav/footer as `index.html` but are **not templated** — nav changes must be made in each file separately
- `googlea6d39f31da54cb95.html` must stay in the root or Google Search Console breaks
- `service-electrical (1).jpg` is a duplicate and unused — safe to delete
