# -*- coding: utf-8 -*-
"""
This program is a random number generating game for tkinter.
The goal of this game is to guess a random number from 1 to a number of your chooseing.
This is my first ideration of this game I hope you enjoy.
@author: Chris Thummel
"""

from tkinter import *
import random 
import tkinter.font as tkFont
import threading

root = Tk()
root.title('Number Game')
root.geometry("200x100")
root.configure(bg='white')
fontStyle = tkFont.Font(family="times", size=10)


# This function allowes you to set the number you want to guess to
def Set ():
    global y 
    global x
    
    x = e.get()# Gets entry text.
    y = random.randint(1,int(x))# generates random number based on the value of x
    e.delete(0, END)# Deletes whats in the entry box.
  
    label_result.config(text='Pick a number from 1 - '+ str(x))
    
    
  # This  function will is what compares the random number and he number you guess  
def check ():
    
    x = e.get()# This is what is calling for the text input.
    c = int(x)#converts entry input into an int.
    
    # Checks to see if c and the random number are same.
    if c == y:
        label_result.config(text='You Got it!')
        e.delete(0, END)
        timer = threading.Timer(5.0, Restart) 
        timer.start() 
        
    elif c > y:
        label_result.config(text='You need to guess a\nsmaller number.')
    elif c < y:
        label_result.config(text='You need to guess \n a larger number.')
    else:
        label_result.config(text='Something went wrong.')
        

# This is the label box this puts the text on the screen.
label_result = Label(root,  text ='Pick a number you would \n like to guess to.', bg = 'white',font=fontStyle )
label_result.pack()

#These are the buttons in the  game each button is linked to a function.
button_set = Button(root, text = 'Set', bg = 'blue', fg = 'yellow', padx=12, pady=2, font=fontStyle, command = Set).pack(side='right')
button_check = Button(root, text = 'Check', bg = 'yellow', fg= 'blue',font=fontStyle, command = check).pack(side = 'left')

#This is the entry box this is where you write down your guess and number that you guess to.
e = Entry(root, width = 7, bg = "white", borderwidth=2)
e.pack()

def Restart():
    label_result.config(text='Pick a number you would \n like to guess to.')

root.mainloop()
root.destroy()
