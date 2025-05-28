import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from src.service.query_service import consultar_propiedades

class QueryController(BaseHTTPRequestHandler):
    def _send_response(self, status, data):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, default=str).encode('utf-8'))

    def do_POST(self):
        # Alternativamente, permite filtros vía POST JSON
        if self.path == "/propiedades":
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                filtros = json.loads(post_data.decode())
            except Exception:
                return self._send_response(400, {"error": "JSON inválido"})
            resultado = consultar_propiedades(filtros)
            return self._send_response(200, resultado)
        else:
            self._send_response(404, {"error": "Ruta no encontrada"})

