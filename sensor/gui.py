#! /usr/bin/python
from tkinter import *
import random
from time import gmtime, strftime
import os
import time

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master) 
        Frame.config(self, bg="white")                
        self.master = master
        self.init_window()

    # Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Quit",command=self.client_exit)
        quitButton.config(bg="red", fg="black", highlightthickness="-1")
        quitButton.place(x=20, y=20)

        text = Label(self, text="Hey there good lookin!")
        text.config(bg="white", fg="black")
        text.pack()
        text.place(relx=0.5, y=40, anchor=CENTER)

        # text input
        name = Label(self, text="Name:")
        numId = Label(self, text="ID:")
        name.config(bg="white", fg="black")
        numId.config(bg="white", fg="black")
        name.place(x=10, y=80)
        numId.place(x=10, y=110)
        
        global name_input
        global numId_input
        name_input = Entry(self)
        numId_input = Entry(self)
        name_input.place(x=80, y=80)
        numId_input.place(x=80, y=110)
        
        global nextButton
        nextButton = Button(self, text="Next",command=self.show_entry)
        nextButton.place(x=100, y=140)


    
    def client_exit(self):
        exit()

    def show_entry(self):
        #print("First Name: %s\nLast Name: %s" % (name_input.get(), numId_input.get()))
        nextButton.config(state="disabled")

        name = Label(self, text=name_input.get())
        numId = Label(self, text=numId_input.get())
        name.config(bg="white", fg="black")
        numId.config(bg="white", fg="black")

        name.place(x=10, y=200)
        numId.place(x=100, y=200)
        
        global take_book
        take_book = Button(self, text="Accept",command=self.accept_book)
        take_book.place(x=10, y=230)

    def accept_book(self):
        # get book_id by random [example]
        name = name_input.get()
        numId = numId_input.get()
        name_id = name + numId

        rand = random.sample(name_id, 5)
        global book_id
        book_id = rand[0] + rand[1] + rand[2] + rand[3] + rand[4] + strftime("%Y%m%d%H%M%S")
        print(book_id)
        
        # disable accept button
        take_book.config(state="disabled")

        trip_id = Label(self, text='Trip_id: ' + book_id)
        trip_id.config(bg="white", fg="black")
        trip_id.place(x=10, y=300)

        os.system('lxterminal -e python3 sensor.py ' + book_id)

        global done_btn
        done_btn = Button(self, text="Done",command=self.done_book)
        done_btn.place(x=100, y=230)

        # show acceleration sensor data
        time.sleep(10)
        f = open ( '/home/pi/sensor/data/'+book_id+'accl.txt',"r" )
        while True:
            lineList = f.readlines()
            time.sleep(2)

        acceleration = Label(self, text='acceleration: ' + lineList[-1])
        acceleration.config(bg="white", fg="black")
        acceleration.place(x=10, y=330)

    def done_book(self):
        # enable accept button
        take_book.config(state="active")
        # disable done button
        done_btn.config(state="disabled")

        

        
        

root = Tk()
 
# size of the window
root.geometry("800x500")

root.overrideredirect(True)
root.overrideredirect(False)
app = Window(root)
root.mainloop()  