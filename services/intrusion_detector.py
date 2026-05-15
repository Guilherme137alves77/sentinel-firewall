from services.logger_service import LoggerService
class IntrusionDetector:

    def __init__(self):

      self.logger = LoggerService()


      self.blacklist = {
            "185.220.101.45",
            "92.118.160.5",
            "190.2.144.66",
            "45.141.157.20",
            "222.186.30.112"
            }

      self.dangerous_ports = {
          
            21: "FTP",
            22: "SSH",
            23: "TELNET",
            3389: "RDP",
            445: "SMB",
            5900: "VNC"

      }

    def annalyze_connection(self, connection):

        self.detect_blacklist_ip(connection)

        self.detect_dangerous_port(connection)

    def detect_blacklist_ip(self, connection):   
        if connection.ip in self.blacklist:

           print(
              f"[WARNING] Blacklisted IP detected: "
              f"{connection.ip}"
           ) 
           connection.status = "BLOCKED"

           self.logger.generate_alert_report(
              connection,
              "CRITICAL"
           )

    def detect_dangerous_port(self, connection):
        
        if connection.port in self.dangerous_ports:

           protocol = self.dangerous_ports[connection.port]

           print(
              f"[WARNING] Dargerous port detected: "
              f"{connection.port} ({protocol})"
           )   
        
        connection.status = "BLOCKED"

        self.logger.generate_alert_report(
           connection,
           "HIGH"
        )