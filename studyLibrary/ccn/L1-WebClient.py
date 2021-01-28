#!/usr/bin/python3

import socket
import sys


def get_content_length(msg):
    print("Response header received: \n" + msg)
    
    response_headers = {}
    
    #retrieve response header part
    space_line_index = msg.index("\r\n\r\n")
    response_header = msg[0: space_line_index]
    
    for index, header in enumerate(response_header.split("\r\n")):
        #retrieve each header line
        if index > 0: 
            key = header.split(':')[0]
            value = header.lstrip(key).lstrip(':')
            key = key.strip(' ').lower()
            value = value.strip(' ')
            response_headers[key] = value

    if "content-length" in response_headers.keys():
        content_length = int(response_headers['content-length'])
        return content_length
    else:
    	return 0


def main(argv):

	# create socket and connect to server
	try:
		sockfd = socket.socket()
		sockfd.connect((argv[1], int(argv[2])))
	except socket.error as emsg:
		print("Socket error: ", emsg)
		sys.exit(1)

	# once the connection is set up; print out 
	# the socket address of your local socket
	print("Connection established. My socket address is", sockfd.getsockname())

	# send the HTTP request message
	msg = 'GET /{} HTTP/1.1\r\nHost: {}:{}'.format(argv[3],argv[1],argv[2])
	msg +='''
	User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
	Accept-Language: pt-PT,pt;q=0.8,en;q=0.5,en-US;q=0.3
	Keep-Alive: timeout = 10, max =100 
    Connection: keep-alive
	'''
    
	sockfd.send(msg.encode("ascii"))
    
    # receive response message
	try:
	    rmsg = sockfd.recv(1024)
	except socket.error as emsg:
	    print("Socket recv error: ", emsg)
	    sys.exit(1)
	
    #get size of response message body
	remaining = get_content_length(rmsg.decode("ascii"))
    
	try:
	    fd = open(argv[3], "wb")
	except IOError as emsg:
	    print("File open error: ", emsg)
	    sys.exit(1)
            
	print("Start receiving response body. . .")
	
	while remaining > 0:
		try:
			rmsg = sockfd.recv(1000)
		except socket.error as emsg:
			print("Socket recv error: ", emsg)
			sys.exit(1)
            
		try:
			fd.write(rmsg)			
		except IOError as emsg:
			print("File open error: ", emsg)
			sys.exit(1)    
        
		remaining -= len(rmsg)

    # close connection
	print("[Completed]")
	fd.close()
	
	sockfd.close()

if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Usage: python3 WebClient.py <Server_addr> <Server_port> <filename>")
		sys.exit(1)
	main(sys.argv)
