mport http.server, socketserver

class server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(open('../script/index.html','rb').read()))
            self.end_headers()
            self.wfile.write(open('../script/index.html','rb').read())
        
        if self.path == '/main.js':
            self.send_response(200)
            self.send_header('Content-Type', 'javascript/js; charset=utf-8')
            self.send_header('Content-Length', len(open('../script/js/main.js','rb').read()))
            self.end_headers()
            self.wfile.write(open('../script/js/main.js','rb').read())
        if self.path == '/design.css':
            self.send_response(200)
            self.send_header('Content-Type', 'text/css; charset=utf-8')
            self.send_header('Content-Length', len(open('../script/css/design.css','rb').read()))
            self.end_headers()
            self.wfile.write(open('../script/css/design.css','rb').read())

    
    def do_POST(self):
        html = "Все ок\n"
        if ( self.path == '/regist' ) :
            l = int(self.headers.get('Content-Length'))
            l = self.rfile.read(l)
            print(l.decode())
            if ( l == '[' ) :
                self.send_response(200)
                self.send_header('Content-Type', 'javascript/js; charset=utf-8')
                self.send_header('Content-Length', len(html))
                self.end_headers()
                self.wfile.write(html.encode())
            else :
                self.send_response(302)
                self.send_header('Location', '/')
                self.end_headers()


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

if __name__ == '__main__':
    ThreadingHTTPServer(('', 17957), server).serve_forever()
