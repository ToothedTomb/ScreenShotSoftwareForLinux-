from tkinter import*
from tkinter import ttk, messagebox
import tkinter
from tkinter.filedialog import askopenfilename,asksaveasfilename
import pyautogui
import time
import tkinter as tk
from tkinter.ttk import *
import os
root = tkinter.Tk()
root.title("Screenshot Software For Linux 2.0!")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='Icon.png'))
root.geometry("610x210")
root.resizable(0,0)
def screen():
    # hide the root window
    root.withdraw()
    # stop execution for 3 seconds
    # to open any window of which you
    # want to take the screenshot
    time.sleep(3) 
    # capture screenshot
    sc = pyautogui.screenshot()
    save = messagebox.askyesno("Screenshot Software For Linux 2.0!","Do you want to store this screenshot to your storage drive?")
    if save:
        file=asksaveasfilename(defaultextension =".ppm",
                               filetypes=[("All Files Types:","*.*"),
                                          ("PNG file","*.png"),
                                          ("jpg file","*.jpg"),
                                          ("pdf file","*.pdf"),
                                          ("Python Imaging Library","*.ppm"),
                                          ("GIF","*.gif")])
        # save screenshot
        if file: 
                sc.save(file)
                print("Screenshot has been saved..")
    # unhide the root window            
    root.deiconify()
style = Style()
style.configure('TButton', font =
               ('Ubuntu', 15),
                    borderwidth = '10')
style.map('TButton', foreground = [('active', '!disabled', 'black')],
                     background = [('active', 'green')])
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
MadeBy = tkinter.Label(root, text = "This software was made by Jonathan Steadman.", 
                                    font = ('Ubuntu', 12,"bold")) 
MadeBy.pack() 
root.mainloop()