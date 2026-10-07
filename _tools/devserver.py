#!/usr/bin/env python3
"""Local preview server for the Gold Marine staging site.

Two things python -m http.server cannot do, both of which we need:
  1. Accept form POSTs. The booking form posts to /contact/; a static server
     answers 501 and it looks like the form is broken.
  2. Send no-store headers. Without them the browser caches HTML, CSS and JS
     and keeps showing a stale build after every edit.

Local development only. Nothing here is part of the deployed site.

    python3 _tools/devserver.py [port]      # run from the repo root
"""
import os
import sys
import urllib.parse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_POST(self):
        length = int(self.headers.get('Content-Length') or 0)
        raw = self.rfile.read(length).decode('utf-8', 'replace')
        fields = urllib.parse.parse_qs(raw)
        name = (fields.get('form-name') or ['(no form-name)'])[0]
        print("\n=== FORM SUBMISSION: %s  (POST %s) ===" % (name, self.path))
        for k, v in fields.items():
            if k in ('form-name', 'bot-field'):
                continue
            print("  %-14s %s" % (k, v[0]))
        print("=== end ===\n", flush=True)

        body = (
            "<!doctype html><meta charset=utf-8><title>Submission received</title>"
            "<style>body{font-family:-apple-system,sans-serif;max-width:620px;"
            "margin:80px auto;padding:0 24px;line-height:1.6;color:#111}"
            "code{background:#eee;padding:2px 6px;border-radius:4px}"
            ".ok{color:#1a7f37;font-weight:700}</style>"
            "<p class=ok>Form received locally.</p><h1>%s</h1>"
            "<p>The submission was printed to the terminal running the dev server.</p>"
            "<p>This is the <strong>local stand-in</strong> for Netlify Forms. On the "
            "deployed site Netlify handles this POST and the submission appears under "
            "<code>Forms</code> in the Netlify dashboard.</p>"
            "<p><a href='/'>Back to the site</a></p>" % name
        ).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4173
    print("serving %s on http://127.0.0.1:%d/  (POST enabled, caching off)" % (root, port), flush=True)
    ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
