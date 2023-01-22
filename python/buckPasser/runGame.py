import miniboa,os, subprocess, sys
import pexpect, re, traceback
from collections import deque
from subprocess import PIPE, STDOUT
clients = []

class Client(object):
    arg = '/>'
    regEx = re.compile(arg)
    def __init__(self):
        self.process = pexpect.spawnu('python3', ['-c', 'from buckPasser import run;run()'])
        self.process.setecho(0)

class CmdLineClient(Client):
    def sendMessage(self, msg):
        print(msg, end = '')

    def getInput(self):
        '''
        assuming commandline
        '''
        return input()
    
    def interact(self):
        '''
        Gets input and puts output from the expect process.
        Returns a string to be sent to the user and None otherwise
        '''
        self.process.expect(self.regEx)
        self.sendMessage(self.process.before)
        msg = self.getInput()
        if msg is not None:
            self.process.sendline(msg)
 
class TelnetClient(Client):
    def __init__(self, client):
        self.client = client
        Client.__init__(self)
        self.cmdBuff = deque()
        self.client = client
        
    @property
    def active(self):
        return self.client.active

    @property
    def cmd_ready(self):
        return self.client.cmd_ready
    
    def sendMessage(self,msg):
        self.client.send(msg)

    def getInput(self):
        if len(self.cmdBuff) > 0:
            return self.cmdBuff.popleft()
    
    def close(self):
        self.client.deactivate()
    
    def interact(self):
        '''
        Gets input and puts output from the expect process.
        Returns a string to be sent to the user and None otherwise
        '''
        msg = self.getInput()
        if msg is not None:
            self.process.sendline(msg)
        self.process.expect(self.regEx)
        self.sendMessage(self.process.before)

def on_connect(client):
    clients.append(TelnetClient(client))
    clients[-1].interact()

def on_disconnect(client):
    if client in clients:
        clients.remove(client)

def process_clients():
    '''
    Check each client, if client.cmd_ready == True then there is a line of
    input available via client.getInput.
    '''
    for client in clients:
        if client.cmd_ready and client.active:
            try:
                client.cmdBuff.append(client.client.get_command())
                client.interact()
            except Exception as e:
                print("Error:", e, traceback.print_exc())
                client.close()

def runCmdLine():
	client = CmdLineClient()
	while True:
		client.interact()

def runTelnet(address="127.0.0.1", port=7000):
    tn = miniboa.TelnetServer(
        port=port, 
        address=address, 
        on_connect = on_connect,
        on_disconnect = on_disconnect
    )
    while True:
        tn.poll()
        if len(clients) > 0:
            process_clients()
