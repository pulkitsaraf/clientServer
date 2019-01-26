import socket
# get name of local machine
s = socket.socket()                     
host = socket.gethostname()              
# add a port number to connect
port = 7344                             
s = socket.socket()
s.bind((host, port))                     
s.listen(5)                              
#get connection from a client
connection, address = s.accept()
print('Got connection from ', address[0], '(', address[1], ')')
#recieve data
while True:
    data = connection.recv(1024)
    print(data.decode("utf-8"))
    if not data: 
        break
    connection.sendall(data)
#close connection
connection.close() 

print('Data Recieved from client')