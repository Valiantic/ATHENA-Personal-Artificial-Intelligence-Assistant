import pyttsx3 #text to speech
import speech_recognition as sr
import random

from pygame import mixer
mixer.init()

engine = pyttsx3.init()
voices = engine.getProperty('voices')  #engine part
engine.setProperty('voice', voices[1].id)

def speak(text, rate = 145):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
    
def parseCommand():
    listener = sr.Recognizer()
    print(*"a"[1:5],sep=',')
    print('A.T.H.E.N.A is Listening...')
    
    with sr.Microphone() as source:   # function to use microphone
         listener.pause_threshold = 2
         input_speech = listener.listen(source)
         
    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')  #google api to understand
        print(f'You choose: {query} ')
    except Exception as exception:
        print('Im sorry sir, I did not quite catch that, could you please repeat it?')
        speak('Im sorry sir, I did not quite catch that, could you please repeat it?')
        print(exception)
        return 'None'
    
    return query  

def game_play():
    speak("Ok sir, i've been waiting for you to ask for that, let's play rock paper and scissor then")
    print(*"a"[1:5],sep=',')
    mixer.music.load("RPS INTRO.mp3")
    mixer.music.play()
    print("* YOU HAVE CHALLENGED ATHENA TO A GAME OF ROCK PAPER AND SCISSORS! *")
    print(*"a"[1:5],sep=',')
    i = 0 
    Steven_score = 0
    Athena_score = 0
    
    while(i<=3):
        choose = ("rock","paper","scissor") #TUPLE
        athena_choose = random.choice(choose) #randomization of athena
        query = parseCommand().lower() #answer to convert into lower words
        if(query == "rock"): #answer of the user
            if (athena_choose == "rock"):
                print("Athena chooses: ROCK")
                speak("Rock")
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
            elif(athena_choose == "paper"):
                print("Athena chooses: PAPER")
                speak("Paper")
                Athena_score += 1 
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
                
            else:
                print("Athena chooses: SCISSOR")
                speak("Scissors")
                Steven_score += 1 
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
                
        elif(query == "paper"): #answer of the user
            if (athena_choose == "rock"):
                print("Athena chooses: ROCK")
                speak("Rock")
                Steven_score += 1
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
            elif(athena_choose == "paper"):
                print("Athena chooses: PAPER")
                speak("Paper")
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
                
            else:
                print("Athena chooses: SCISSOR")
                speak("Scissors")
                Athena_score += 1 
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
                
        elif (query == "scissors" or query == "scissor"): #answer of the user
            if (athena_choose == "rock"):
                print("Athena chooses: ROCK")
                speak("Rock")
                Athena_score += 1
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
            elif(athena_choose == "paper"):
                print("Athena chooses: PAPER")
                speak("Paper")
                Steven_score += 1 
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
                
            else:
                print("Athena chooses: SCISSOR")
                speak("Scissors")
                print(f"Score:- Me :- {Steven_score} : Com :- {Athena_score}")
        i += 1 
        
       
    speak("that's fun sir, let's try again sometimes")
    print(f"FINAL SCORE :- ME :- {Steven_score} : COM :- {Athena_score}")
           

           
        
   
              
                