# modules
from ast import Delete
import speech_recognition as sr
import pyttsx3  #(Text to Speech conversion library) (offline)
import datetime
import time
import os
import sys
import ctypes
import webbrowser
import pywhatkit as kit
import wikipedia
from datetime import date
from requests import get
from requests.api import request
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
from playsound import playsound
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import sys
from AI1Ui import Ui_MainWindow


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)

def speak(audio):
    engine.setProperty("rate",150)
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        print(f"Good Morning Sir, its {tt}")
        speak(f"Good Morning Sir, its {tt}")


    elif hour>=12 and hour<18:
        print(f"Good Afternoon Sir, its {tt}")
        speak(f"Good Afternoon Sir, its {tt}")   

    else:
        print(f"Good Evening Sir, its {tt}")
        speak(f"Good Evening Sir, its {tt}") 
         
    print("I am PI! your assistant")
    speak("I am PI! your assistant")
    print("How may i help you,sir")
    speak("How may i help you,sir")  

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.hotword()
    
    
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"Sir: {self.query}\n")

        except Exception as e:
            # print(e)    
            return "None"
        return self.query
    
    def taskexecution(self):
        wishMe()    # wish the user
        while True:
        #if 1:
            self.query = self.takeCommand().lower()   
        
            # Assistant sleep command.........
            if "sleep" in self.query:
                speak("okay sir, i am going to sleep you can call me anytime")
                break  
            
            # system commands.............
            elif 'lock window' in self.query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                    
            elif 'system shutdown' in self.query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    os.system("shutdown /s /t 1")
                    
            elif 'system restart' in self.query:
                speak("Okay sir! Sytem is going to restart")
                os.system("shutdown /r /t 1")
            
            elif "system sleep" in self.query:
                speak("okay sir! system is going to sleep")
                os.system("rundll32.exe powrprof.dil,setsuspendstate 0,1,0")
            
            # chatbot...............
            elif 'how are you pi' in self.query:
                speak("I am fine sir")
                speak("What's about you sir.")
                
            elif 'i am fine' in self.query:
                speak("Its good to know.")
            
            # open websites command............
            elif '.com' in self.query or '.org' in self.query or '.pk' in self.query:
                self.query = self.query.replace('open','')
                self.query = self.query.replace('launch','')
                self.query = self.query.replace(' ','')
                self.query = self.query.replace('www.','')
                webbrowser.open_new_tab(self.query)
                speak("opening")
                print("opening...")
            
            # play music onine..........
            elif "play" in self.query:
                self.query = self.query.replace('play','')
                self.query = self.query.replace('song','')
                kit.playonyt(self.query)
            
            # short information on wikipedia.......
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            # current time and date...........
            elif 'today' in self.query or 'time' in self.query or 'date' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                today = date.today()
                current_date = today.strftime('%b %d %y')
                print(f"Time:{strTime}        Date:{current_date}")    
                speak(f"Sir, the time is {strTime} and the date is{current_date}")
            
            # Ip address of device............
            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                print(f"Ip address: {ip}")
                speak(f'Your IP address is {ip}')
                
            # Check the temperature of any city............
            elif "check temperature in" in self.query:
                self.query = self.query.replace('check','')
                self.query = self.query.replace('pi','')
                url = (f"https://www.google.com/search?q={self.query}")
                re = requests.get(url)
                data = BeautifulSoup(re.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                print(f"current {self.query} is {temp}")
                speak(f"current {self.query} is {temp}")
                
            # step wise explanation of anything............
            elif "how to" in self.query:
                max_results = 1
                how_to = search_wikihow(self.query, max_results)
                assert len(how_to) == 1
                how_to[0].print()
                speak("Done sir")
            
            # Check the system battery percentage...........
            elif "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir your system have {percentage} percent battery")
                    
            # Location of place with map...........
            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")
                speak("Okay sir. let me check")
            
            # To check where the user are............
            elif "where i am" in self.query or "Where we are" in self.query or "where I am" in self.query:
                speak("Wait sir, let me check")
                try:
                    ipADD = requests.get("https://api.ipify.org").text
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipADD+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are.")
                    pass
                
            # open applications.............
            elif "open" in self.query:
                self.query = self.query.replace('open','')
                speak(f"opening {self.query}")
                os.system(f"start {self.query}")
            
            # close websites or web apps...........
            elif "close webpage" in self.query or "close website" in self.query:
                self.query = self.query.replace('close','')
                print("closing....")
                speak("closing")
                os.system(f"taskkill /f /im msedge.exe")
            
            # Set Alarm.................
            elif "alarm" in self.query:
                speak("Tell me the time sir")
                time = input("Time:")
                while True:
                    Time_at = datetime.datetime.now()
                    now = Time_at.strftime("%H:%M:%S")
                    speak("Alarm is set sir.")
                    
                    if now==time:
                        speak("Time to wakeup sir")
                        playsound('loud-alarm-02-46010.mp3')
                        speak("Alarm closed")
                        
                    elif now>time:
                        break
            
            # Remainder.................     
            elif "remember that" in self.query:
                remembermsg = self.query.replace("remember that","")
                speak("you tell me to Remaind that:"+remembermsg)
                remember = open("data.txt",'w')
                remember.write(remembermsg)
                remember.close()
            
            elif "what do you remember" in self.query:
                remember = open('data.txt','r')
                speak("you Tell me that"+remember.read())
                speak("sir Do you want to remove the remainder")
                ko = self.takeCommand()

    def hotword(self):
        playsound("D:\Assistant\Assistant.mp3")
        while True:
            permission = self.takeCommand()
            if "wake up" in permission:
                playsound('1_second_tone.mp3')
                self.taskexecution()
            elif "goodbye" in permission:
                speak("thanks for using me sir, have a good day")
                sys.exit()
                
