import http.server
from prometheus_client import start_http_server

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Send the success status
        self.send_response(200)
        
        # Fixed the header typo ('Content' instead of 'Conten')
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # The content we want to show
        response_text = "<h1>Success! The server is working.</h1>"
        
        # FIX: Changed .writable() to .write()
        self.wfile.write(response_text.encode("utf-8"))

if __name__ == "__main__":
    start_http_server(5001)
    # Ensure the port is an integer, not a string ('5000' -> 5000)
    server_address = ('localhost', 5000)
    server = http.server.HTTPServer(server_address, HandleRequests)
    print(f"Server running on http://{server_address[0]}:{server_address[1]}")
    server.serve_forever()