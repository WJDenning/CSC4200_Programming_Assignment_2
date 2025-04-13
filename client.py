import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

def start_client():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	print(f"Connected to server at {HOST}:{PORT}, type your message.")
	print("Type 'exit' to disconnect.")

	while True:
		message = input("> ")
		if message.lower() == "exit":
			break
		client.send(message.encode())

		acknowledgement = client.recv(1024)
		print(f"Server: {acknowledgement}")

	client.close()
	print("Disconnected from the server.")

start_client()
