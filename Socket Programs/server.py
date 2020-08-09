#access files remotely
# * Gain access to different directories
# * View Files
# * Download Files
# * Remove Files
# * Remove Directories
# * Send Files
# * Create Directory

import os
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
#host = '106.223.252.90'
port = 9999

s.bind((host, port))
print("")
print("Server is currently running @", host)
print("")
print("Waiting for incoming connections...")
s.listen(4)
conn, addr = s.accept()
print("")
print(addr, "Has connected to the server successfully")

#connnections has been completed

def commands():
    print("")
    print("command list.....")
    print("1> view_cwd - will show all files in the directory where the file is running")
    print("2> custom_dir - will show files from custom directory")
    print("3> downlaod_file - will download files from directory")
    print("4> remove_file - will remove files from directory")
    print("5> send_file - will send the files to another directory")
    print("6> shutdown - will shutdown the system")
    print("6> exit - will break the connection")
    
#command handling

while 1:
    commands()
    print("")
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent, waiting for  connections...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)
     
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir : "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result : ", files)
        
    elif command == "download_file":
        conn.send(command.encode())
        print("")
        filepath = input(str("Please enter the file path including the filename"))
        print("")
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("Please enter a filename for the incoming file with extension : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, " has been downloaded and saved")
        print("")
     
    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("Please enter the filename and directory : "))
        conn.send(fileanddir.encode())
        print("")
        print("Command has been executed successfully: File Removed")
        print("")
        
    elif command == "send_file":
        conn.send(command.encode())
        print("")
        file = input(str("Please enter the filename and directory: "))
        print("")
        filename = input(str("Please enter the filename for the file being sent: "))
        data = open(file, "rb")
        file_data = data.read(1000000000)     #Change when the file is big
        conn.send(filename.encode())
        print(file, " has been sent successfully")
        conn.send(file_data)
        
    elif command == "shutdown":
        conn.send(command.encode())
        
    elif command == "exit":
        conn.send(command.encode())
        sys.exit()
     
    else:
        print("")
        print("Command not recognized")