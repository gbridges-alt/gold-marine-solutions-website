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
python3 _tools/devserver.py
# Visit http://127.0.0.1:4173/
```

Use `_tools/devserver.py`, not `python3 -m http.server`. The plain server
answers form POSTs with 501 (the booking form looks broken) and sends no
cache headers, so the browser keeps showing a stale build after every edit.

If the page suddenly shows `ERR_CONNECTION_RESET`, the server has stopped or
is stale. Check with `lsof -ti:4173`, `kill -9 <pid>`, and start it again.

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
├── assets/                 ← Shared CSS, JS and the newer photography
│   ├── css/site.css        ← Site-wide stylesheet (all pages link it)
│   ├── js/site.js          ← Nav, FAQ accordion, contact-form ?type= preselect
│   └── img/                ← Imported Gold Marine photos, web-sized
├── _tools/                 ← Local dev scripts, never served (404 via netlify.toml)
└── [various .jpg images]   ← Remaining legacy gallery and service card photos
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

4. **No page carries a visible copy placeholder any more.** `/about/` and
   `/service-areas/` were removed at the owner's request (see the deviation
   notes below), and `/emergency-marine-callout/` and `/contact/` run on
   approved or structural content. Step 1's `STAGING-ONLY` grep now only has
   the banner and the meta robots tag to find.
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
8. **Owner-directed copy deviations — Marine Mechanical hub.**
   `MARINE-MECHANICAL-HUB-PAGE-COPY-v1.1-FINAL` §1 approved the sub-line
   *"across marine engines, propulsion and drivetrain — diesel, petrol and
   outboard."* It now reads *"across marine engine and propulsion systems —
   Diesel, Petrol and Outboards."* Changed on the owner's instruction, not a
   build decision.
   Same file, §3 sub-line: approved copy read *"Not every propulsion job is an
   engine service."* It now reads *"Marine mechanical work goes well beyond
   routine engine servicing."* Also owner-directed.
   Same file, §2: the two "Confirmed work includes ..." proof lines were
   removed from the Diesel and Petrol & Outboard routing cards as too wordy.
   §2 specifies "one service-led line plus one proof line each". The same proof
   is still carried in full in the Real work sections of both child pages, so
   nothing is lost from the site.
   Fold all three into the copy file at its next revision so the document and
   the site agree.

9. **Owner-directed terminology change — "drivetrain" retired site-wide.**
   Replaced with "propulsion systems" throughout, on the owner's instruction.
   Two of these deviate from controlling documents and need folding back in:
   - `VESSEL-PURCHASE-ADVISORY-PAGE-COPY-v1.2-FINAL` §3: the inspection group
     *"Engines & drivetrain"* now reads *"Engines & propulsion systems"*.
   - `MASTER-SITEMAP-v3.2` names the Phase 2 page **Engine & Drivetrain
     Diagnostics** in five places (§4 Mechanical table, §4b collision table,
     §5 Phase 2 list, §7 CTA matrix). It is now presented as **Engine &
     Propulsion Diagnostics**. The sitemap is LOCKED and has NOT been edited —
     it needs a new version to carry this. **The URL is unchanged**
     (`/marine-mechanical/engine-diagnostics/`), and the §4b anti-cannibalisation
     rationale still holds: the name stays system-specific and does not stray
     into Marine Electrical Repairs & Fault Finding's territory.

10. **Interim imagery** — the Vessel Systems hero (brief §10) and the Sanitation
   hero (IMG_9071 needs a crop, brief §12) are running placeholder photography.

**SEO:**

11. Export Search Console page and query data **before** anything ships. Without
   a baseline you cannot tell a normal post-restructure dip from real damage.
12. Resubmit `sitemap.xml` in Search Console after the merge.
13. Confirm the four suburb redirects still resolve: `/coomera.html`,
    `/hope-island.html`, `/runaway-bay.html`, `/southport.html` →
    `/service-areas/` (301).

## Service Areas page — removed

`MASTER-SITEMAP-v3.2` lists **Service Areas** at `/service-areas/` as a Phase 1
page, and §6 makes it the single answer that replaces the deleted suburb pages.
Removed on the owner's instruction as unnecessary.

**This is a deviation from the LOCKED sitemap** and needs folding into a new
version of that document.

Two things were handled with it:

1. **The suburb redirects.** `netlify.toml` had `/coomera.html`,
   `/hope-island.html`, `/runaway-bay.html` and `/southport.html` 301-ing to
   `/service-areas/`. Those four were real URLs on the live site and still carry
   index presence, so they would have started landing on a 404. They now point
   at `/#areas`, which is exactly where production sends them today — so live
   behaviour is unchanged.

2. **Geographic relevance.** §7 relied on Service Areas linking to all five hubs
   and back, "now that there are no suburb pages". That reciprocal pair is gone.
   The homepage `#areas` section still lists the 22 areas served, and the nav and
   footer "Service Areas" links now point there. Worth watching in Search
   Console: if local coverage queries soften, this is the change to look at
   first.

## About page — removed

`MASTER-SITEMAP-v3.2` lists **About** at `/about/` as a Phase 1 trust page. It
was removed on the owner's instruction: it was hard to reach and, with no FINAL
copy ever written for it, only ever held a placeholder.

**This is a deviation from the LOCKED sitemap** and needs folding into a new
version of that document.

No SEO impact: `/about/` only ever existed on this branch, was never deployed
and was never indexed, so no redirect is required. The About content itself is
not lost — it lives in the homepage `#about` section, which is where the sitemap
notes it sat before the route was planned. The nav and footer "About" links now
point at `/#about`.

## Backup HTML files — removed

`index.backup.html`, `membership.backup-pre-premium.html` and
`membership.backup-pre-vessel-mgmt.html` were committed, so they would have
been served publicly and indexed at e.g. `/index.backup.html`. They carried
stale pricing and the auto-electrician credential claims. Deleted; git history
still has them. `.gitignore` now covers `*.backup.html` and `*.backup-*.html`,
so no new ones get committed.

Note: several backup files still sit in the working folder untracked. They will
never deploy via git, but they **would** deploy if you drag the whole folder
onto Netlify. Use git, or delete them locally before a drag-and-drop deploy.

## Editing the shared header and footer

The nav and footer are duplicated into all 18 pages, because the site is plain
HTML with no build step. Do not hand-edit them page by page — that is how they
drift. Edit `_tools/sync_shared.py` (it holds the nav order, the dropdown
contents and the footer columns) and run:

```bash
python3 _tools/sync_shared.py --check   # report drift, change nothing
python3 _tools/sync_shared.py           # rewrite every page
```

`--check` exits non-zero if any page has drifted, so it is worth running before
a merge. Everything else — page copy, per-page CTAs, images — is edited
directly in the HTML.

`_tools/` is committed so it cannot be lost, and `netlify.toml` returns 404 for
`/_tools/*` so it is never served.

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
