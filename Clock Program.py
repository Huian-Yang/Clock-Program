from tkinter import *
from time import * 

def update():
    time_string = strftime("%I:%M:%S %p") #display current time
    time_label.config(text=time_string) #updates time label
    
    day_string = strftime("%A") #display day of the week
    day_label.config(text=day_string) #updates time
    
    date_string = strftime("%B %d, %Y") #display month,day,year
    date_label.config(text=date_string) #updates time
    
    window.after(1000,update)   #update this window every second/1000 milisecond
                                #recursive function, calling a function in a function

window = Tk()
window.title("Clock Program")

time_label = Label(window,font=("Arial",50),fg="green",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25))
day_label.pack()

date_label = Label(window,font=("Ink Free",30))
date_label.pack()

update() #recursive function


window.mainloop()
