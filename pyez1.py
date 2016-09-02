from jnpr.junos import Device
from jnpr.junos.op.phyport import *
import sys

class pyez:

    def __init__(self):
        self.__ip = ""
        self.__user = ""
        self.__passw = ""
        
    def set_device(self, ip, user, passw):
        self.__ip = ip
        self.__user = user
        self.__passw = passw
        
    def get_ports (self):
        
        try:
            # test for 3 seconds if device is reachable
            Device.auto_probe = 3

            # Instantiate a Device object
            dev = Device(host = self.__ip, user = self.__user, password = self.__passw)
            
            print 'Opening connection to ', self.__ip
            dev.open()

        #**********************EXCEPTION**********************************
        except Exception as somethingIsWrong:
            print "Unable to connect to host:", somethingIsWrong
            sys.exit(1)
        #*****************************************************************
        print "getting ports"
        ports = PhyPortTable(dev).get()

        port_list = []
        for port in ports:
            port1 = "%s" %(port.oper)
            if port1 == 'up':
                list1 = "#00ff00"
                port_list.append(list1)
            else:
                list1 = "#ff0000"
                port_list.append(list1)
        
        print "Port,Status" #Print Header for CSV
        #port_list = []
        #for port in ports:
        #      port_list.append(("%s" % (port.oper)))
        return port_list
        dev.close()
