import tkinter as tk
from tkinter import filedialog, Text
from tkinter import Frame
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import Menu
from tkinter import *
import os
from os import *
import webbrowser
from webbrowser import *
import subprocess
from subprocess import *
import threading
from threading import *
import socket
from socket import *

import urllib
import time
from datetime import datetime

import sys
from sys import *
import urllib
from urllib import *
import time
from time import *
from datetime import datetime
import ipaddress
from ipaddress import *

print('    /-------------------------------------\ ')
print('   /                                       \ ')
print('  /   ---       ---        ---       ---    \ ')
print(' /   /  /      /  /        \  \      \  \    \ ')
print('/   /  /      /  /----------\  \      \  \    \ ')
print('\   \  \      \  \__________/  /      /  /    / ')
print(' \   \  \      \  \        /  /      /  /    / ')
print('  \   ---       ---        ---       ---    / ')
print('   \                                       / ')
print('    \-------------------------------------/ ')

sleep(1)

license = input('enter license :')

if license == ('4DDEQFR'):
    print('welcome to PYcharm')
    print('------------')

else:
    print('invalid license')
    quit()

root = tk.Tk()


root.title('PYSTART')

Frame = tk.Frame(root)
Frame.pack()

frame01 = tk.Frame(Frame)
frame01.pack()
apps = []


    
def google():
    webbrowser.open('www.google.com')

def YT():
    webbrowser.open('www.youtube.com')




    


def addapp():


        
    filename= filedialog.askopenfilename(initialdir='/', title='file selector', filetypes=(('executables','*.exe'), ('allfiles', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(Frame, text=app, bg='white')
        label.pack()


def runapps():
    for app in apps:
        os.startfile(app)

def stop():

    messagebox.askokcancel('terminate', 'terminating program')

    quit()

def cmd():
    os.system('cmd /k color a')

def discord():
    os.startfile('C:/Users/casperdevens/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord.lnk')

def teams():
    os.startfile('C:/Users/casperdevens/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Microsoft Teams.lnk')


def hackerman():

    root02 = tk.Tk()
    root02.title('HackerManModule')

    frame02 = tk.Frame(root02, bg='black')
    frame02.pack()

    frame03 = tk.Frame(frame02, bg='black')
    frame03.pack()



    def ipcam():
        webbrowser.open('inurl /view/index.shtml')

    def tracert192():
        os.system('cmd /k tracert 192.168')

    def tracert84():
        os.system('cmd /k tracert 84.112')

    def ip_sec():
        

        ip2 = input('what is the ip address :')

        ipa = ipaddress.ip_address(ip2)

        ip2a = ipa.is_private

        ip2b = ipa.is_global

        ip2c = ipaddress.ip_address(ip2).is_loopback

        ip2d = ipaddress.ip_address(ip2).is_multicast

        ip2e = ipaddress.ip_address(ip2).is_link_local

        ip2f = ipaddress.ip_address(ip2).is_reserved

        print('-----------------------------------')

        print('is it a private ip adress =')
    
        sleep(1)
        print(ip2a)

        print('-----------------------------------')

        print('is the ip address global =')

        sleep(1)
        print(ip2b)
  
        print('-----------------------------------')

        print('is the ip address a loopback =')

        sleep(1)
        print(ip2c)

        print('-----------------------------------')

        print('is the ip address a multicast =')

        sleep(1)
        print(ip2d)

        print('-----------------------------------')

        print('is the ip address local =')

        sleep(1)
        print(ip2e)

        print('-----------------------------------')

        print('is the ip address reserved =')

        sleep(1)
        print(ip2f)

    def ping():
        

        ip = input('enter Ip Address')
        
        for ping in range(1,10):
            
            address = ip + str(ping)
            res = subprocess.call(['ping', '-c', '3', address])
            if res == 0:
                
                print("ping to", address, "OK")
            elif res == 2:

                print("no response from", address)
            else:
                
                print("ping to", address, "failed!")

    def ip_logger():
        Ip = input('enter Ip you want to log:')

        try:
            host = Ip
            port = 80

            socket.bind((host, 80))
        except:
            print('Error')
            print('Try another Ip Address')

        while True:
            try:
                socket.listen(5)
                conn, address = s.accept()

                print('[+] Ip Logged' + (str(address[0])))

            except:
                pass
                print('exiting')
                sys.exit(0)

        
        



    tracert192 = tk.Button(frame02, text='tracert 192.168', fg='green', bg='black', command=tracert192)

    tracert192.pack(side=LEFT)

    tracert84 = tk.Button(frame02, text='tracert 84.112', fg='green', bg='black', command=tracert84)

    tracert84.pack(side=RIGHT)

    ipcam = tk.Button(frame02, text='Ip Camera', fg='green', bg='black', command=ipcam)

    ipcam.pack(side=LEFT)

    ipcheck = tk.Button(frame02, text='Ip security', fg='green', bg='black', command=ip_sec)

    ipcheck.pack(side=RIGHT)

    ping = tk.Button(frame02, text='Ip Pinger', fg='green', bg='black', command=ping)

    ping.pack(side=LEFT)

    ip_logger = tk.Button(frame03, text='Ip Logger', fg='green', bg='black', command=ip_logger)

    ip_logger.pack(side=LEFT)

    

    
    
canvas = tk.Canvas(root, height=75, width=100, bg='white')
canvas.pack()

openfile = tk.Button(Frame, text='Open File', padx=10, pady=5, fg='white', bg='#0000AA', command=addapp)

openfile.pack(side=RIGHT)

runapp = tk.Button(Frame, text='Run Apps', padx=10, pady=5, fg='white', bg='#0000AA', command=runapps)

runapp.pack(side=RIGHT)

stop = tk.Button(root, text='Stop Program', fg='white', bg='#0000AA', command=stop)

stop.pack(side=RIGHT)

cmdopen = tk.Button(Frame, text='Command Prompt', padx=10, pady=5, fg='white', bg='#0000AA', command=cmd)

cmdopen.pack(side=LEFT)

google = tk.Button(root, text='Google', fg='white', bg='#0000AA', command=google)

google.pack(side=LEFT)

YT = tk.Button(root, text='YouTube', fg='white', bg='#0000AA', command=YT)

YT.pack(side=LEFT)

hackerman = tk.Button(frame01, text='HackerMan', fg='green', bg='black', command=hackerman)

hackerman.pack()

root.mainloop()
