import cherrypy
from jinja2 import Environment,FileSystemLoader
from jnpr.junos import Device
from jnpr.junos.op.phyport import *
import sys
hostIP = '192.168.10.10'
try:
    # test for 3 seconds if device is reachable
    Device.auto_probe = 3

    # Instantiate a Device object
    dev = Device(host = hostIP, user = 'lab', password = 'lab123')
    print 'Opening connection to ', hostIP
    dev.open()

#**********************EXCEPTION**********************************
except Exception as somethingIsWrong:
    print "Unable to connect to host:", somethingIsWrong
    sys.exit(1)
#*****************************************************************

ports = PhyPortTable(dev).get()
mList=[]
print "Port,Status,Flapped" #Print Header for CSV
for port in ports:
        port1 = "%s" %(port.oper)
        if port1 == 'up':
            list1 = "#00ff00"
            mList.append(list1)
        else:
            list1 = "#ff0000"
            mList.append(list1)

print(mList)
dev.close()
env = Environment(loader=FileSystemLoader('templates'))
class Root: 
	@cherrypy.expose 
	def index(self): 
		tmpl = env.get_template('index.html') 
		return tmpl.render(salutation='LAB',target = 'DASHBOARD',myList = mList,)
cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8080,})
cherrypy.quickstart(Root())
