import http.server, socketserver, json
import request_bd


#bd = request_bd.bd_user('user.bd', "USER")

class server(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.send_response(200)
			self.send_header('Content-Type', 'text/html; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/mainpage.html','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/mainpage.html','rb').read())
		if self.path == '/signup.html':
			self.send_response(200)
			self.send_header('Content-Type', 'text/html; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/signup.html','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/signup.html','rb').read())
		if self.path == '/main.js':
			self.send_response(200)
			self.send_header('Content-Type', 'text/javascript; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/js/main.js','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/js/main.js','rb').read())
		if self.path == '/design.css':
			self.send_response(200)
			self.send_header('Content-Type', 'text/css; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/css/design.css','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/css/design.css','rb').read())
		if self.path == '/mainpage.css':
			self.send_response(200)
			self.send_header('Content-Type', 'text/css; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/css/mainpage.css','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/css/mainpage.css','rb').read())
		if self.path == '/mainpage.js':
			self.send_response(200)
			self.send_header('Content-Type', 'text/javascript; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/js/mainpage.js','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/js/mainpage.js','rb').read())
		if self.path == '/signin.js':
			self.send_response(200)
			self.send_header('Content-Type', 'text/javascript; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/js/signin.js','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/js/signin.js','rb').read())
		if self.path == '/signin.html':
			self.send_response(200)
			self.send_header('Content-Type', 'text/html; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/signin.html','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/signin.html','rb').read())
		if self.path == '/paper.jpg':
			self.send_response(200)
			self.send_header('Content-Type', 'image/jpg; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/css/paper.jpg','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/css/paper.jpg','rb').read())
		if self.path == '/back-reg.jpg':
			self.send_response(200)
			self.send_header('Content-Type', 'image/jpg; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/css/back-reg.jpg','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/css/back-reg.jpg','rb').read())
		if self.path == '/list-check.png':
			self.send_response(200)
			self.send_header('Content-Type', 'image/png; charset=utf-8')
			self.send_header('Content-Length', len(open('../script/css/list-check.png','rb').read()))
			self.end_headers()
			self.wfile.write(open('../script/css/list-check.png','rb').read())
	

    def do_POST(self):
        bd = request_bd.bd_user('user.bd', "USER")
        #    if self.path == '/regist' :
        l = int(self.headers.get('Content-Length'))
        l = self.rfile.read(l)
        print(l)
        l = json.loads(l)
        if ( not(bd.add_user(1, l['login'], l['password']))) :
            html = "Error"
            self.send_response(500)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(html))
            self.end_headers()
            self.wfile.write(html.encode())
            print("Error")
        else :
            self.send_response(200)
            self.send_header('Location', '/')
            self.end_headers()


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
	pass

if __name__ == '__main__':
	ThreadingHTTPServer(('', 17957), server).serve_forever()
