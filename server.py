#!/usr/bin/python
# -*- coding: utf-8 -*- 

import socket
import os
import sys
import select
import thread

host = ''
port = 9896
backlog = 10
size = 2048
temp = 0

#function for help command
def usage(client):
    msg= '''
Command List:

\GET_CLIENT_LIST – to request list of connected clients

\GET_CLIENT_INFO <username> - to receive listening socket of the client to connect to

\DISCONNECT_CLIENT –  to indicate that you are no longer connected to the chat service\n'''
    client.send(msg)

#to store username and password in dictionary, to register user
def store(client,dict,uname,pswd,c_info):
    if dict.has_key(uname):
        client.send('username is already taken. Type "Y" to set new username\n')
    else:
        dict[uname]=pswd
        corl(client,c_info,uname)
        client.send('\nType your request or type \help for help\n')

#to check if username and password is present in dictionary, to authenticate user
def check(client,dict,uname,pswd,c_info):
    if dict.has_key(uname) and dict[uname] == pswd:
        client.send('Welcome back ' +uname)
        corl(client,c_info,uname)
        temp = 0
    else:
        client.send('Incorrect username or password! Try again\n')
        temp = 1
    return temp

#ask if client wants to listen for connections or connect to existing client
def corl(client,c_info,uname):
    client.send('Do you want to "connect" or "listen"? ')
    resp = client.recv(size)
    if resp == 'listen':
        client.send('Enter your listening port: ')
        cport = client.recv(size)
        c_info[uname] = cport

#provides client_info i.e. listening port
def info(client,c_info):
    client.send('username: ')
    uname = client.recv(size)
    if c_info.has_key(uname):
        client.send(c_info[uname])
        #log[uname]
    else:
        client.send('Incorrect username')

#function to process requests from client
def start(client,input,dict,c_info,log):
    try:
        data = client.recv(size)

        if data == 'y' or data == 'Y':    #requests new username and password if new user
            client.send('Set new username & password\nusername: ')
            uname = client.recv(size)
            client.send('password: ')
            pswd = client.recv(size)
            store(client,dict,uname,pswd,c_info)
        
        elif data == 'n' or data == 'N':   #if existing user, it verifies the username and password
            for x in range(0, 3):          #provides three attempts for user to login
                client.send('Type your username and password\nusername: ')
                uname = client.recv(size)
                client.send('password: ')
                pswd = client.recv(size)
                if check(client,dict,uname,pswd,c_info)==0:
                    client.send('\nType your request or type \help for help\n')
                    break
                if x == 2:
                    client.send('You have exceeded the no. of retries')        
                
        if data == '\help':                 #if help command is given
            usage(client)    

        if data =='\GET_CLIENT_LIST':       #send list of connected clients to user
            client.send('\CLIENT_LIST: ' +str(dict.keys()))

        if data =='\GET_CLIENT_INFO':       #sends listening port of client
            info(client,c_info) 

        if data == '\DISCONNECT_CLIENT':    #disconnect client if requested
            client.close()
            input.remove(client)

        else:
            pass
    except:
        client.close()
        input.remove(client)
        
#main to create initial connection
def main():
    #creating a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #binding the socket to localhost and port
    sock.bind((host,port))
    sock.listen(backlog)
    input = [sock]
    dict = {}    #to store username and password
    c_info = {}  #to store username and port nos.
    log = {}     #to store chat sessions
    print "Chat server is now running on port " + str(port)
    while 1:
        # Using Select to handle multiplexing
        inready,outready,exceptready = select.select(input,[],[])
        for s in inready:
            if s == sock:
                client, address = sock.accept()
                input.append(client)
                client.send('Are you a new user? Type Y or N: ')
            else:
                start(s,input,dict,c_info,log)

if __name__ == '__main__':
    main()
