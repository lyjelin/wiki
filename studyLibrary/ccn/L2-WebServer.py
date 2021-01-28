#!/usr/bin/python3

import socket
import sys
from email.utils import formatdate
import os

def main(argv):
    # get port number from argv
    if len(argv) == 2:
        serverPort = int(argv[1])
    else:
        serverPort = 12345
   
    # create socket and bind
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sockfd.bind(('', serverPort))
    except socket.error as emsg:
        print("Socket bind error: ", emsg)
        sys.exit(1)
    
    sockfd.listen(5)
    
    print("The server is ready to receive")
    
    while True:
        
        # accept new connection
        try:
            conn, addr = sockfd.accept()
        except socket.error as emsg:
            print("Socket accpt error: ", emsg)
            sys.exit(1)
        
        # receive the HTTP request from client
        try:
            request = conn.recv(1000).decode("ascii")
        except socket.error as emsg:
            print("Socket recv error: ", emsg)
            sys.exit(1)
        
        print("Request received: \n" + request)
        
        # use Python string split function to retrieve requested file name
        req_list = request.split(' ')
        fname = (req_list[1].split('/'))[1]
        
        #use the getsize function in the os.path module to get the requested file's size (https://docs.python.org/3/library/os.path.html)
        try:
            fsize = int(os.path.getsize(fname))
        except OSError :
            print("Path '%s' does not exists or is inaccessible" %fname)
            sys.exit(1)
                
        print("length:", fsize)
        
        cur_date = formatdate(timeval=None, localtime=False, usegmt=True)
        response="HTTP/1.1 200 OK\r\n"
        response+="Date: "+cur_date+"\r\n" 
        response+="Server: Apache/2.4.41 (Ubuntu)\r\n"
        response+="Last-Modified: Wed, 12 Aug 2020 02:38:00 GMT\r\n"
        response+="Keep-Alive: timeout=10, max=100"
        response+="Connection: keep-alive\r\n"
        response+="Content-Type: text/html; charset=utf-8\r\n"
        response+="Content-Length: {}\r\n".format(fsize)
        response+="\r\n" 
        
        #send the above response message header part to client
        try:
            conn.send(response.encode("ascii"))
        except socket.error as emsg:
            print("Socket send error: ", emsg)
            sys.exit(1)
        
        #read the requested file and send file content to client       
        try:
            fd = open(fname, 'rb')
        except IOerror as emsg:
            print("File open error: ", emsg)
            sys.exit(1)
        
            
        remaining = fsize
        while remaining > 0:
            
            smsg = fd.read(1000)
            mlen = len(smsg) 
            if mlen == 0:
                print("EOF is reached, but I still have %d to read !!!" % remaining)
                sys.exit(1)
            try:
                conn.sendall(smsg)
            except socket.error as emsg:
                print("Socket sendall error: ", emsg)
                sys.exit(1)
                
                
            remaining -= mlen
            
            
        print("[Response Sent]")
        fd.close()
        conn.close()
        
    sockfd.close()
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 WebServer.py <Server_port>")
        sys.exit(1)
    main(sys.argv)
