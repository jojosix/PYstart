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

    license01 = input('enter second license (License text file) :')
    if license01 == ('6DQTYLM'):

        print('Welcome')
        print('------------')

    else:
        print('invalid license')
        quit()

    root02 = tk.Tk()
    root02.title('HackerManModule')

    frame02 = tk.Frame(root02, bg='black')
    frame02.pack()

    label02 = tk.Label(frame02, text='PYstart', fg='green', bg='black')
    label02.pack()

    def ipcam():
        webbrowser.open('inurl /view/index.shtml')

    def tracert192():
        os.system('cmd /k tracert 192.168')

    def tracert84():
        os.system('cmd /k tracert 84.112')


    tracert192 = tk.Button(frame02, text='tracert 192.168', fg='green', bg='black', command=tracert192)

    tracert192.pack(side=LEFT)

    tracert84 = tk.Button(frame02, text='tracert 84.112', fg='green', bg='black', command=tracert84)

    tracert84.pack(side=LEFT)

    ipcam = tk.Button(frame02, text='Ip Camera', fg='green', bg='black', command=ipcam)

    ipcam.pack(side=BOTTOM)
    
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
