import socket, os, sys
def socketCreate():
        try:
            global host
            global port
            global s
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = ''
            port = raw_input('Listening Port: ')
            if port == '':
                socketCreate()
            port = int(port)
        except socket.error as msg:
            print 'Socket creation error: ' + 
            
