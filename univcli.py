import socket
#import msvcrt
import sys

if sys.platform[:3] == 'win':
    import msvcrt
    def getkey():
        key = msvcrt.getch()
        if ord(key) == 224: #catch second event with arrow keys
            key = msvcrt.getch()
        return key
else : #sys.platform[:3] == 'lin':
    import termios, sys, os
    TERMIOS = termios

    def getkey():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
        new[6][TERMIOS.VMIN] = 1
        new[6][TERMIOS.VTIME] = 0
        termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
        c = None
        try:
            c = os.read(fd, 1)
        finally:
            termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
        return c

def Main():
    hostname=socket.gethostname()
    host=socket.gethostbyname(hostname)
    #host = '192.168.0.110'
    port = 5001
    print('Your Computer Name is:'+hostname)
    print('Your IP address is:'+host)
    serveraddr=raw_input('Inserire IP del server: ')

    #server = ('192.168.0.111',5000)
    server = (serveraddr,5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    #message = msvcrt.getch()
    message=''
    message = getkey().decode()
    #print (str(message))
    while message != 'x':
        print message
        message=str(message)
        #print message.decode()
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        data=str(data)
        print 'Received from server: ' + str(data)
        #message = msvcrt.getch()
        message = getkey().decode()
    s.close()

if __name__ == '__main__':
    Main()
