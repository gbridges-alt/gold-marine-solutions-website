#!/usr/bin/env python3
"""Rewrite the shared header and footer across every page.

The site is plain static HTML with no build step, so the nav and footer are
duplicated into all 18 pages. Editing them by hand is how they drift. Change
them HERE, run this once, and every page is updated identically.

    python3 _tools/sync_shared.py --check    # report drift, change nothing
    python3 _tools/sync_shared.py            # rewrite all pages

Everything else — page copy, per-page CTAs, images — is edited directly in the
HTML. This script only owns the block between <!-- NAV --> and the end of the
mobile menu, and the block from <!-- MOBILE STICKY CALL BAR --> to </footer>.
"""
import os
import re
import sys

PHONE_TEL = "tel:0436965243"
PHONE_DISPLAY = "0436 965 243"
EMAIL = "geordie@goldmarinesolutions.com"
WHATSAPP = ("https://wa.me/61436965243?text=Hi%20Geordie%2C%20I%27d%20like%20"
            "a%20quote%20for%20my%20boat.")

# Navigation order is deliberate: Mechanical and Electrical lead, because they
# remain the primary operational and lead-generation focus.
PILLARS = [
    # Mechanical is deliberately a single consolidated page with no children.
    # Owner-directed, 2026-10-06: the customer should not have to pick a
    # subsystem before making contact. Child pages may return later if Search
    # Console shows the demand to justify them.
    ("Mechanical", "/marine-mechanical/", []),
    # Consolidated the same way as Mechanical, owner-directed 2026-10-06.
    ("Electrical", "/marine-electrical/", []),
    # Consolidated like Mechanical and Electrical, owner-directed 2026-10-06.
    ("Vessel Systems", "/vessel-systems/", []),
    ("Purchase &amp; Sale", "/purchase-and-sale/", [
        ("Purchase &amp; Sale", "/purchase-and-sale/"),
        ("Vessel Purchase Advisory", "/purchase-and-sale/pre-purchase-inspection/"),
    ]),
    ("Vessel Management", "/vessel-management/", [
        ("Vessel Management", "/vessel-management/"),
        ("Gold Marine Memberships", "/membership.html"),
    ]),
]


def nav():
    items = []
    for label, hub, children in PILLARS:
        if not children:
            # No dropdown markup at all — an empty .nav-dropdown still renders
            # a hover target.
            items.append(
                '<div class="nav-item"><a href="{hub}">{label}</a></div>'.format(
                    hub=hub, label=label))
            continue
        drop = "".join(
            '<a href="{u}"{cls}>{l}</a>'.format(
                u=u, l=l, cls=' class="is-parent"' if u == hub else "")
            for l, u in children)
        items.append(
            '<div class="nav-item"><a href="{hub}">{label}</a>'
            '<div class="nav-dropdown">{drop}</div></div>'.format(
                hub=hub, label=label, drop=drop))
    desktop = "\n          ".join(items)

    mobile = []
    for label, hub, children in PILLARS:
        mobile.append('<div class="mm-group-label">{}</div>'.format(label))
        for l, u in (children or [("Marine " + label, hub)]):
            mobile.append('<a href="{u}" class="mm-child">{l}</a>'.format(u=u, l=l))
    mobile_links = "\n      ".join(mobile)

    return """<!-- NAV -->
<nav class="nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo" aria-label="Gold Marine Solutions — home">
      <img src="/logo.png" alt="Gold Marine Solutions" style="height:110px; max-width:280px; object-fit:contain; filter: drop-shadow(0 0 8px rgba(197,165,90,0.4));" loading="eager">
    </a>
    <div class="nav-links">
          {desktop}
    </div>
    <div class="nav-phone">
      <a href="/emergency-marine-callout/" class="btn-emergency"><span class="pulse-dot" aria-hidden="true"></span> Urgent Callout</a>
      <a href="/contact/" class="btn-nav">Get a Quote</a>
      <button class="hamburger" id="hamburger" aria-label="Menu" aria-expanded="false" aria-controls="mobileMenu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

<div class="mobile-menu" id="mobileMenu">
      {mobile}
      <div class="mm-group-label">More</div>
      <a href="/#about" class="mm-child">About</a>
      <a href="/#areas" class="mm-child">Service Areas</a>
      <a href="/emergency-marine-callout/" class="mm-child">Urgent Callout</a>
      <a href="/contact/" class="mobile-cta">Get a Quote</a>
</div>""".format(desktop=desktop, mobile=mobile_links)


