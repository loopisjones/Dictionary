import json
import pprint
import os
import cv2
from PIL import Image, ImageTk
from Tkinter import *
from time import strftime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#initsheet
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\SignIn\client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/151kMtuOOoaz9Gjnjfp_BUBj8BKRIBZ3e3aXNQATrto0/edit#gid=0')

worksheet = sheet.get_worksheet(0)
#initsheet


#inittk
app = Tk()
app.geometry('{0}x{1}+0+0'.format(app.winfo_screenwidth(), app.winfo_screenheight()))
#inittk

#initcv2
cap = cv2.VideoCapture(0)
#initcv2

img = cap.read()
canvas = Canvas(root, width = 300, height = 300)
canvas.pack()
canvas.create_image(20,20, anchor=NW, image=img)
ide = StringVar()
ida = Entry(app, textvariable = ide)
ida.pack()
def test():
    label = Label(app, text = ide.get())
    label.pack()
button = Button(app, text = 'test', command = test)
button.pack()

app.mainloop()
