import socket

# Función para enviar una expresión al servidor
def enviar_expresion(expresion):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    client_socket.sendall(expresion.encode())
    respuesta = client_socket.recv(1024).decode()
    print(f"Respuesta del servidor: {respuesta}")
    client_socket.close()

# Menú para el cliente
while True:
    print("\nIngrese una expresión matemática o salir: ")
    expresion = input("Expresión: ")

    if expresion.lower() == 'salir':
        break

    enviar_expresion(expresion)


