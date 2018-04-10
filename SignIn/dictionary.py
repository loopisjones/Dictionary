import json
import pprint
import os
import cv2
from PIL import Image, ImageTk
from Tkinter import *
from time import strftime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#inittk
app = Tk()

#inittk

#initsheet
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\SignIn\client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/151kMtuOOoaz9Gjnjfp_BUBj8BKRIBZ3e3aXNQATrto0/edit#gid=0')

worksheet = sheet.get_worksheet(0)
#initsheet


#initcv2
lmain = Label()
cap = cv2.VideoCapture(0)
#initcv2

img = cap.read()




def show():
    frame = cap.read()
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = ImageTklmain.configure(image=imgtk)
    lmain.after(10, show)
label1 = Label(app, text = 'ID')
id = StringVar()
idin = Entry(app, textvariable = id )

label1.grid(row=0,column=0)
idin.grid(row=0,column=1)

show()
app.mainloop()
