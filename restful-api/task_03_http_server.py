#!/usr/bin/python3
"""A basic API implemented using Python's standard HTTP server."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlsplit


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Serve a few simple GET endpoints."""

    def send_body(self, status, body, content_type="text/plain; charset=utf-8"):
        """Write a complete HTTP response."""
        content = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        """Handle GET /, /data, /status, and /info."""
        path = urlsplit(self.path).path
        if path == "/":
            self.send_body(200, "Hello, this is a simple API!")
        elif path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_body(200, json.dumps(data), "application/json")
        elif path == "/status":
            self.send_body(200, "OK")
        elif path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_body(200, json.dumps(info), "application/json")
        else:
            self.send_body(404, "Endpoint not found")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), SimpleAPIHandler)
    print("API running on http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
