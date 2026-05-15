import os
import json
from models.connection import Connection
from services.firewall import Firewall

firewall = Firewall() 

incoming_connections = [
    Connection("192.168.1.50", 443, "HTTPS"),
    Connection("10.0.0.12", 80, "HTTP"),
    Connection("172.16.254.1", 53, "DNS"),

    Connection("185.220.101.45", 22, "SSH"),
    Connection("103.203.57.1", 3389, "RDP"),
    Connection("92.118.160.5", 23, "TELNET"),

    Connection("190.2.144.66", 445, "SMB"),
    Connection("45.141.157.20", 21, "FTP"),
    Connection("104.248.14.50", 25, "SMTP"),

    Connection("8.8.8.8", 443, "HTTPS"),
    Connection("1.1.1.1", 53, "DNS"),
    Connection("66.240.192.138", 8080, "HTTP"),

    Connection("89.248.165.74", 3306, "MYSQL"),
    Connection("222.186.30.112", 5432, "POSTGRES"),
    Connection("5.188.206.26", 5900, "VNC")
]
for connection in incoming_connections:

    firewall.verify_connection(connection)
