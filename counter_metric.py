import http.server
from prometheus_client import start_http_server, Counter

# Define the metric
REQUEST_COUNT = Counter("app_requests_counts", "Total HTTP Request Count")

class HandleRequests(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Increment the Prometheus counter
        REQUEST_COUNT.inc()
        
        # 1. Send Response Code
        self.send_response(200)
        
        # 2. Send Headers (Fixed: adding required arguments and end_headers)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # 3. Write Body (Fixed: added content and proper method call)
        self.wfile.write(bytes("<html><body>Hello, Prometheus!</body></html>", "utf-8"))

if __name__ == "__main__":
    # Start Prometheus metrics server on port 5001
    start_http_server(5001)
    print("Metrics available at http://localhost:5001/metrics")
    
    # Start the main app server on port 5000
    server = http.server.HTTPServer(('localhost', 5000), HandleRequests)
    print("App running at http://localhost:5000")
    server.serve_forever()