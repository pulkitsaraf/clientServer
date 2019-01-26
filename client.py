import socket                           # Import socket module
# get name of local machine
host = socket.gethostname()          
# add a port number to connect
port = 7344                        
connection = socket.socket()                  
#create connection
connection.connect((host, port))

connection.sendall(b'Connected. Wait for data...') 
#send message
intosend = input("Send a Message:")
connection.sendall(bytes(intosend, 'utf-8')) 

data = connection.recv(1024)
intosend= "no"

while intosend != "quit":
    intosend = input("Send a Message:")
    conn.sendall(bytes(intosend, 'utf-8'))


#close connection
connection.close()                                    # Close the socket when done


print(data.decode("utf-8"))