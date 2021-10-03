import speech_recognition as sr
import pyttsx3
# import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import sys
import PyPDF2
import pyautogui
import random 
import requests
import cv2
from openpyxl import Workbook
import wolframalpha
from requests import get
from pyautogui import hotkey ,typewrite ,click,prompt,password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
from win10toast import ToastNotifier
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pyowm
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.ttk import *
from time import strftime
import JarvisAI
import re
import pprint
admin = smtplib.SMTP('smtp.gmail.com', 587)
admin.ehlo()
admin.starttls()
admin.ehlo()

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0) 
def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning sir!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon sir!")   

    else:
        talk("Good Evening sir!") 


def sleep():
    time.sleep(1)
def sleep2():
    time.sleep(5)
def sleep3():
    time.sleep(10)
def take_command():
    with sr.Microphone() as source:
        print('Listening....')
        voice = listener.listen(source,timeout=4,phrase_time_limit=7)
            
    try:
        print('Understanding....')
        command = listener.recognize_google(voice)
        print(f"user-said: {command} ")

       
    except Exception as e:
        return "none"
    command=command.lower()
    return command
    
def news():
    url = "http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=de6fb6ca315240b987b40db032daba3a"
    page = requests.get(url).json()
    articles = page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is: {head[i]}")
        talk(f"today's {day[i]} news is: {head[i]}")
