import cherrypy
from jinja2 import Environment,FileSystemLoader
from collections import defaultdict
import sys
import pyez1
import cherry

ips = ["192.168.10.128", "192.168.10.129"]
user = "fck"
passw = "junos1"

def main():

    data = pyez1.pyez()
    status_port = []
    
    for ip in ips:
        values = data.set_device(ip, user, passw)
        eth_port = data.get_ports()
        status_port.append(eth_port)        
    print status_port

    env = Environment(loader=FileSystemLoader('templates'))
    class Root: 
            @cherrypy.expose 
            def index(self): 
                    tmpl = env.get_template('index.html')        
                    return tmpl.render(myList = status_port)
    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8080,})
    cherrypy.quickstart(Root())
  
main()
