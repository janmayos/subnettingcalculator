import socket

mi_socket = socket.socket()

mi_socket.connect(("localhost",8000))
mi_socket.send(bytes("Hola deesde el cliente!", 'utf-8'))
respuesta = mi_socket.recv(1024)

print(respuesta.decode('utf-8'))
mi_socket.close()