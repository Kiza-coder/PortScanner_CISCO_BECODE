#Class who herit from Exception
class InvalidPortRangeError(Exception):

    #super() = use the constructor from the parent class
    
    def __init__(self, start_port, end_port, message=None):
        if message is None:
            message = f"Invalid port range: start_port ({start_port}) > end_port ({end_port})"    
        super().__init__(message)
    
        