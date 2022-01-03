import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from sensor_gas import SensorGas

host_name = "localhost"
server_port = 8080
sensors = []


class MetricsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        for sensor in sensors:
            label, value = sensor.metric_data()
            self.wfile.write(bytes(f"utility_sensor{{type={label}}} {value}", "utf-8"))


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    sensors = [SensorGas()]
    server = HTTPServer((host_name, server_port), MetricsServer)
    logging.info(f"Server started http://{host_name}:{server_port}")

    try:
        server.serve_forever()
    finally:
        for sensor in sensors:
            sensor.cleanup()

    server.server_close()
    logging.info("Server stopped.")

