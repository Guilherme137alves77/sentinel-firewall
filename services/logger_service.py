import os 
import json

class LoggerService:

    def __init__(self):
       
       self.logs_directory = "database/logs"

       self.create_logs_directory()

    def create_logs_directory(self):

        if not os.path.exists(self.logs_directory):

            os.makedirs(self.logs_directory)

    def generate_alert_report(self, connection, risk):

        report = {

            "source_ip": connection.ip,

            "port": connection.port,

            "protocol": connection.protocol,

            "timestamp": str(connection.timestamp),
            
             "risk_level": risk,

             "status": connection.status
        }

        self.save_log(connection, report)

    def save_log(self, connection, report):

        filename = (
            f"{self.logs_directory}/"
            f"alert_{connection.ip.replace('.', '_')}_{connection.port}.json" 
        )    

        with open(filename, "w") as file:

            json.dump(report, file, indent=4)