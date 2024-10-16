class SocketTcp:

    def __init__(self,ip_address,port_number):
        self.__ip_address = ip_address
        self.__port = port_number
        self.__isOpen = False 

    def get_ip(self):
        return self.__ip_address
    
    def get_port(self):
        return self.__port
    
    def isOpen(self):
        return self.__isOpen

    def set_isOpen(self,value):
        self.__isOpen = value
        
    def info(self):
        print(self.__isOpen, self.__port, self.__ip_address)
        
    
