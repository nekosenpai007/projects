# Basic Network Connectivity & Socket Test (Python)
This project demonstrates two simple but important networking tests in Python:
1. Low-level socket connection test
2. Basic internet connectivity check
These scripts are useful for beginners learning networking, penetration testing fundamentals, or validating network access before running advanced tools.

## Requirements
Python 3.x
Active internet connection
No external libraries required (uses Python standard library only)

# 1. Socket Connection Test

This script creates a raw TCP socket and connects to httpbin.org on port 80.
It sends a manual HTTP GET request and prints the raw HTTP response from the server.
This helps you understand:
- How sockets work at a low level
- How HTTP requests look internally
- Whether outbound TCP connections are allowed

# 2. Internet Connectivity Test
## Description
This script checks basic internet access by attempting to open Google’s website using urllib.
It is useful for:
- Verifying internet access before running network tools
- Debugging proxy/firewall issues
- Quick connectivity health check


**Author**
Black hat python
