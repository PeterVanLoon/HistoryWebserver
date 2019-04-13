def do_POST(self):
        try:
            self.send_response(301)  # Compare this line with your code
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.get('Content-type'))  # Compare this line with your code - getheader -> get
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")  # This is new
            if ctype == 'multipart/form-data':    # Compare this line with your code - form data -> form-data
                fields = cgi.parse_multipart(self.rfile, pdict)    # Compare this line with your code - self, rfile -> self.rfile
                messagecontent = fields.get('message')
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this you fools?:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0].decode()
            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output.encode('utf-8'))  # Compare this line with your code
            print (output)
        except:
            pass