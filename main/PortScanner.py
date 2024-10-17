
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from SocketTcp import SocketTcp
from InvalidPortRangeError import InvalidPortRangeError

class PortScanner:

    #Initiate the port scanner with all parameter needed
    def __init__(self,host, start_port, end_port):
        
        #Test the range port
        if start_port > end_port :
            raise InvalidPortRangeError(start_port,end_port)
        if start_port < 0 or end_port < 0:
            raise InvalidPortRangeError(start_port,end_port,"Ports can't be negatif")

        self.__range_ports = range(start_port, end_port + 1)
        self.__host = host
        self.__socket_list = [SocketTcp]
        self.__ip = None

        #Try to resolve Ip adress
        try:
            self.__ip = socket.gethostbyname(self.__host)
            print(f"Resolved {self.__host} to {self.__ip}")
        except socket.gaierror:
            print(f"Error: Could not resolve host :  {self.__host}")
            raise
        
        self.__socket_list = [SocketTcp(self.__ip, port) for port in self.__range_ports]
   

    
    
    # Function who scan only 1 socket
    def scan_tcp_port(self,tcp_socket: SocketTcp):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            try:
                sock.settimeout(1)  # 1 second timeout for each connection attempt
                result = sock.connect_ex((tcp_socket.get_ip(), tcp_socket.get_port()))  # 0 if the connection succeeds

                if result == 0:
                    tcp_socket.set_isOpen(True)

            except socket.error as e:
                return f"Error scanning port {tcp_socket.port}: {e}"
        


    # Function who scan multiple socket at the same time with the ThreadPoolExecutor
    def scan_ports(self):
        
        with ThreadPoolExecutor(max_workers=100) as executor:
             executor.map(lambda tcp_socket: self.scan_tcp_port(tcp_socket), self.__socket_list)


    #Display the result
    def display(self):
        
        print("\033[1;34m{:<18} {:<10} {:<10}\033[0m".format("IP", "Port", "Open"))
        print("=" * 40)

        for i, tcp_socket in enumerate(self.__socket_list):
            if tcp_socket.isOpen():
                print("\033[{1;31m:<18} {:<10} {:<10}\033[0m".format(tcp_socket.get_ip(), tcp_socket.get_port() , "True"))
            else:
                print("\033[1;34m{:<18} {:<10} {:<10}\033[0m".format(tcp_socket.get_ip(), tcp_socket.get_port() , "False"))
    
    
    def create_log_file(self):
        
        file_name = str(datetime.now().date())
        
        with open(file_name, 'w') as file:
            
            file.write("Ip Adresses-------Port---------Open\n")
            file.write("**************************************\n")
            
            for tcp_socket in self.__socket_list:
                file.write(f"{tcp_socket.get_ip()}-------{tcp_socket.get_port()}-----------{tcp_socket.isOpen()}\n")
        
        print("File log file created") 
           



