from datetime import datetime

class Connection:

    def __init__(self,ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol

        self.timestamp = datetime.now()

        self.status = "PENDING"