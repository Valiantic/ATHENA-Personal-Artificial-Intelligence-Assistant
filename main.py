from datetime import datetime #date and time recognizer
import speech_recognition as sr #voice recognition
import pyttsx3 #text to speech for ai
import webbrowser #web navigation
import wikipedia #brain modules
import wolframalpha #api calculation
import pywhatkit #for opening websites use it later

# Speech engine initialisation

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
activationWord = 'athena'

# Configure browser
# Set the path
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))


def speak(text, rate = 145):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command sir...')
    
    with sr.Microphone() as source:   # function to use microphone
         listener.pause_threshold = 2
         input_speech = listener.listen(source)
         
    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')  #google api to understand
        print(f'The input speech was: {query} ')
    except Exception as exception:
        print('I did not quite catch that sir')
        speak('I did not quite catch that sir')
        print(exception)
        return 'None'
    
    return query  

#Main loop

if __name__ == '__main__':
   speak('All systems nominal. hello steven, welcome back sir!')
   
   while True:
       # parse as a list 
       query = parseCommand().lower().split()
       
       if query[0] == activationWord:
           query.pop(0)
               
           # list commands 
           if query[0] == 'say':
               if 'hello' in query:
                   speak('hello everyone! my name is athena, im steven madali personal artificial intelligence assistant')
               else:
                   query.pop(0) # remove say
                   speech = ' '.join(query)
                   speak(speech)
                   
           #navigation
           if query[0] == 'go' and query[1] == 'to':
               speak('Ok sir, opening...')
               query = ' '.join(query[2:])
               webbrowser.get('chrome').open_new(query)
               
           if query[0] == 'play':
              speak('Opening youtube sir')
              pywhatkit.playonyt(query)
              
           if query[0] == 'youtube':
              speak('Opening youtube sir')
              webbrowser.open('www.youtube.com')
              
           if query[0] == 'how' and query[1] == 'are' and query[2] == 'you':
               speak('Im fine as wine sir... how about you?')
               query = ' '.join(query[3:])
               
        
          
              
              
            
        
          
                   
          