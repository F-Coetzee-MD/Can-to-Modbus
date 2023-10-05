import json
import socket

settings = json.load(open("settings.json", "r"))

# Server IP address and port
server_ip = settings["plc ip"]  
server_port = settings["plc port"] 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_tcp_server():
  client_socket.connect((server_ip, server_port))
  return 0

def close_tcp_connection():
  # Close the socket
  client_socket.close()

def send_message_to_plc():
  message = "";
  client_socket.send(message.encode())
  return 0