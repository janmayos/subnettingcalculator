import socket

mi_socket = socket.socket()
mi_socket.bind(("localhost",8000))
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexión establecida!")
    print(addr)

    conexion.send(bytes("Hola soy el server", 'utf-8'))
    conexion.close()