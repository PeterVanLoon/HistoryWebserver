from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            # Objective 3 Step 2 - Create /restaurants/new page
            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Make a New Restaurant</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/restaurants/new'>"
                output += "<input name = 'newRestaurantName' type = 'text' placeholder = 'New Restaurant Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></html></body>"
                self.wfile.write(output.encode())
                return

            if self.path.endswith("/restaurants"):
                restaurants = session.query(Restaurant).all()
                print ("This is before I print out restaurants")
                print (restaurants) 
                print ("this is after")
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "Is this working?"                
                output += "<html><body>"
                print ("one")
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br></br>"
                output += "It does seem to work"   
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return            




            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>&#161Hola! <a href = '/hello' >Back to Hello</a></body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                self.wfile.write(output.encode())
                print (output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(303)
            self.send_header('Content-type', 'text/html')
            print ("one")
            self.end_headers()
            print ("two")
            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            print ("three")
            #pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            if ctype == 'multipart/form-data':    # Compare this line with your code - form data -> form-data
                fields = cgi.parse_multipart(self.rfile, pdict)    # Compare this line with your code - self, rfile -> self.rfile
                messagecontent = fields.get('message')
            print ("four")
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this you fools?:</h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What should I say?</h2><input name='message'type='text' ><input type='submit' value='Submit'></form>"
            output += "</body></html>"
            self.wfile.write(output.encode())
            print (output)
        except:
            pass

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webserverHandler)
        print ("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()