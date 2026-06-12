from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>EcoVerde - Produccion</h1>")
        self.wfile.write(b"<p>Aplicacion ejecutandose correctamente.</p>")

PORT = 8080

print(f"Servidor iniciado en puerto {PORT}")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()