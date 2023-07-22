import speech_recognition as sr 
import pyttsx3 
import pywhatkit 
import datetime 
import wikipedia 
import pyjokes
from googlesearch import search
import webbrowser
import sys


listener = sr.Recognizer()

engine=pyttsx3.init() 
voices=engine.getProperty('voices') #for voice
engine.setProperty('voice',voices[1].id) #voice changer 
command='' 
done= True
say = ''
def talk(text): 
    engine.say(text) 
    engine.runAndWait() 
def take_command(): 
    global command 
    command=None
    talk("how may i help you?") 
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
    except:
        talk("Sorry, Can't catch the voice")
        
        
        
        
        
    if command!='':
        
        return command
        

def run_alexa():
    
    global done
    command=take_command()
    
    if(command==None):
        global say
        print("say start to start it again")
        talk("say start to start it again")
        try:
            with sr.Microphone() as source:
                print('listening..')
                voice = listener.listen(source)
                say = listener.recognize_google(voice)
        except:
            pass
        if 'start' in say:
            run_alexa()
        else:
            talk("Bye, Shutting down")
            print("Bye, Shutting down")
            sys.exit("Bye, Shutting down")
            
    if command==None:
        done = False
        return
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        #time=datetime.datetime.now().strftime('%H:%M')
        time=datetime.datetime.now().strftime('%I:%M %p')#%p for am/pm
        talk(time)
        print(time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
   
    else:
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        for j in search(command, tld="co.in", num=1, stop=1, pause=2):
            print(j) 
            webbrowser.open(j)
    
    command=None
    

        
while done:
    run_alexa()

