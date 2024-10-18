from PortScanner import PortScanner
from InvalidPortRangeError import InvalidPortRangeError

def main():

    host = input("Enter the host to scan (IP or domain): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    
    try:
        scanner = PortScanner(host, start_port,end_port)
        scanner.scan_ports()
        scanner.display()
        scanner.create_log_file()
            
    except InvalidPortRangeError as ex:
        print(f"Exception caught : {ex}" )
        
    except PermissionError as ex:
        print(f"Exception caught : {ex}")

if __name__ == "__main__":
    main()
