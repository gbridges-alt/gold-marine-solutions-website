# Gold Marine Solutions — Handover Doc for Claude

This file is for Claude (or any AI assistant) helping Geordie maintain and edit this website.

---

## What This Site Is

Static website for **Gold Marine Solutions** — Geordie Bridges, mobile marine mechanic, Gold Coast / SEQ.

> **Credential rule.** Gold Marine holds a **mechanical trade qualification**. It does **not** hold an Australian auto-electrician qualification or an electrical contractor licence. Never write "auto electrician", "qualified electrician" or anything implying unrestricted 240V/AC capability. The approved wording is: *"marine 12V and 24V electrical diagnosis, testing and troubleshooting backed by Geordie's heavy-diesel mechanical and electrical training."*

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

> **You must use a local server. Do not open `index.html` from Finder.**
> The site is now multi-page with a shared stylesheet, shared JS and directory
> URLs (`/marine-mechanical/`). Those are root-relative, so under `file://`
> they resolve against your hard drive instead of the site — the CSS 404s and
> every page renders as unstyled text with no header. That is not a bug in the
> site; it is what `file://` does to a multi-page site.

```bash
cd "<this folder>"
python3 -m http.server 4173
# Visit http://127.0.0.1:4173/
```

Or `npx serve .` if you prefer Node.

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
| Instagram | `https://www.instagram.com/goldmarinesolutions/` |
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


---

# Staging branch — `staging/site-repositioning`

Phase 1 of the approved repositioning, built against `MASTER-SITEMAP-v3.2.md`
(LOCKED). **Production `main` is untouched.**

## What changed structurally

| Area | Before | After |
|---|---|---|
| Pages | 4 | 18 (4 existing + 14 new Phase 1 routes) |
| CSS | inline `<style>` per page | `/assets/css/site.css`, shared |
| JS | inline `<script>` per page | `/assets/js/site.js`, shared |
| Nav | flat anchor list | five pillar dropdowns + Urgent Callout route |
| Images | repo root | new imagery in `/assets/img/` (root images unchanged) |

Still plain HTML. Still no build step, no npm, no bundler. Edit any `.html`
file in a text editor and push.

## URLs that must never change

`/` · `/membership.html` · `/links.html` · `/privacy.html`

No redirects point at them and none should. The homepage `<title>` carries the
existing ranking for *marine mechanic Gold Coast* and the related head terms —
it is byte-identical to production and must not be materially changed.

## PRE-MERGE CHECKLIST — do all of this before merging to `main`

**Staging protection (must be removed):**

1. Strip every `STAGING-ONLY` marker. Two per page:
   ```bash
   grep -rn "STAGING-ONLY" --include="*.html" .
   ```
   - the `<meta name="robots" content="noindex,nofollow,noarchive">` line, which
     must go back to `index, follow` (or be removed, which means the same)
   - the `<div class="staging-banner">` block
2. Remove `class="has-staging-banner"` from every `<body>` tag.
3. Leave the `context.branch-deploy` / `context.deploy-preview` header blocks in
   `netlify.toml`. They never apply to production and protect future branches.

**Content blockers (pages that must not publish as-is):**

4. **Urgent Callout, Service Areas and About** carry visible
   `copy-placeholder` blocks because no FINAL page-copy file exists for them.
   Each block is wrapped in `STAGING-ONLY` markers, so step 1's grep catches
   them. Approve copy for each, or do not publish those routes.
   `/contact/` no longer shows one: the page is functionally complete (booking
   form, contact details, CTAs) and the outstanding intro copy would be an
   addition rather than a fix. Its build note is an HTML comment instead —
   a "copy pending approval" banner does not belong above the booking form on
   the site's single conversion destination.
5. **Urgent Callout** — confirm the current local marine rescue body and its
   contact details. Required by `MASTER-SITEMAP-v3.2` §4c before publication.
6. **Vessel Management §8** — the "View Sample Vessel Maintenance Guide" link
   routes to `/contact/` because the sample guide does not exist. The copy
   requires that destination to exist before launch.
7. **Purchase & Sale hub** is built from `PURCHASE-SALE-HUB-PAGE-COPY-v1.md`,
   which is **not FINAL**. Its §4 credential claim was replaced with the
   approved capability wording — re-confirm when that file goes FINAL.
8. **Owner-directed copy deviation — Marine Mechanical hub hero.**
   `MARINE-MECHANICAL-HUB-PAGE-COPY-v1.1-FINAL` §1 approved the sub-line
   *"across marine engines, propulsion and drivetrain — diesel, petrol and
   outboard."* It now reads *"across marine engine and propulsion systems —
   Diesel, Petrol and Outboards."* Changed on the owner's instruction, not a
   build decision. Fold into the copy file at its next revision so the document
   and the site agree.

9. **Interim imagery** — the Vessel Systems hero (brief §10) and the Sanitation
   hero (IMG_9071 needs a crop, brief §12) are running placeholder photography.

**SEO:**

10. Export Search Console page and query data **before** anything ships. Without
   a baseline you cannot tell a normal post-restructure dip from real damage.
11. Resubmit `sitemap.xml` in Search Console after the merge.
12. Confirm the four suburb redirects still resolve: `/coomera.html`,
    `/hope-island.html`, `/runaway-bay.html`, `/southport.html` →
    `/service-areas/` (301).

## Store — removed

Gold Marine no longer promotes or operates a Store through this website. There
was never an internal `/store` or `/shop` route — it was only an external link
to `https://shop.goldmarinesolutions.com`, which has been removed from the
mobile navigation and the footer. It was not replaced with anything.

If the Shopify property is being retired too, that is separate from this repo.
Nothing here links to it any more.

## Phase 2 swaps

Several cards route to `/contact/` as a deliberate single link value so each
Phase 2 page launch is a one-line change:

| Card | Currently | Phase 2 target |
|---|---|---|
| Electrical hub §3 | `/contact/` | `/marine-electrical/repairs-fault-finding/` |
| Mechanical hub §3 ×3 | `/contact/` | gearbox / fuel-cooling / engine-diagnostics |
| Vessel Systems cards 2-4 | `/contact/` | freshwater / bilges / air-conditioning |
| Purchase & Sale "selling" | `/contact/` | `/purchase-and-sale/pre-sale-assessment/` |
| Vessel Management projects | `/contact/` | `/vessel-management/project-coordination/` |

None of them are "coming soon" and none are disabled. Hierarchy on those pages
reflects routing priority, not capability.
