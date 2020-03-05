import socket
import time
import sys

sys.path.append('generator')
from generator.synthetic import SyntheticDataGenerator, giveMeMyData

# Change ip address if you are starting server from
# different network
ip = "172.20.10.3"
const_connection_close_command = "Stop"

# Server socket configuration
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9999
host = socket.gethostname()

print("Server started running..")
print("Host : %s\nPort : %s" % (host, port))

server_socket.bind((ip, port))
server_socket.listen(5)

client_socket, address = server_socket.accept()
print("Got a connection from %s" % str(address))

# Test if we can receive any information its OK.
request = client_socket.recv(1024).decode()

if not ',' in request:
    print("Wrong request format.\nServer stopped running..")
    client_socket.send(const_connection_close_command.encode('ascii'))
    client_socket.close()
    server_socket.close()
    sys.exit()

mission, code = request.split(",")
if mission == "generate" and code == "666":
    # Start generating data.
    # generator = SyntheticDataGenerator()    
    # generator.medium_generator_engine(data)
    # synhtetic_generator = SyntheticDataGenerator()
    # synhtetic_generator.basic_generator_engine()

    data = ""
    while data != const_connection_close_command:

        # Send information to client here.
        # You will send AI response here.
        mod_res = giveMeMyData()
        start_time_ms = time.time()
        for j,i in enumerate(mod_res):
            print(j+1,i)
            if i == 'RightLeg':
                client_socket.send(str(i+"\n").encode('ascii'))
                computed_time = time.time() - start_time_ms
                a = "Index,"+str(j+1)+"," + str(computed_time)+"\n"
                client_socket.send(a.encode('ascii'))
                print("Hunger Loop Completed..")
                print("Server stops running..")
                data = const_connection_close_command
                break
            client_socket.send(str(i+"\n").encode('ascii'))
            time.sleep(0.05)

        # data = input("Send Message to Client : ")
        # client_socket.send(str(data+"\n").encode('ascii'))

    client_socket.close()


print("Server stopped running..")
server_socket.close()

