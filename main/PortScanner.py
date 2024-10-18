
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from SocketTcp import SocketTcp

class PortScanner:

    #Initiate the port scanner with all parameter needed
    def __init__(self,host, start_port, end_port):
    
        self.__range_ports = range(start_port, end_port + 1)
        self.__host = host
        self.__socket_list = [SocketTcp]
        self.__ports_open = []
        self.__socket_list = [SocketTcp(self.__host, port) for port in self.__range_ports]

    
    # Function who scan only 1 socket
    def scan_tcp_port(self,tcp_socket: SocketTcp):
        try:
            tcp_socket.connexion()
            
        except socket.error as e:
             print(f"Exception caught: {e}")

        

    # Function who scan multiple socket at the same time with the ThreadPoolExecutor 
    def scan_ports(self):

        with ThreadPoolExecutor(max_workers=100) as executor:
             executor.map(lambda tcp_socket: self.scan_tcp_port(tcp_socket), self.__socket_list)
        self.__ports_open = [ item.get_port() for item in self.__socket_list if item.isOpen()]
    
   

    #Display the result
    def display(self):
        
        print("\033[1;34m{:<18} {:<10} {:<10}\033[0m".format("IP", "Port", "Open"))
        print("=" * 40)

        for i, tcp_socket in enumerate(self.__socket_list):
            if tcp_socket.isOpen():
                print("\033[1;31m{:<18} {:<10} {:<10}\033[0m".format(tcp_socket.get_ip(), tcp_socket.get_port(), "True"))
            else:
                print("\033[1;34m{:<18} {:<10} {:<10}\033[0m".format(tcp_socket.get_ip(), tcp_socket.get_port() , "False"))
        
        print(f"Open ports = {self.__ports_open}" )
    
    
    
    #Create a log file
    def create_log_file(self):
        
        file_name = str(datetime.now())
        
        try:
            with open(file_name, 'w') as file:
                file.write(f"{file_name}\n")
                file.write("Ip Adresses-------Port---------Open\n")
                file.write("**************************************\n")
                
                for tcp_socket in self.__socket_list:
                    file.write(f"{tcp_socket.get_ip()}-------{tcp_socket.get_port()}-----------{tcp_socket.isOpen()}\n")
                    
        except PermissionError:
            print("You dont have permission to create this file")
            raise
    
        print("File log file created") 
           



