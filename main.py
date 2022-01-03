from http.server import BaseHTTPRequestHandler, HTTPServer
from sensor_gas import setup_gas_sensor, cleanup_gas_sensor

host_name = "localhost"
server_port = 8080


class MetricsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    setup_gas_sensor()
    webServer = HTTPServer((host_name, server_port), MetricsServer)
    print(f"Server started http://{host_name}:{server_port}")

    try:
        webServer.serve_forever()
    finally:
        cleanup_gas_sensor()

    webServer.server_close()
    print("Server stopped.")

