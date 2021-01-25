import socket, pickle

HOST = 'localhost'
HOST105 = '192.168.1.105'
PORT = 56772

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST105, PORT))

s.listen(1)

conn, addr = s.accept()
print(f"Connect by {addr}")

while True:
    data = conn.recv(4096)
    if len(data) > 0:
        data_variable = pickle.loads(data)
        conn.close()
        break
    
print(data_variable)
print("data received from client")