# Gold Marine Solutions — Handover Doc for Claude

This file is for Claude (or any AI assistant) helping Geordie maintain and edit this website.

---

## What This Site Is

Static website for **Gold Marine Solutions** — Geordie Bridges, mobile marine mechanic and auto electrician, Gold Coast / SEQ.

- **Live URL**: https://goldmarinesolutions.com
- **Owner**: Geordie Bridges — geordie@goldmarinesolutions.com — 0436 965 243

---

## Tech Stack

| Layer | Tech |
|-------|------|
| Language | Plain HTML, CSS (inline `<style>`), vanilla JS (inline `<script>`) |
| Framework | None |
| Build step | None — files deployed as-is |
| Hosting | Netlify |
| Forms | Netlify Forms (native `netlify` attribute on `<form>`) |
| Analytics | Google Analytics 4 — `G-6W754KYH0C` |
| Fonts | Google Fonts CDN — Inter |
| Domain | goldmarinesolutions.com (Geordie owns it) |

No npm, no Node, no bundler. Edit any `.html` file in a text editor, deploy, done.

---

## Running Locally

```bash
# Simplest — just open in browser:
open index.html

# Better — local dev server:
npx serve .
# Visit http://localhost:3000
```

Contact form won't work locally — that's expected. Netlify only processes it on the live domain.

---

## How to Deploy a Change

### Drag & Drop (no Git needed):
1. Edit the file(s) locally
2. Go to https://app.netlify.com → your site → Deploys tab
3. Drag the whole project folder onto the deploy dropzone
4. Wait ~30 seconds. Done.

### Via Git (cleaner):
1. Edit, then: `git add . && git commit -m "what you changed" && git push`
2. Netlify detects the push and auto-deploys within ~1 minute

---

## File Structure

```
/
├── index.html              ← MAIN PAGE — homepage, edit this most
├── links.html              ← Social / link-in-bio page
├── privacy.html            ← Privacy policy
├── netlify.toml            ← Netlify config (leave alone)
├── robots.txt              ← Tells Google what to crawl
├── sitemap.xml             ← Page list for Google SEO
├── googlea6d39f31da54cb95.html  ← DO NOT DELETE — Google Search Console verification
├── logo.png
├── geordie.jpg             ← Geordie's photo (About section)
└── [various .jpg images]   ← Hero, gallery, and service card photos
```

---

## Contact Form

Located in `index.html` (search for `<form name="contact"`).

Uses **Netlify Forms** — completely free, zero code required.

```html
<form name="contact" method="POST" netlify netlify-honeypot="bot-field">
```

- Submissions appear in: Netlify dashboard → Forms
- To get email notifications: Site settings → Forms → Form notifications → Add notification → Email
  - Use: `geordie@goldmarinesolutions.com`

---

## Hardcoded Values — Find & Replace These If They Change

Search across **all `.html` files** if any of these change:

| What | Current value |
|------|--------------|
| Phone (display) | `0436 965 243` |
| Phone (links/tel) | `61436965243` |
| Email | `geordie@goldmarinesolutions.com` |
| WhatsApp link | `https://wa.me/61436965243` |
| Facebook | `https://www.facebook.com/profile.php?id=61556990786261` |
| Instagram | `https://www.instagram.com/outbackdiesel/` |
| Google Analytics ID | `G-6W754KYH0C` (in `index.html` `<head>`) |

---

## Gotchas & Known Issues

1. **All CSS/JS is inline** — no separate `.css` or `.js` files. Everything lives inside `<style>` and `<script>` tags in each HTML file.

2. **Suburb pages were removed** — `coomera.html`, `hope-island.html`, `runaway-bay.html`, `southport.html` previously existed as suburb-specific SEO landing pages but have been deleted (Geordie operates fully mobile across the whole region, so suburb-specific pages were misleading). 301 redirects in `netlify.toml` send the old URLs to `/#areas` so any inbound links don't 404.

3. **`netlify.toml` had an old absolute path** — the `publish =` line originally pointed to a Google Drive path. It's been corrected to `"."`. If Netlify ever complains about the publish directory, make sure it reads `publish = "."`.

4. **`service-electrical (1).jpg`** — duplicate file, not referenced in any HTML. Safe to delete.

5. **`googlea6d39f31da54cb95.html`** — must stay in the root folder or Google Search Console will lose site verification.

6. **`netlify.toml` references `@netlify/plugin-emails`** — this plugin was added during development but is not actively used. It won't cause errors; can be removed if desired.

---

## Common Edits

**Change phone number or email:** Find & Replace (Cmd+Shift+H in VS Code) across all `.html` files.

**Add a new service card:** Find `<!-- SERVICES -->` in `index.html`, copy an existing `.service-card` block.

**Add a gallery photo:** Add your `.jpg` to the root folder, then add an `<img>` inside the `.gallery-grid` section of `index.html`.

**Update a testimonial:** Search `review-text` in `index.html`.

**Change business hours:** Search `Mon-Sun` in `index.html`.

**Add a new suburb to the service-area chips:** Add a `<span class="area-tag">Suburb Name</span>` inside the `.area-tags` block in `index.html`. No separate page needed — Geordie services everywhere mobile.
