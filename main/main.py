from PortScanner import PortScanner

def main():
    scanner = PortScanner("8.8.8.8", 800,900)
    scanner.scan_ports()
    scanner.display()
    
   

if __name__ == "__main__":
    main()