def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=de6fb6ca315240b987b40db032daba3a'
def run_alexa():
    wishMe()
    greet='What can I do for you?','How can I help you','I am full of energy and ready to help you sir'
    talk(random.choice(greet))
    while True:
       
        command = take_command()
        print(command)
        # play anything in youtube
        if 'play' in command:
            song = command.replace('play','')
            talk('playing'+song)
            pywhatkit.playonyt(song)
        elif 'voice' in command:
                engine.setProperty('voice', voices[0].id)
                talk("Hello I am your alexa ")
        elif 'hello' in command:
            talk('Hi, what can I do for you')
        # Google Meet
        elif 'google meet' in command:
            talk('Enter the code of the meeting')
            code = prompt(text="enter the meeting code",title="meetbot")#ask for meeting code
            talk('Want to join meeting now?')
            join = input('Want to join meeting now?(y/n) ')
            # zz= float(input('In how many minutes you want to leave the meeting = '))
            # z= int(zz*60)
            if join=="y" or join=="Y":
                # a=prompt(text="enter the email",title="email")
                # b=password(text="enter the password",title="Password(safe)",mask="*")
                # code=prompt(text="Enter meeting code",title="Meeting code")
                opt=Options()
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                # Pass the argument 1 to allow and 2 to block
                opt.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.geolocation": 1,
                "profile.default_content_setting_values.notifications": 1
                })
                # driver =  webdriver.Firefox(executable_path=r'C:\Users\Laptop-16\Desktop\python\geckodriver.exe')
                driver = webdriver.Chrome(chrome_options=opt,executable_path=r'C:\Users\Laptop-16\Desktop\python\chromedriver.exe')
                driver.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Dwm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession')

                driver.maximize_window()
                driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('jhabinayak006@gmail.com')
                time.sleep  
                driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
                time.sleep(2)
                driver.find_element_by_name('password').send_keys('jhabinayak006binayak')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
                time.sleep(5)
                driver.get('https://meet.google.com/'+code)
                # driver.find_element_by_xpath('//*[@id="i3"]').send_keys(code)
                # driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button').click()
                time.sleep(10)
                camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div')
                camera.click()
                time.sleep(1)
                mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div')
                mic.click()
                time.sleep(1)
                join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
                join.click()
                print("Joining the meeting")
                talk("Joining the meeting")
                # time.sleep(65)
                # end = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]')
                # # end2=int(end.text)
                # print(end2)
                # for i in tqdm(range(z),desc="Minutes Left"):
                #         a=(str(z-i))
                #         sleep()

            elif join=="n"or join=="N":
                talk("Do you want to join the meeting in some minutes or hour?")
                seconds1=input("Do you want to join the meeting in minutes/hour(m/h)? ")
                
                if seconds1=="m"or seconds1=="M":
                    seconds=int(input("In how many minutes you want to join= "))
                    talk("In how many minutes you want to join?")
                    s=seconds*60
                    print("Ok timer set. Google meet will open after the timer ends. Till then you can do your other works:)")
                    talk("ok timer set. Google meet will open after the timer ends Till then you can do your other works.")
                    for i in tqdm(range(s),desc="Minutes Left"):
                        a=(str(s-i))
                        sleep()
                    opt=Options()
                    opt.add_argument("start-maximized")
                    opt.add_argument("--disable-extensions")
                    # Pass the argument 1 to allow and 2 to block
                    opt.add_experimental_option("prefs", { \
                    "profile.default_content_setting_values.media_stream_mic": 1,
                    "profile.default_content_setting_values.media_stream_camera": 1,
                    "profile.default_content_setting_values.geolocation": 1,
                    "profile.default_content_setting_values.notifications": 1
                    })
                    # driver =  webdriver.Firefox(executable_path=r'C:\Users\Laptop-16\Desktop\python\geckodriver.exe')
                    driver = webdriver.Chrome(chrome_options=opt,executable_path=r'C:\Users\Laptop-16\Desktop\python\chromedriver.exe')
                    driver.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Dwm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession')

                    driver.maximize_window()
                    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('jhabinayak006@gmail.com')
                    time.sleep  
                    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('jhabinayak006binayak')
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
                    time.sleep(5)
                    driver.get('https://meet.google.com/'+code)
                    # driver.find_element_by_xpath('//*[@id="i3"]').send_keys(code)
                    # driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button').click()
                    time.sleep(10)
                    camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div')
                    camera.click()
                    time.sleep(1)
                    mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div')
                    mic.click()
                    time.sleep(1)
                    join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
                    join.click()
                    print("Joining the meeting")
                    talk("Joining the meeting")
                    # for i in tqdm(range(z),desc="Minutes Left"):
                    #     a=(str(z-i))
                    #     sleep()
                    
                elif seconds1=="h"or seconds1=="H":
                    talk("In how many hours you want to join?")
                    hours=float(input("In how many hours you want to join(write in numbers)= "))
                    h=int(hours*3600)
                    print("Ok timer set. Google meet will open after the timer ends. Till then you can do your other works:)")
                    talk("ok timer set. Google meet will open after the timer ends Till then you can do your other works")
                    for i in tqdm(range(h),desc="hours left"):
                        aa=(str(h-i))
                        sleep()
                        
                    print("Opening Google Meet")
                    talk("Opening Google Meet")
                
                    opt=Options()
                    opt.add_argument("start-maximized")
                    opt.add_argument("--disable-extensions")
                    # Pass the argument 1 to allow and 2 to block
                    opt.add_experimental_option("prefs", { \
                    "profile.default_content_setting_values.media_stream_mic": 1,
                    "profile.default_content_setting_values.media_stream_camera": 1,
                    "profile.default_content_setting_values.geolocation": 1,
                    "profile.default_content_setting_values.notifications": 1
                    })
                    # driver =  webdriver.Firefox(executable_path=r'C:\Users\Laptop-16\Desktop\python\geckodriver.exe')
                    driver = webdriver.Chrome(chrome_options=opt,executable_path=r'C:\Users\Laptop-16\Desktop\python\chromedriver.exe')
                    driver.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Ftab%3Dwm%26ogbl&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession')

                    # driver.maximize_window()
                    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('jhabinayak006@gmail.com')
                    time.sleep(1)  
                    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('jhabinayak006binayak')
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
                    time.sleep(5)
                    driver.get('https://meet.google.com/'+code)
                    # driver.find_element_by_xpath('//*[@id="i3"]').send_keys(code)
                    # driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button').click()
                    time.sleep(10)
                    camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div')
                    camera.click()
                    time.sleep(1)
                    mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div')
                    mic.click()
                    time.sleep(1)
                    join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
                    join.click()
                    print("Joining the meeting")
                    talk("Joining the meeting")
                    for i in tqdm(range(z),desc="Minutes Left"):
                        a=(str(z-i))
                        sleep()
                    talk('meeting ended')
                    
                    # driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span').click
                    # typewrite('Good Morning')
                    # sleep()
                    # pyautogui.press('enter')
                # driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span").click()
        # Closing the tabs (Not working Working on it.)
        elif 'close the tabs' in command or 'close the tab' in command:
           talk('Ok sir closing the tabs')
           os.system("taskkill /f /im chromedriver.exe")
        # Youtube
        elif 'youtube' in command:
            print('opening youtube')
            talk('opening youtube')
            webbrowser.open(r'C:\Users\Laptop-16\Desktop\python\youtube.py')
        # Map
        elif 'map' in command:
            op = command.replace('open','')
            print('Opening '+op)
            talk('Opening '+op)
            webbrowser.open_new('https://maps.google.com/')
        # all web browser
        elif 'open' in command:
            obj = JarvisAI.JarvisAssistant()
            if re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                print(open_result)
                talk('Ok sir Here you go.')        
        # Search for something
        elif 'search for' in command:
            search = command.replace('search for','')
            print('opening '+search)
            talk('Searching sir')
            pywhatkit.search(search)
        # Time
        elif 'time' in command:
            t = datetime.datetime.now().strftime('%I:%M %p')
            print(t)
            talk('Current Time is '+ t)
        # Reminder
        elif 'reminder' in command:
            reminder=input("Enter the reminder title = ")
            reminder_time=input("Enter time (HH:MM AM/PM) = ")
            email=input("Incase you miss to see reminder please tell your email = ")
            print("Reminder set:)")
            talk("Reminder Set")
            while True:
                current_time = time.strftime("%I:%M %p")
                if current_time == reminder_time:
                    print('Your Reminder: '+reminder)
                    talk('Your Reminder: '+reminder)
                    break
                else:
                    pass 
                    
            hr=ToastNotifier()
            hr.show_toast("Reminder",reminder,icon_path=r'C:\Users\Laptop-16\Desktop\python\logo.ico',duration=10)
            def send():
                admin.login('jhabinayak006@gmail.com','jhabinayak006binayak')
                subject = 'Your Reminder'
                body = 'Your Reminder\n '+reminder
                msg =f"Subject: {subject}\n\n{body}"
                admin.sendmail(
                    'binayakjha36@gmail.com',
                    email,
                    msg

                )
                print("Email has also Been send")
                admin.quit()
            send()
        # Thank you
        elif 'thank you'in command: 
            print('Its my duty sir.')
            talk('Its my duty sir.')      
        # Who made you?
        elif 'who made you' in command:
            print('I am being made by Coding Jha')
            talk('I am being made by Coding Jha')
        # Wikipedia
        elif 'wikipedia' in command:
            person = command.replace('wekipedia','')
            talk("Searching in wikipedia")
            info = wikipedia.summary(person,2)
            print(info)
            talk(info)
        # Date(not date another one:))
        elif 'date' in command:
            print('sorry,I have a headache')
            talk('sorry,I have a headache')
        # Are you single
        elif 'are you single'in command:
            print('I am in a relationship with wifi')
            talk('I am in a relationship with wifi')
        # How are you
        elif 'how are you 'in command:
            print('I am fine.')
            talk('I am fine')
        # Notepad
        # Open
        elif 'open notepad' in command:
            talk('opening notepad')
            webbrowser.open(r'C:\WINDOWS\system32\notepad.exe')
        # Close
        elif 'close notepad' in command:
            talk('Ok sir, closing notepad.')
            os.system("taskkill /f /im notepad.exe")
        # Read PDF
        elif 'read pdf' in command:
            pdfname=input("enter the name of the pdf you want to make me read = ")
            book = open('../'+pdfname+'.pdf','rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            talk(f"Total numbers of pages in this book {pages}")
            
            pg = int(input("Please enter the page number: "))
            page = pdfReader.getPage(pg)
            text = page.extractText()
            talk(text)
        # IP ADDRESS
        elif 'ip address' in command:
            ip =get('https://api.ipify.org').text 
            print(f'Your IP address is {ip}')
            talk(f'Your IP address is {ip}')
        # Location
        elif 'location' in command:
            try:
                url = 'https://get.geojs.io/v1/ip/geo.json'
                geo_requests = requests.get(url)
                geo_data= geo_requests.json()
                city = geo_data['city']
                country = geo_data['country']
                talk(f"sir I think you are in {city} city of {country} country.")
            except Exception as e:
                talk("sorry sir, Due to some issue I am not able to find your location")
           # weather
        # Weather
        elif 'weather' in command:
                # talk("Enter your city name")
            # city = prompt(text="Enter your city name",title="weather")
            talk("Ok getting the weather report of your location")
            url = 'https://get.geojs.io/v1/ip/geo.json'
            geo_requests = requests.get(url)
            geo_data= geo_requests.json()
            city2 = geo_data['city']
            c = city2
            talk('weather report of '+c)
            owm = pyowm.OWM(
                'c27b3cb0e80d123b13b3cf04e962684a')
            loc = owm.weather_at_place(c)
            weather = loc.get_weather()
            # temperature
            print('-------------Weather Of '+c+' ---------------')
            temp = weather.get_temperature(unit='celsius')
            for key,val in temp.items():
                print(f'{key} => {val}')

            # humidity, wind, rain, snow
            print('------------------------------------------------')
            humidity = weather.get_humidity()
            wind = weather.get_wind()
            rain = weather.get_rain()
            snow = weather.get_snow()
            print('------------------------------------------------')
            print(f'humidity = {humidity}')
            print(f'wind = {wind}')
            print(f'rain = {rain}')
            print(f'snow = {snow}')
            # sun rise and sun set
            # sr = weather.get_sunrise_time
            # ss = weather.get_sunset_time
            # print(f'SunRise = {sr}') 
            # print(f'SunSet = {ss}')
            print('------------------------------------------------')
            # clouds and rain
            loc = owm.three_hours_forecast(c)

            clouds = str(loc.will_have_clouds())
            rain = str(loc.will_have_rain())

            print('will have clouds? ' + clouds)
            print('will have rain? ' + rain)
            print('------------------------------------------------')
            
            print("The weather report says that the temperature outside is ")
            for key,val in temp.items():
                print(f'{val}°C')
                break
            print(" and the sky being covered by clouds is "+clouds+" and the chance of raining is "+rain)                
            talk("The weather report says  that the temperature is  ")
            for key,val in temp.items():
                talk(f'{val} degree celcius')
                break
            talk(" and the sky being covered by clouds is "+clouds+" and the chance of raining is "+rain)         
        # Send email with file
        elif 'send email with file' in command:
            try:
                talk("What should be the subject ?")
                sub = prompt(text="What should be the subject = ",title="Jarvis")
                talk("Ok, what should be in body?")
                bod=prompt(text="What should be in body? = ",title="Jarvis")
                talk("Please enter the correct file path")
                file = prompt(text="Please enter the correct file path ",title="Jarvis")
                talk("Cool, To whom should I send?")
                sen =prompt(text="To whom should I send = ",title="Jarvis")
                talk("Ok, sending email to "+sen)
                msg = MIMEMultipart()
                msg['From'] = 'jha36binayak@gmail.com'
                msg['To'] = sen
                msg['Subject'] = sub
                msg.attach(MIMEText(bod,"plain"))
                #blabla
                filename = os.path.basename(file)
                attachment = open(file,"rb")
                payload = MIMEBase("application","octate-stream")
                payload.set_payload((attachment).read())
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition','attachment', filename = file)
                msg.attach(payload)
                server = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                server.starttls()
                    
                server.login('jhabinayak006@gmail.com','jhabinayak006binayak')
                text = msg.as_string()
                server.sendmail(
                    'jhabinayak006@gmail.com',
                    sen,
                    text

                )
                talk("Email has been send succesfully sir!")
                server.quit()
            except Exception as e:
                print("Sorry sir, email could not be send.")
                talk("Sorry sir, email could not be send.")
        # Send email without file
        elif 'send email' in command:
            try:
                
                talk("What should be the subject ?")
                sub = prompt(text="What should be the subject = ",title="Jarvis")
                talk("What should be the greeting ?")
                greet=prompt(text="What should be the greeting ?",title="jarvis")
                talk("Ok, what should be in body?")
                bod=prompt(text="What should be in body? = ",title="Jarvis")
                talk("To whom shoud I send?")
                sen = prompt(text="To whom shoud I send ? ",title="Jarvis")
                admin.login('jhabinayak006@gmail.com','jhabinayak006binayak')
                subject = sub
                body = bod
                greeting = greet
                msg =f"Subject: {subject}\n\n{greet}\n\n{body}\n\n from,\n Binayak Jha"
                admin.sendmail(
                    'jhabinayak006@gmail.com',
                    sen,
                    msg

                )
                print("Email has been send sir")
                talk("Email has been send sir")
                admin.quit()
            except Exception as e:
                print("Sorry sir, email could not be send.")
                talk("Sorry sir, email could not be send.")         
        # Make the system sleep, shutdown, restart
        elif 'sleep the system' in command:
            talk("Ok sir. sleeping the system sir")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif 'shutdown' in command:
            talk("Ok sir. Computer will shutdown in just 1 minute.So please close all the windows and file")
            time.sleep(5)
            talk("shutting down computer in 5 seconds.")
            time.sleep(5)
            os.system("shutdown /s /t 1")
        elif 'restart' in command:
            talk("Ok sir. Computer will restart soon")
            talk("restarting computer in 5 seconds.")
            time.sleep(5)
            os.system("shutdown /r /t 1")
        # Open camera
        elif "open camera" in command:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows() 
        # Switch the window
        elif 'change the window' in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        # Swithching the window once more
        elif "change once more" in command:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        # Tell the news
        elif 'news' in command:
            talk("Getting the news sir. Please wait")
            print("Top 10 recent news headlines")
            news()
            # talk('Ofcourse sir..')
            # news()
            # talk('Do you want to read the full news...')
            # test = take_command()
            # if 'yes' in test:
            #     talk('Ok Sir, Opening browser...')
            #     webbrowser.open(getNewsUrl())
            #     talk('You can now read the full news from this website.')
            # else:
            #     talk('No Problem Sir')
        # Screenshot
        elif 'screenshot' in command:
           talk("sir please tell me the name to save the sceenshot")
           name=prompt(text="Name of the screenshot",title="jarvis")
           talk("Ok sir please hold the screen for some seconds I am going to take a screenshot")
           time.sleep(3)
           talk('Screenshot has been taken. Please wait saving the image sir.')
           image= pyautogui.screenshot()
           image.save(f"C:\\Users\\Laptop-16\\Desktop\\{name}.png")
           talk("screenshot saved in your desktop sir.")
        # Write Something
        elif "write a note" in command:
            talk("What should i write, sir")
            note = take_command()
            file = open('jarvis.txt', 'w')
            talk("Sir, Should i include date and time")
            snfm = take_command()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         # # Remind Me
        elif "show note" in command or 'remind me' in command:
            talk("Showing Notes")
            file = open("jarvis.txt", "r").read() 
            aaa=print(file)
            talk('Your notes:')
            time.sleep(1)
            talk(file)
        
        # Notification
        elif 'notification' in command and 'facebook' in command:
            try:
                opt=Options()
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                # Pass the argument 1 to allow and 2 to block
                opt.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.geolocation": 1,
                "profile.default_content_setting_values.notifications": 1
                })
                # driver =  webdriver.Firefox(executable_path=r'C:\Users\Laptop-16\Desktop\python\geckodriver.exe')
                driver = webdriver.Chrome(chrome_options=opt,executable_path=r'C:\Users\Laptop-16\Desktop\python\chromedriver.exe')
                driver.maximize_window()
                driver.get('https://facebook.com/')
                time.sleep(5)
                driver.find_element_by_xpath('//*[@id="email"]').send_keys('9813257515')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="pass"]').send_keys('jhabinayak123binayak')
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
                time.sleep(5)
                a = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/span/div/div[2]/span/span')
                print(a.text)
                b=int(a.text)
                if b > 0:
                    print("You have some notification sir. Please check it")
                    talk("You have some notification sir")
            except Exception as e:
                print("You do not have any notification sir")
                talk("You do not have any notification sir")
        # Make an HTML document
        elif 'html' in command:
            talk("ok sir what should be the name of html file?")
            filen=take_command()
            talk("ok sir,making an html file with the name"+ filen+".html and will be in desktop")
            ff = open(f'C:\\Users\\Laptop-16\\Desktop\\{filen}.html','w')
            talk("Sir what should be the heading?")
            heading= prompt(text="Heading",title="jarvis")
            talk("Ok sir, what should be the paragraph?")
            paragraph = prompt(text="Paragraph",title="Jarvis")
            message1="""
            <html>
            <head></head>
            <body>
                <h1>"""+heading+"""</h1>
                <p>"""+paragraph+"""</p>
            </body> 
            </html>
                    """
            ff.write(message1)
            ff.close()
            talk("opening the output file sir")
            webbrowser.open_new(f'C:\\Users\\Laptop-16\\Desktop\\{filen}.html')
        # Make an excel-file
        elif "excel" in command:
            talk("What should be the name of the exel file?")
            ex1=take_command()
            talk("Ok sir, making an excel file. It will be saved in desktop")
            wb = Workbook()
            # grab the active worksheet
            ws = wb.active
            wb.save(f"C:\\Users\\Laptop-16\\Desktop\\{ex1}.xlsx")
            ans=take_command()
            talk("You can find the file in desktop")
        # Make an ms-word extension=.docx
        elif 'word' in command:
            talk("ok sir making a word file")
            talk("what should be the name?")
            filen2=take_command()
            talk("ok sir,making an word file and will be save in desktop")
            ff2 = open(f'C:\\Users\\Laptop-16\\Desktop\\{filen2}.docx','w')#os.O_RDWR
            talk("Opening the file sir")
            webbrowser.open(f"C:\\Users\\Laptop-16\\Desktop\\{filen2}.docx")
        # Minimise the window
        elif 'minimise' in command:
            pyautogui.keyDown('winleft')
            pyautogui.press('m')
            pyautogui.keyUp('winleft')
        # Ask
        elif "ask" in command:
            talk("Ok sir. You can ask any question related to any subject sir.")
            try:
                app_id = '3H9XW7-T3WXV22A5U'  # get your own at https://products.wolframalpha.com/api/
                client = wolframalpha.Client('3H9XW7-T3WXV22A5U')
                talk("Do you want to speak the question or write the question.")
                aa=take_command().lower()
                if "speak" in aa:
                    talk("Ok sir please speak the question.")
                    que=take_command().lower
                    talk("Ok sir. Please wait.")
                    res = client.query(que)
                    print("Ans:")
                    print()
                    print(next(res.results).text)
                    talk(next(res.results).text)
                    print()
                    print()
                elif "write" in aa:
                    talk("Ok sir please write the question")
                    que2=prompt(text="Question:",title="Jarvis")
                    res2 = client.query(que2)
                    talk("Ok sir. Please wait.")
                    print("Ans:")
                    print()
                    print(next(res2.results).text)
                    talk(next(res2.results).text)
                    print()
                    print()
            except Exception as e:
                talk("Sorry sir. Could not find the answer.")
        # Jarvis Clock 
        elif 'open' in command and'clock' in command:
            talk('Ok opening my clock sir')
            webbrowser.open('new.py')
        # elif 'close' in command and 'clock' in command:
            # talk('Ok sir. Closing it.')
        # where is
        # elif "where is" in command:
        #     command = command.replace("where is", "")
        #     location = command
        #     talk("User asked to Locate")
        #     talk(location)
        #     webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        # Go To Sleep
        elif  'go to sleep' in command or 'sleep now'in command:
            talk('Ok sir. You can wake me up whenever you want.')
            break
        # Else Statement
        else:
            talk("Sorry sir I didn't understand what you said. Please try again.")    
if __name__=='__main__':
    while True:
        permission = take_command()
        if 'sleep' in permission:
            print('Ok sir. Have a good day ')
            talk('Ok sir. Have a good day ')
            sys.exit()
        elif 'wake up' in permission:
            run_alexa()


# More Function Adding:
# youtube
# //*[@id="notification-count"]
#meet
# //*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]
  
