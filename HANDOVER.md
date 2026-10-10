# Gold Marine Solutions — maintenance guide

For Geordie, or any AI assistant working on this site.

**Live:** https://goldmarinesolutions.com
**Owner:** Geordie Bridges · geordie@goldmarinesolutions.com · 0436 965 243
**Repo:** github.com/gbridges-alt/gold-marine-solutions-website (public)
**Last launch:** 10 Oct 2026 — the 4-URL single-page site was replaced by the
current 12-page structure.

This file is served as 404 and is not public. Keep it that way; it is listed
in the `netlify.toml` redirects.

---

## The rule that matters most

> **Credentials.** Gold Marine holds a **mechanical trade qualification**. It
> does **not** hold an Australian auto-electrician qualification or an
> electrical contractor licence.
>
> Never write "auto electrician", "qualified electrician", or anything
> implying unrestricted 240V/AC capability. Approved wording:
> *"marine 12V and 24V electrical diagnosis, testing and troubleshooting
> backed by Geordie's heavy-diesel mechanical and electrical training."*

Four more claims the site deliberately does **not** make. Check these after
any copy change:

| Never claim | Why |
|---|---|
| Manufacturer affiliation | The brand band is nominative use only |
| Guaranteed 24/7 availability | Urgent Callout offers willingness, not a dispatch guarantee |
| Marine surveying | Purchase & Sale explicitly disclaims it and refers to an AMSA surveyor |
| Dometic/VacuFlush dealership | Vessel Systems carries a non-affiliation line |

Sweep for them:

```bash
grep -rniE 'auto electrician|qualified electrician|240v|authorised dealer|approved service centre|24/7|marine surveyor' --include='*.html' .
```

---

## Structure

Five pillars, one page each. There are **no child pages** — Mechanical,
Electrical and Vessel Systems were each consolidated from a hub plus children
in Oct 2026, because customers should not have to pick a subsystem before
making contact.

```
/                                           home — owns the head terms
/marine-mechanical/                         consolidated pillar
/marine-electrical/                         consolidated pillar
/vessel-systems/                            consolidated pillar
/purchase-and-sale/                         hub
/purchase-and-sale/pre-purchase-inspection/ the money page for this pillar
/vessel-management/                         positioning pillar
/emergency-marine-callout/                  life-safety page
/contact/                                   single conversion destination
/membership.html   /links.html   /privacy.html
```

**Keyword split.** Home owns *marine mechanic Gold Coast*, *mobile marine
mechanic Gold Coast*, *boat mechanic Gold Coast*. The Mechanical page
deliberately does **not** target those — it takes service-level terms
(*marine engine service*, *boat engine repair*). Do not let the pillar pages
drift onto the head terms; that is the cannibalisation the split prevents.

**Split a pillar back into child pages only when Search Console shows the
demand.** Start consolidated.

---

## Tech

Plain static HTML. No npm, no build step, no framework. Edit a `.html` file,
push, done.

| | |
|---|---|
| Shared CSS | `assets/css/site.css` — linked by all 12 pages |
| Shared JS | `assets/js/site.js` |
| Cache busting | `site.css?v=<hash>` — **must be updated when the CSS changes** |
| Hosting | Netlify, project `gold-marine-solutions-au` |
| Forms | Netlify Forms, 3 of them |
| Analytics | GA4 `G-6W754KYH0C` |
| Netlify plugin | `@netlify/plugin-emails` — installed, unused |

Older notes said "all CSS is inline". That has not been true since the shared
stylesheet was extracted. Some pages still carry page-local `<style>` blocks
**after** the site.css link, to override it — `membership.html` and
`privacy.html` especially. Leave those below the link or they stop working.

### After any CSS change

```bash
H=$(shasum -a 256 assets/css/site.css | cut -c1-8)
grep -rl 'site\.css?v=' . --include='*.html' | grep -v '\.git' | xargs sed -i '' "s|site\.css?v=[0-9a-f]*|site.css?v=$H|g"
```

Skip this and visitors keep the old stylesheet from cache.

---

## The shared header and footer

**Never hand-edit nav or footer markup in a page.** It is duplicated across
all 12 and will drift. It is owned by:

```bash
python3 _tools/sync_shared.py --check   # report drift, change nothing
python3 _tools/sync_shared.py           # rewrite all pages
```

Edit the `PILLARS` list in `_tools/sync_shared.py`, run it, commit everything.
A pillar with `[]` children renders as a plain nav link with no dropdown.

`--check` should always say `would change: 0` before you commit.

---

## Running locally

```bash
cd "/Users/geordiebridges/Desktop/Gold Marine Solutions website/Gold Marine Solutions/gold-marine-solutions-website"
python3 _tools/devserver.py 4173
```

