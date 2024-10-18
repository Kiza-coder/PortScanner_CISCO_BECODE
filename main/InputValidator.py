import re

class InvalidInputError(Exception):
    
    def __init__(self, message="Entrée invalide"):
        self.message = message
        super().__init__(self.message)

class InputValidator:
    
   
    ipv4_regex = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    

    @staticmethod
    def validate_ip(ip_address):
        if not InputValidator.ipv4_regex.match(ip_address):
            raise InvalidInputError(f"L'adresse IP '{ip_address}' est invalide")
        return True
    
    @staticmethod
    def validate_range(start_port,end_port):
        if start_port > end_port :
            raise InvalidInputError(f"Invalid port range: start_port ({start_port}) > end_port ({end_port})")
        if start_port < 0 or end_port < 0:
            raise InvalidInputError("Ports can't be negatif")
        if start_port > 65535 or end_port > 65535:
            raise InvalidInputError("Ports can't exceed 65535")


