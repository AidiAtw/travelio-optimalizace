"""Jednoduchý lokální HTTP server pro web Travelio.

Spuštění:  python server.py
Adresa:    http://localhost:8000
"""

import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))

# Doba platnosti cache v sekundách podle typu souboru
CACHE_RULES = {
    ".css": 600,       # 10 minut
    ".js": 600,        # 10 minut
    ".png": 86400,     # 1 den
    ".jpg": 86400,
    ".jpeg": 86400,
    ".webp": 86400,
    ".avif": 86400,
    ".svg": 86400,
}


class TravelioHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".avif": "image/avif",
        ".svg": "image/svg+xml",
    }

    def end_headers(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        ext = os.path.splitext(path)[1].lower()

        if ext in CACHE_RULES:
            self.send_header("Cache-Control", f"public, max-age={CACHE_RULES[ext]}")
        else:
            # HTML stránky se vždy ověřují u serveru
            self.send_header("Cache-Control", "no-cache")

        super().end_headers()


def main():
    handler = partial(TravelioHandler, directory=ROOT)
    with ThreadingHTTPServer(("", PORT), handler) as server:
        print(f"Server běží na http://localhost:{PORT}  (ukončení: Ctrl+C)")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer ukončen.")


if __name__ == "__main__":
    main()