def footer():
    return """<!-- MOBILE STICKY CALL BAR -->
<div class="sticky-call">
  <a href="{tel}" class="call-btn">&#128222; Call</a>
  <a href="{wa}" class="call-btn">&#128172; WhatsApp</a>
  <a href="/contact/" class="quote-btn">Get a Quote</a>
</div>

<!-- FOOTER -->
<footer class="footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <a href="/" class="nav-logo" style="margin-bottom:8px;">
        <img src="/logo.png" alt="Gold Marine Solutions" style="height:52px; filter: drop-shadow(0 1px 3px rgba(0,0,0,0.3));" loading="lazy">
      </a>
      <p>One call. Every marine solution.<br>Mobile marine mechanical and electrical service across the Gold Coast and South East Queensland.</p>
      <p style="margin-top:12px;">ABN 57 680 746 356</p>
    </div>
    <div>
      <h4>Services</h4>
      <a href="/marine-mechanical/">Marine Mechanical</a>
      <a href="/marine-electrical/">Marine Electrical</a>
      <a href="/vessel-systems/">Vessel Systems</a>
      <a href="/purchase-and-sale/">Purchase &amp; Sale</a>
      <a href="/vessel-management/">Vessel Management</a>
      <a href="/emergency-marine-callout/">Urgent Callout</a>
    </div>
    <div>
      <h4>Company</h4>
      <a href="/#about">About</a>
      <a href="/#areas">Service Areas</a>
      <a href="/membership.html">Memberships</a>
      <a href="/#gallery">Our Work</a>
      <a href="/contact/">Contact</a>
    </div>
    <div>
      <h4>Connect</h4>
      <a href="{tel}">{phone}</a>
      <a href="mailto:{email}">{email}</a>
      <a href="https://www.instagram.com/goldmarinesolutions/" rel="noopener">Instagram</a>
      <a href="https://www.facebook.com/profile.php?id=61556990786261" rel="noopener">Facebook</a>
      <a href="/links.html">Links</a>
      <a href="/privacy.html">Privacy Policy</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; <span id="year">2026</span> Gold Marine Solutions Pty Ltd. All rights reserved.</p>
  </div>
</footer>""".format(tel=PHONE_TEL, phone=PHONE_DISPLAY, email=EMAIL, wa=WHATSAPP)


NAV_PAT = r'<!-- NAV -->.*?<div class="mobile-menu" id="mobileMenu">.*?\n</div>'
FOOT_PAT = r'<!-- MOBILE STICKY CALL BAR -->.*?</footer>'


def pages(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '_tools', 'assets')]
        for f in filenames:
            if f.endswith('.html') and 'backup' not in f and not f.startswith('google'):
                out.append(os.path.join(dirpath, f))
    return sorted(out)


def main():
    check = '--check' in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    new_nav, new_foot = nav(), footer()
    changed, skipped = [], []

    for p in pages(root):
        s = open(p, encoding='utf-8').read()
        orig = s
        if re.search(NAV_PAT, s, re.S):
            s = re.sub(NAV_PAT, lambda _: new_nav, s, flags=re.S)
        if re.search(FOOT_PAT, s, re.S):
            s = re.sub(FOOT_PAT, lambda _: new_foot, s, flags=re.S)
        rel = os.path.relpath(p, root)
        if s == orig:
            skipped.append(rel)
        else:
            changed.append(rel)
            if not check:
                open(p, 'w', encoding='utf-8').write(s)

    print("in sync : %d" % len(skipped))
    print("%s: %d" % ("would change" if check else "updated", len(changed)))
    for c in changed:
        print("   " + c)
    if check and changed:
        sys.exit(1)


if __name__ == '__main__':
    main()
