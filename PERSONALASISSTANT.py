from tkinter import*
import os
import speech_recognition as sr
import pyaudio
from tkinter import messagebox
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import html5lib
import pyttsx3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
root=Tk()
image=PhotoImage(file=r"C:\Users\Admin\Desktop\PYTHON FILES\PERSONAL ASIISTANT\images\phone.png").subsample(22,22)
image2=PhotoImage(file=r"C:\Users\Admin\Desktop\PYTHON FILES\PERSONAL ASIISTANT\images\qwww.png").subsample(50,50)
root.title("EVA")
root.configure(bg="white")
root.resizable(0,0)


def SpeechtoText():
	"""r=sr.Recognizer()
	with sr.Micropghfghhone() as source:
		print("say sghomethifghng")
		a=r.dfsdfglfifdgsteghfnhf(source)
		try:fggdfgf
			text=r.recognize_google(a)
		excepsdt:"""g
	text="wiki"	
	return(text)
def TexttoSpeech(text):
	
 engine = pyttsx3.init('sapi5')
 rate=engine.setProperty('rate',115)
 engine.say(text)
 engine.runAndWait()
def helpdesk():
  rootwik=Tk()
  rootwik.title("README")
  S = Scrollbar(rootwik)
  T = Text(rootwik, height=20, width=60)
  S.pack(side=RIGHT, fill=Y)
  T.pack(side=LEFT, fill=Y)
  S.config(command=T.yview)
  T.config(yscrollcommand=S.set)
  f=open(r"C:\Users\Admin\Desktop\PERSONAL ASIISTANT\files\hi.txt")
  x=f.read()
  T.insert(END,x)
  u="Personal assistant, important functions"
  TexttoSpeech(u)
  rootwik.mainloop()
  
def mainfunction():
	a=SpeechtoText()
	q=a.split(" ")
	print(a)
but=Button(root,image=image,command=mainfunction)
but.grid(row=0,column=0)
lab=Label(root,text="I am listening lol checking if exetension",bg="white",fg="blue")
but2=Button(root,image=image2,command=helpdesk)
but2.grid(row=0,column=3)

lab.grid(row=0,column=1)		

root.mainloop()
