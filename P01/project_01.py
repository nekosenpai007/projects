import socket

target_host = "httpbin.org"  # Use this instead of Google
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data - FIXED: added 'b' for bytes and proper Host header
client.send(b"GET / HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")

# receive some data - FIXED: typo 'rev' to 'recv'
response = client.recv(4096)

print(response.decode())