http://127.0.0.1:4173/ — sends no-store headers so you are never fooled by
cache, and accepts form POSTs so the contact page does not 501.

If the port is held by a stale process: `lsof -nP -iTCP:4173` then `kill -9`.
This has happened twice; the symptom is `ERR_CONNECTION_RESET`.

---

## Deploying

Auto-publish is **on**. A push to `main` goes live as soon as the build
finishes — there is no review step.

```bash
git push origin main
```

**To get a review step back:** Netlify → Deploys → *Lock to stop auto
publishing*. Builds still run; nothing goes live until you click Publish.
Worth doing for anything structural.

**Rollback:** Netlify → Deploys → pick an earlier deploy → *Publish deploy*.
Seconds, no rebuild. `main@b9c5c64` is the pre-launch site if you ever need it.

**Never drag-and-drop a folder to deploy production.** Manual deploys do not
get the `context.branch-deploy` noindex headers, and a preview deployed that
way was fully indexable for several days before it was caught.

---

## netlify.toml — why each rule exists

Validate before committing. Hand-inspection is not enough — an unvalidated
edit broke a production deploy:

```bash
python3 -c "import tomli; d=tomli.load(open('netlify.toml','rb')); print('ok', len(d['redirects']), 'redirects')"
```

| Rule | Why |
|---|---|
| `pretty_urls = false` | Netlify rewrote every internal `.html` link to extensionless **after deploy**, so rendered links disagreed with their own canonicals. Do not remove. |
| `/membership` → `/membership.html` (301) | Netlify serves both forms with a 200. `.html` is canonical; these collapse the duplicate. |
| `/_tools/*`, `/HANDOVER.md`, `/README.md` → 404 | `publish = "."` would otherwise serve them publicly. Add any new internal file here. |
| `[[headers]]` for `/assets/docs/*` | noindex for the sample PDF, which cannot carry a meta tag. **Never widen to `/*`** — that deindexes the site. |
| `context.branch-deploy` / `context.deploy-preview` | The only staging noindex. Never applies to production. |

**Do not add `headers = []` back at the top.** It conflicts with `[[headers]]`
and fails the build with a TOML parse error.

---

## Search Console

**The property is not where you would guess.** It sits on
**gbridges@macromechanical.com**, and it is a **URL-prefix** property
(`https://goldmarinesolutions.com/`), verified by the two `google*.html` files
in the root — not a Domain property.

`geordie@goldmarinesolutions.com` has **no** Search Console properties. Signing
in as that account shows an empty "Add a website" screen, and asking for the
Domain property `sc-domain:goldmarinesolutions.com` returns "you don't have
access" on every account. Neither means the data is gone; it means the wrong
account or the wrong property type.

Direct link, including the account number:

```
https://search.google.com/u/0/search-console?resource_id=https%3A%2F%2Fgoldmarinesolutions.com%2F
```

To ask Google to recrawl a page: URL inspection → paste the full URL → enter →
**REQUEST INDEXING**. Roughly 10 per property per day. The sitemap handles
discovery on its own; this only jumps the queue after a change.

---

## Indexing

| | |
|---|---|
| Indexable | all 11 public pages, no robots meta, no `X-Robots-Tag` |
| `links.html` | `noindex, follow` on purpose, excluded from sitemap |
| Sample PDF | noindex via header, excluded from sitemap |
| sitemap.xml | 11 URLs — update it when you add a page |

No HTML file carries a blanket noindex, so nothing can suppress production by
being merged.

---

## URLs that must not change

These carried the site's entire search presence before launch:

```
/            /membership.html     /links.html     /privacy.html
```

Also keep `google5dcc5927d4598317.html` and `googlea6d39f31da54cb95.html` in
the root, or Search Console loses verification.

---

## Working with images

**EXIF rotation is the trap.** Most phone photos here are stored landscape and
displayed portrait. `sips` crops in **stored** coordinates, so a crop computed
from what you see lands on the wrong axis — this produced a rotated frame with
black padding more than once.

Mapping from displayed `(dx, dy, dw, dh)` to a sips crop:

```
sips -c <dw> <dh> --cropOffset <H - dx - dw> <dy>     # H = stored height
```

A resize pass (`sips -Z 1600`) sometimes normalises orientation and makes
plain crops behave. **Always look at the output before committing it.**

**Crop to the frame's ratio** rather than letting `object-fit: cover` guess.
Measure the frame in the browser first:

```js
const r = document.querySelector('.route-card-img').getBoundingClientRect();
r.width / r.height
```

