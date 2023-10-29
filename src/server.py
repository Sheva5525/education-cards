import http.server, socketserver

class server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(open(self.pwd + '../skrip/index.html','rb').read()))
            self.end_headers()
            self.wfile.write(open(self.pwd + '../skrip/index.html','rb').read())
        
        if self.path == '/main.js':
            self.send_response(200)
            self.send_header('Content-Type', 'javascript/js; charset=utf-8')
            self.send_header('Content-Length', len(open(self.pwd + '../skrip/js/index.html','rb').read()))
            self.end_headers()
            self.wfile.write(open(self.pwd + '../skrip/js/main.js','rb').read())

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

if __name__ == '__main__':
    ThreadingHTTPServer(('', 17957), server).serve_forever()
        

