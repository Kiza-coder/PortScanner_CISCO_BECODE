from PortScanner import PortScanner
from InputValidator import *


def main():

    validator = InputValidator()
    try:
        host = input("Enter the host IP to scan): ")
        validator.validate_ip(host)
        start_port = int(input("Enter the starting port number: "))
        end_port = int(input("Enter the ending port number: "))
        validator.validate_range(start_port,end_port)
        scanner = PortScanner(host, start_port,end_port)
        scanner.scan_ports()
        scanner.display()
        scanner.create_log_file()
            
    except InvalidInputError as ex:
        print(f"Exception caught : {ex}" )
        
    except PermissionError as ex:
        print(f"Exception caught : {ex}")

if __name__ == "__main__":
    main()
