from services.intrusion_detector import IntrusionDetector
class Firewall:

    def __init__(self):
      
      self.trusted_ips = {
          
            "192.168.1.50",
            "10.0.0.12",
            "172.16.254.1"
      
      }

      self.detector = IntrusionDetector()

    def verify_connection(self, connection):

       if connection.ip in self.trusted_ips:
         
         connection.status = "ALLOWED"

         print(f"[ALLOWED] {connection.ip}") 

       else:
 
          connection.status = "BLOCKED"
          
          print(f"[BLOCKED] {connection.ip} - Untrusted IP")


          self.detector.annalyze_connection(connection)  