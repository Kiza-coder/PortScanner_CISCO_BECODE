import socket
class SocketTcp:

    def __init__(self,ip_address,port_number):
        self.__ip_address = ip_address
        self.__port = port_number
        self.__isOpen = False 

    def connexion(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.settimeout(1)  # 1 second timeout for each connection attempt
                result = sock.connect_ex((self.__ip_address, self.__port))  # 0 if the connection succeeds
                if result == 0:
                    self.set_isOpen(True)

            except OSError:
                return f"Error scanning port {self.__port}"
            

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
        
    
