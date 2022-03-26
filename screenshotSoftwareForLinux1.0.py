from tkinter import*
from tkinter import ttk, messagebox
import tkinter
from tkinter.filedialog import askopenfilename,asksaveasfilename
import pyautogui
import time
root = tkinter.Tk()
root.title("Screenshot Software For Linux 1.0!")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='Icon.png'))
root.geometry("610x180")
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
    save = messagebox.askyesno("Screenshot Software For Linux 1.0!","Do you want to store this screenshot to your storage drive?")
    if save:
        file=asksaveasfilename(defaultextension =".png",
                               filetypes=[("All Files","*.*"),
                                          ("PNG file","*.png"),
                                          ("jpg file","*.jpg")])
        # save screenshot
        if file: 
                sc.save(file)
                print("Screenshot has been saved..")
    # unhide the root window            
    root.deiconify()
# create button to take screenshot
Welcome = tkinter.Label(root, text = "Press the button below to take a screenshot!", 
                                    font = ('Ubuntu', 15)) 
Welcome.pack() 
capture = ttk.Button(root, text="Take Screenshot", command=screen)
capture.pack(pady=22)
Install = tkinter.Label(root, text = "It should work but if not working: Please enter this command in the terminal:", 
                                    font = ('Ubuntu', 12)) 
Install.pack() 
InstallIns = tkinter.Label(root, text = "sudo apt-get install scrot.", 
                                    font = ('Ubuntu', 12)) 
InstallIns.pack() 
MadeBy = tkinter.Label(root, text = "This software was made by Jonathan Steadman.", 
                                    font = ('Ubuntu', 12)) 
MadeBy.pack() 
root.mainloop()