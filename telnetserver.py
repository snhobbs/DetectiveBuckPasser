import miniboa,os, subprocess, sys
import pexpect, re
from subprocess import PIPE, STDOUT
from buckPasser import run
clients = []

class Client(object):
    def __init__(self, client):
        self.client = client
        self.process = pexpect.spawnu('./buckPasser.py')
        self.process.setecho(0)
    @property
    def active(self):
        return self.client.active

    @property
    def cmd_ready(self):
        return self.client.cmd_ready

    def get_command(self):
        return self.client.get_command()

def on_connect(client):
    clients.append(Client(client))

def process_clients():
    """
    Check each client, if client.cmd_ready == True then there is a line of
    input available via client.get_command().
    """
    for client in clients:
        if client.active and client.cmd_ready:
            # If the client sends input echo it to the chat room
            try:
                interact(client)
            except:
                client.client.deactivate()
                
def interact(client):
    choice = client.process.expect([re.compile('\n*/>$'), '\n'])
    if choice == 1:
        if len(client.process.before) == 0:
            return
        client.client.send(client.process.before + '\n')
    else:
        msg = client.get_command().strip()
        print('msg info',msg, len(msg))
        client.client.send(client.process.before + client.process.after[:-3] )
        client.process.sendline(msg)
                    
if __name__ == "__main__":
    tn = miniboa.TelnetServer(
        port=7000, 
        address='127.0.0.1', 
        on_connect = on_connect
    )
    while True:
        tn.poll()
        if len(clients) > 0:
            process_clients()
