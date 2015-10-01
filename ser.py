from http.server import HTTPServer, CGIHTTPRequestHandler

class Handler(CGIHTTPRequestHandler):
        cgi_directories = ["/cgi-bin"]

        PORT = 9999

        httpd = HTTPServer(("", PORT), Handler)
        print("serving at port", PORT)
        httpd.serve_forever()
