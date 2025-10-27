#!/usr/bin/env python3
"""
Network Scanner Project
Students: [Your names here]
Date: [Date]
"""

import socket
import sys

def start_server(host, port):
    pass

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(f"The hostname is: {hostname}")
    print(f"THe IP is: {ip}")
    pass
