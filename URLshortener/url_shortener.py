'''URL Shortener
Author : Lakshmi Sowjanya'''

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import pyshorteners as sht


master = tk.Tk(className="URL shortener")

master.geometry("500x500")
mainFrame = Frame(master)
mainFrame.pack()

url_str = tk.StringVar()
Label(mainFrame, text="Enter URL").grid(row=0,column=0)
Label(mainFrame, text="Shortened URL").grid(row=2,column=0)
url_text = Entry(mainFrame,textvariable=url_str,bg='white')
url_text.grid(row=0,column=1)



def url_shortener():
    shortener = sht.Shortener()
    short_url = shortener.tinyurl.short(url_str.get())
    print(short_url)
    # messagebox.showinfo("message",short_url)
    # output_url.delete('0','end-1c')
    output_url.insert(0,short_url)

buttonFrame = Frame(master)
buttonFrame.pack()
short_button = tk.Button(buttonFrame,text='shorten',activebackground='white',activeforeground='pink',width=20,bg='white',command=url_shortener)
short_button.grid(row=1,column=2)
short_button.pack()

output_url = Entry(mainFrame)
output_url.grid(row=2,column=1)


master.mainloop()



