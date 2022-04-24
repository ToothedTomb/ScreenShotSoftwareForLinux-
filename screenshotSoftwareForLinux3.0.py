from tkinter import*
from tkinter import ttk, messagebox
import tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import pyautogui
import time
import tkinter as tk
from tkinter.ttk import *
import os
root = tkinter.Tk()
root.title("Screenshot Software For Linux 3.0!")
root.attributes('-topmost',True)
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='Icon.png'))
root.geometry("610x180")
root.resizable(0,0)
my_menu = Menu(root)
root.config(menu=my_menu)
def our_command2():

    root = tkinter.Tk() 
    root.resizable(0,0)
    root.title("Who made this software?")
    root.attributes('-topmost',True)


    labelTitle = ttk.Label(root,font=("Ubuntu", 12,"bold","underline"),anchor='center', text="Who made this game?")
    label = ttk.Label(root,font=("Ubuntu", 12,"bold",),anchor='center', text="Jonathan Steadman has made this software.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tkinter.Button(root, text="Exit",font=("ubuntu",16,),activebackground='#cc6633', command = root.destroy)
    B1.pack()
def our_command3():
    root = tkinter.Tk() 
    root.attributes('-topmost',True)

    root.resizable(0,0)
    root.title("What is this software about?")


    labelTitle = ttk.Label(root,font=("Ubuntu", 12,"bold","underline"),anchor='center', text="What is this software about?")
    label = ttk.Label(root,font=("Ubuntu", 12,"bold",),anchor='center', text="Free and open source basic screenshot software for Linux.")
    labelTitle.pack(side="top",fill="x",pady=1)
    label.pack(side="top", fill="x", pady=2)
    B1 = tkinter.Button(root, text="Exit",font=("ubuntu",16,),activebackground='#cc6633', command = root.destroy)
    B1.pack()
file_menu= Menu(my_menu,activebackground="#cc6633",border="6")
my_menu.add_cascade(label="About:",font=("Ubuntu",12),activebackground="#cc6633", menu=file_menu)
file_menu.add_command(label="Who made this software?",font=("Ubuntu",12,),activebackground="#cc6633",command=our_command2) 
file_menu.add_command(label="What is this software about?",font=("Ubuntu",12,),activebackground="#cc6633",command=our_command3) 
def on_closing():
    if messagebox.askokcancel("Confirm to close this software:", "Do you want to close this software?"):
        root.destroy()
def screen():
    # hide the root window
    root.withdraw()
    # stop execution for 3 seconds
    # to open any window of which you
    # want to take the screenshot
    time.sleep(3) 
    # capture screenshot
    sc = pyautogui.screenshot()
    save = messagebox.askyesno("Message:","Do you want to store this screenshot to your storage drive?")
    if save:
        file=asksaveasfilename(defaultextension =".ppm",
                               filetypes=[("All Files Types:","*.*"),
                                          ("PNG file","*.png"),
                                          ("jpg file","*.jpg"),
                                          ("pdf file","*.pdf"),
                                          ("Python Imaging Library","*.ppm")])
        # save screenshot
        if file: 
                sc.save(file)
                print("Screenshot has been saved.")
    # unhide the root window            
    root.deiconify()
style = Style()
style.configure('TButton', font =
               ('Ubuntu', 15),
                    borderwidth = '10')
style.map('TButton', foreground = [('active', '!disabled', 'black')],
                     background = [('active', '#cc6633')])
# create button to take screenshot
Welcome = tkinter.Label(root, text = "Press the button below to take a screenshot!", 
                                    font = ('Ubuntu', 15,"bold")) 
Welcome.pack() 
capture = ttk.Button(root, text="Take Screenshot", command=screen)
capture.pack(pady=22)
Install = tkinter.Label(root, text = "It should work but if not working: Please enter this command in the terminal:", 
                                    font = ('Ubuntu', 12,"bold")) 
Install.pack() 
InstallIns = tkinter.Label(root, text = "sudo apt-get install scrot.", 
                                    font = ('Ubuntu', 14,"bold")) 
InstallIns.pack() 
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()