"""Mini server web per provare TamaPixel.

  Solo su questo PC:                  python serve.py
  Anche dall'iPhone (stesso Wi-Fi):   python serve.py --lan
"""
import argparse
import functools
import http.server
import socket
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        '.webmanifest': 'application/manifest+json',
        '.js': 'text/javascript',
    }

    def end_headers(self):
        # Niente cache: ogni modifica ai file si vede subito ricaricando la pagina
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()


def lan_ip():
    # Scopre l'indirizzo del PC nella rete Wi-Fi (non invia nessun dato)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(('10.255.255.255', 1))
            return s.getsockname()[0]
        except OSError:
            return None


def main():
    parser = argparse.ArgumentParser(description='Mini server per TamaPixel')
    parser.add_argument('--port', type=int, default=8123)
    parser.add_argument('--lan', action='store_true', help='visibile anche agli altri dispositivi del Wi-Fi')
    args = parser.parse_args()

    host = '0.0.0.0' if args.lan else '127.0.0.1'
    handler = functools.partial(Handler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer((host, args.port), handler) as httpd:
        print(f'TamaPixel è acceso: http://localhost:{args.port}/', flush=True)
        if args.lan:
            ip = lan_ip()
            print(f"Dall'iPhone apri con Safari: http://{ip}:{args.port}/" if ip else "Non trovo l'indirizzo del PC nella rete.", flush=True)
        print('Premi Ctrl+C per spegnerlo.', flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
