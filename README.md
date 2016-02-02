# Peer-to-Peer-Chat-and-File-Sharing-Server
A chat service in python which enables clients to chat and share files between each other. The client makes a direct connection to the opposite client using the information provided by the server, and the server maintains a log of chat sessions. This program was developed as part of the Socket programming assignment for the Data Communications course.

--------------------
Author Information
--------------------
--> Name: Harsh Kotak  
--> Email ID: Harsh.Kotak@colorado.edu

-----------------------
Application Description
-----------------------
A peer-to-peer chat and file sharing service is built where multiple clients will be able to log into a central server, and subsequently share files with each other directly. The chat system consists of a central server that manages multiple chat sessions, and users can participate as chat clients. Clients connect to the central server on its universally-known port. Upon connection, the server asks each client if it is a new client or a returning one. In case it is a new client, it is asked to register its username and password with the central server. If it is a returning client, the server authenticates them using the existing username/password combination.  
Once this initial process is done, clients request for a list of clients that are currently connected to the server. Clients are then given the listening socket of the client they want to connect to, and it then attempts to make a direct connection to the opposite client using the information from the server. The server keeps a track of all the active chat sessions. Through this direct connection, clients share messages and files with each other. After communication is complete, the clients indicate to the server that the session is finished, and the server removes that session from its database.  

----------------------------------
Program Compilation and Execution
----------------------------------
1) Extract the server and client python files from the 103334084.tar.gz file.  
2) Run the server.py file in the terminal.  
3) Now open a new terminal and run client.py file.  
4) The server will ask if you are a new client or a returning client. Type 'Y' or 'N'.  
5) You will be asked to set a new username and password or type your existing username and password.  
6) If the new username you are trying to set already exists, then you will be asked to set a new username by typing 'Y'.  
7) After you set your username you will be asked to set up your listening port, where other client can connect.  
8) If you are existing user and provide incorrect username for 3 consecutive attempts, you will be blocked.  
9) After this initial log in, you can type your command to be sent to server or type '\help' to get command list.  
10) You can type '\GET_CLIENT_LIST' to get list of clients and '\GET_CLIENT_INFO' to get listening port of other client to connect to.  
11) Your window will display if you are connected to the user and then you can chat.  
12) You can send files to other clients during chat by typing '\SEND_FILE' command.  
13) To end chat session, send '\CLOSE_SESSION' command.  
14) Send '\DISCONNECT_CLIENT' or (Ctrl+C) command to server to disconnect.  

------------------
Technical details
------------------
1) The program is coded in python 2.7  
2) Since the program uses select.select, the program will run only on Linux/Unix environments.  
3) The chat server is running on localhost and port is set at 9876 by default.  
4) The program is currently designed to send '.txt', '.png', and '.pdf' files. It can be easily modified to support other file types.  
