#readhtml
#Program uses CherryPy to serve an html-file
#Auth: CTE
import cherrypy
with open('table.html', 'r') as f:
	read_data = f.read()
	f.close()

class HelloWorld():
	@cherrypy.expose
	def index(self):
		return read_data
	index.exposed = True
cherrypy.quickstart(HelloWorld())