Current frames: service cards `2.31`, about-img `1.14`, work-list is
uncropped (`max-height` only).

**Check before publishing any job photo:** builder's plates, job and slot
numbers, other vessels' registrations, client houses. One frame had a Princess
builder's plate with job numbers and had to be recropped. `IMG_9071.jpg` is the
uncropped version and must never be used — `IMG_9071-cropped.jpg` is the safe one.

---

## Forms

Three, all Netlify Forms. Submissions appear in Netlify → Forms.

```
index.html          name="contact"
contact/index.html  name="contact"
membership.html     name="membership-waitlist"
```

Each has a honeypot: `<p class="hp-field" aria-hidden="true">` with a
`bot-field` input. It is hidden off-screen, not `display:none`, and carries no
label text — the old version left "Don't fill this out:" in the raw HTML where
audit tools read it as page content. Keep the `netlify-honeypot="bot-field"`
attribute on the form.

---

## Hardcoded values

Find and replace across all `.html` if any change:

| What | Value |
|---|---|
| Phone (display) | `0436 965 243` |
| Phone (tel:) | `61436965243` |
| Email | `geordie@goldmarinesolutions.com` |
| WhatsApp | `https://wa.me/61436965243` |
| Facebook | `facebook.com/profile.php?id=61556990786261` |
| Instagram | `instagram.com/goldmarinesolutions/` |
| GA4 | `G-6W754KYH0C` |
| ABN | `57 680 746 356` |
| Labour rate | `$175/hr` |
| Petrol service from | `$350` |
| Diesel service from | `$525` |
| Pre-purchase from | `$395 + GST` |

**Pricing lives in two places on the homepage** — the pricing card *and* the
FAQPage JSON-LD. They have drifted before. Change both, and keep the schema
answer matching the visible answer or it breaches Google's guidelines.

---

## Life-safety copy

`/emergency-marine-callout/` carries the emergency notice. Verified against
mrq.qld.gov.au on 10 Oct 2026:

- The body is **Marine Rescue Queensland**. VMR Southport became MRQ Southport
  East on 20 Aug 2026 — "VMR" is out of date.
- Correct instruction, matching every MRQ unit page: **call 000 or radio
  Marine Rescue Queensland on VHF Channel 16**.
- **Never publish a rescue phone number.** The numbers on MRQ unit pages are
  general-enquiries and log-on lines, not emergency lines.
- Gold Marine's area spans several units, so name the statewide body, not one
  unit.

Re-verify if MRQ restructures again.

---

## Before you commit

```bash
python3 _tools/sync_shared.py --check          # expect: would change: 0
python3 -c "import tomli; tomli.load(open('netlify.toml','rb'))"
python3 -c "
import json,re,glob
for f in glob.glob('**/*.html',recursive=True):
    if f.startswith(('_tools','google')): continue
    for m in re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>',open(f).read(),re.S):
        json.loads(m)
print('JSON-LD ok')"
```

Then check the **deployed** output, not just source. Two defects this year were
invisible in source and only appeared after deploy: the Pretty URLs rewrite,
and a preview that shipped without its noindex headers.

---

## Open items

- **Vessel Systems has one photographed job**, against six on Mechanical. Any
  heads, holding-tank, bilge-pump or seacock photos would strengthen the
  weakest pillar on the site.
- **10 engine-series maintenance guides** sit in `~/Desktop/GMS Service/` —
  Caterpillar 3208/3406/C15/C18, Volvo Penta D-Series/KAD/TAMD/petrol,
  MerCruiser petrol, Yanmar. None is tied to a vessel or a client, so any
  could become a published guide the way the sample PDF was. The two
  vessel-named ones (Cameo, Riviera 43) and the `Mike Hemburrow` folder are
  client work — **do not publish those**.
- **15 unreferenced images** of 47 in `assets/img/`. Harmless, could be cleared.
- Controlling documents (`MASTER-SITEMAP-v3.2.md` and the LOCKED strategy
  files) still describe the pre-consolidation architecture. They need a new
  version to match the site as built.

---

## Baseline

`Gold Marine Solutions/_search-console-baseline-2026-10-10/` holds the last 12
months of the old site, captured the day it was replaced. It cannot be
regenerated.

Homepage **165 clicks / 6,901 impressions / avg position 13.82**. Clicks were
almost entirely brand. The restructure targets terms that had impressions and
zero clicks: *gold coast boat servicing* (285 impr, pos 39.9), *boat mechanic
gold coast* (184, pos 11.7), *marine mechanic gold coast* (142, pos 14.3).

Brand queries should not move. If *gold marine solutions* falls from position
1.08, something is wrong — that is not a settling period.
