from PortScanner import PortScanner

def main():
    scanner = PortScanner("192.168.1.49", 800,900)
    scanner.scan_ports()
    scanner.display()
    
   

if __name__ == "__main__":
    main()