StartExe = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.start.clicked.connect(self.startTask)
        self.gui.exit.clicked.connect(self.close)
        
    def startTask(self):
        
        self.gui.movie = QtGui.QMovie("C:/Users/jitin/Downloads/giphy.gif")
        self.gui.gif1.setMovie(self.gui.movie)
        self.gui.movie.start()
        
        self.gui.movie= QtGui.QMovie("C:/Users/jitin/Downloads/8.gif")
        self.gui.gif2.setMovie(self.gui.movie)
        self.gui.movie.start()
        
        self.gui.movie = QtGui.QMovie("C:/Users/jitin/Downloads/7.gif")
        self.gui.gif3.setMovie(self.gui.movie)
        self.gui.movie.start()
        
        self.gui.movie = QtGui.QMovie("C:/Users/jitin/Downloads/2.gif")
        self.gui.gif4.setMovie(self.gui.movie)
        self.gui.movie.start()
        
        self.gui.movie = QtGui.QMovie("C:/Users/jitin/Downloads/4.gif")
        self.gui.listen_gif.setMovie(self.gui.movie)
        self.gui.movie.start()
        
        self.gui.movie = QtGui.QMovie("C:/Users/jitin/Downloads/Premium Vector _ Abstract background of futuristic sci-fi hud display.jpg")
        self.gui.exit_gif.setMovie(self.gui.movie)
        self.gui.movie.start()
        
        self.gui.movie = QtGui.QMovie("C:/Users/jitin/Downloads/Premium Vector _ Abstract background of futuristic sci-fi hud display.jpg")
        self.gui.start_gif.setMovie(self.gui.movie)
        self.gui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        StartExe.start()
    
        
        
    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('TIME:- hh:mm:ss')
        label_date = current_date.toString('DATE:-dd-MM-yyyy')
        self.gui.png_date1.setText(label_date)
        self.gui.png_time1.setText(label_time)
        
        
app = QApplication(sys.argv)
AI_gui = Main()
AI_gui.show()
app.exec_()
                       
    