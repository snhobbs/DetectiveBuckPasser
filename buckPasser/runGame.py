import miniboa,os, subprocess, sys
import pexpect, re
from subprocess import PIPE, STDOUT
clients = []

class Client(object):
    def __init__(self):
        self.process = pexpect.spawnu('python3', ['-c', 'from buckPasser import run;run()'])
        self.process.setecho(0)
    
    def sendMessage(self, msg):
        print(msg, end = '')

    def getInput(self):
        '''
        assuming commandline
        '''
        return input()

    def expectInteract(self):
        '''
        Gets input and puts output from the expect process.
        Returns a string to be sent to the user and None otherwise
        '''
        choice = self.process.expect([re.compile('/>$'), '\n'])
        #print("choice ", choice)
        if choice == 0:
            self.sendMessage(self.process.before + self.process.after[:-3])
            msg = self.getInput()
            #print('msg info',msg, len(msg))
            self.process.sendline(msg)

        elif choice == 1:
            if len(self.process.before) > 0:
                self.sendMessage(self.process.before + '\n')

    def interact(self):
        '''
        Interacts with the client
        '''
        self.expectInteract()

class TelnetClient(Client):
    def __init__(self, client):
        Client.__init__(self)
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
        return client.client.get_command().strip()
    
    def close(self):
        self.client.deactivate()

def on_connect(client):
    clients.append(TelnetClient(client))

def process_clients():
    '''
    Check each client, if client.cmd_ready == True then there is a line of
    input available via client.getInput.
    '''
    for client in clients:
        if client.active and client.cmd_ready:
            # If the client sends input interacte with it
            try:
                client.interact()
            except:
                client.close()

def runCmdLine():
	client = Client()
	while True:
		client.interact()

def runTelnet(address="127.0.0.1", port=7000):
    tn = miniboa.TelnetServer(
        port=port, 
        address=address, 
        on_connect = on_connect
    )
    while True:
        tn.poll()
        if len(clients) > 0:
            process_clients()
