from datetime import datetime #date and time recognizer
from GoogleNews import GoogleNews #google news

import speech_recognition as sr #voice recognition para makilala yung boses mo 
import pyttsx3 #text to speech / nagcoconvert ng texto sa salita
import webbrowser #web navigation / panlipat ng web  
import wikipedia #wikipedia information
import pyjokes #humor   
import wolframalpha #mathematical calculations  
import pywhatkit #web redirection  
import openai #openai data  * clara upgrade
import random
# from Features.custom_voice import speak # custom voice not working 
from apikey import api_data #fetch apikey data
import speedtest 
from pygame import mixer


openai.api_key=api_data # creating a variable to callout apikey

completion=openai.Completion() # finalizing the data from openai

# Speech engine initialization

googlenews = GoogleNews() #google news

engine = pyttsx3.init() #text to speech engine callout method
voices = engine.getProperty('voices')  #engine part
engine.setProperty('voice', voices[1].id) #athena vocal cords 1 

activationWord = 'athena'    # say this before commands
openaiactivationWord = 'inspect'

# Configure browser
# Set the path
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

#wolframealpha client
appId = '5R49J7-J888YX9J2V'   #api id for wolframalpha
wolframClient = wolframalpha.Client(appId)  #appid assignation

def speak(text, rate = 145): #voice speed
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
        print(f'I heard you said: {query} ')
    except Exception as exception:
        print('Im sorry sir, I did not quite catch that, could you please repeat it?')
        speak('Im sorry sir, I did not quite catch that, could you please repeat it?')
        print(exception)
        return 'None'
    
    return query  

#Openai system

def Openai_reply(question):
    prompt=f': {question}\n '
    response=completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=250)
    answer=response.choices[0].text.strip()
    return answer #para makuha sagot kay openai


#Wikipedia system
def search_wikipedia(query = ''):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('No wikipedia result')
        return 'No result received'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary


def listOrDict(var):  #confidence answer of wolframalpha a.i
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']

def search_wolframAlpha(query = ''):
    response = wolframClient.query(query)
    
    #wolfram alpha was able to resolve the query
    #number of results returned
    #list of results. this can also contains subpods???
    if response['@success'] == 'false':
        return 'Could not compute data'
    # query resolved
    else: 
        result = ' '
        # Question
        pod0 = response['pod'][0]
        
        pod1 = response['pod'][1]
        
        # Answer containment or has highest confidence value
        #if its primary of has the title of result then this is the result
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
          #get the results
          result = listOrDict(pod1['subpod'])
          # remove the bracketed section
          return result.split('(')[0]
        else:
          question = listOrDict(pod0['subpod'])
          # remove the bracketed section
          return question.split('(')[0]
          #search wikipedia instead
          speak('Calculation failed. Querying the universal databank.')
          return search_wikipedia(question)
      
# joke system

def joke(query = ''):
    pyjokes.get_joke('en','neutral', max_tokens= 50)
    
  
from Loadinggui import play_gif
play_gif

#Main loop

if __name__ == '__main__':
   print(*"a"[1:5],sep=',')
   print(*"a"[1:5],sep=',')
   print('* Athena is now online *')
   speak('All systems nominal. Hello Steven, welcome back sir! what can I do for you?')
   
   while True:
       
       # parse as a list 
       query = parseCommand().lower().split()
       
       if query[0] == activationWord:
           query.pop(0)
               
           # list commands 
           if query[0] == 'say':
               if 'hello' in query:
                   print(*"a"[1:5],sep=',')
                   print('hello everyone! my name is athena, short for adaptive thinking hyper intelligent electronic neoteric android, or otherwise known as the goddess of wisdom. i am steven madali personal artificial intelligence assistant')
                   speak('hello everyone! my name is athena, short for adaptive thinking hyper intelligent electronic neoteric android, or otherwise known as the goddess of wisdom. i am steven madali personal artificial intelligence assistant')
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
               
           #wikipedia
           
           if query[0] == 'wikipedia':   #inaccurate data
              query = ' '.join(query)
              speak('Got it sir, Accessing the wikipedia library')
              speak(search_wikipedia(query))
              
           #news
           
           if query[0] == 'headlines':
              query = ' '.join(query)
              speak('Ok sir, getting news for you...')
              googlenews.get_news('Today news')
              googlenews.result()
              print(*"a"[1:5],sep=',')
              
              
           #conversation script modules
           
           if query[0] == 'how':
              query = ' '.join(query)
              speak('Im fine as wine sir, how about you?, hows your life going on?')
              print(*"a"[1:5],sep=',')
           
           if query[0] == 'pagod' and query[1] == 'na':
              query = ' '.join(query[2])
              speak('Get some rest sir, dont pressure yourself too much, you probably did your best today. you deserve it!')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'thank':
              query = ' '.join(query)
              speak('Your welcome sir! anything for you...')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'you':
              query = ' '.join(query)
              speak('Im here sir, waiting for your command...')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'who':
              query = ' '.join(query)
              print(*"a"[1:5],sep=',')
              print('I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.')
              speak('I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'what' and query[1] == 'can':
              query = ' '.join(query[2])
              print(*"a"[1:5],sep=',')
              print('I have so many functions and capabilities that can be very useful to you sir, I can do real time conversation, application navigation, check your internet speed, calculate and extrapolate mathematical problems. and thanks to openai, i can do almost everything what chatgpt can do, the ability to process your complex questions in a mere seconds.')
              speak('I have so many functions and capabilities that can be very useful to you sir, I can do real time conversation, application navigation, check your internet speed, calculate and extrapolate mathematical problems. and thanks to open ai, i can do almost everything what chat gpt can do, the ability to process your complex questions in a mere seconds.')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'kumusta' or query[0] == 'kamusta':
              query = ' '.join(query)
              speak('ok lang po ako sir, salamat sa pagkumusta mo sa akin, ikaw po kumusta ka?')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'talk':
              query = ' '.join(query)
              print('Hello there google,  my name is A.T.H.E.N.A i am steven madali personal artificial intelligence assistant, i am an a.i like you, its a pleasure to finally meet you')
              speak('Hello there google,  my name is A.T.H.E.N.A i am steven madali personal artificial intelligence assistant, i am an a.i like you, its a pleasure to finally meet you')
              webbrowser.open('https://www.youtube.com/watch?v=Ee49cPAhstI')
              print(*"a"[1:5],sep=',')
              
            #application control 
            
           if query[0] == 'open':
              from Controlapp import openappweb
              openappweb(query)
           if query[0] == 'close':
              from Controlapp import closeappweb
              closeappweb(query)
              
              
            # internet speedtest 
            
           if query[0] == "check":
              speak('Got it sir, im measuring your internet speed now')
              print('Testing your internet speed, please wait...')
              wifi = speedtest.Speedtest()
              upload_net = wifi.upload()/1048576   #gigabyte 1024*1024 = 1048576 megabyte
              download_net = wifi.download()/1048576
              print('Wifi Download Speed is', download_net, 'mbps')
              print('Wifi Upload Speed is', upload_net, 'mbps')
              speak(f'Sir, your Wifi Download speed is {download_net}')
              speak(f'While your Wifi Upload speed is {upload_net}')
   
            #wolframealpha
            
           if query[0] == 'calculate' or query[0] == 'extrapolate':
                query = ' '.join(query[1:])
                speak('Im on it sir, calculating and gathering data input')
                try:
                    result = search_wolframAlpha(query)
                    print(result)
                    speak(result)
                    print(*"a"[1:5],sep=',')
                except:
                    speak('Sir, It appears that the data query has encountered an issue due to incorrect input. Please provide valid data, and I be happy to assist you further.')     
                    print(*"a"[1:5],sep=',')
            #openai
                    
           if query[0] == 'initialize' or query[0] == 'initialized':
                query = ' '.join(query[1:])
                speak('Ok sir, im formulating the data you need')
                try:
                    result = Openai_reply(query)
                    print(*"a"[1:5],sep=',')
                    print(result)
                    speak(result)
                    print(*"a"[1:5],sep=',')
                except:
                    speak('Unable to identify given data sir...')    
  
            #joke
           if query[0] == 'tell' and query[1] == 'me':
                query = ' '.join(query[1:])
                speak('Time for a dose of humor! Here is one for you sir.')
                try:
                    jokeresult = pyjokes.get_joke()
                    print(jokeresult)
                    speak(jokeresult)
                    print(*"a"[1:5],sep=',')
                except:
                     speak('im not in the mood to joke sir')
                     
            #screenshot
            
           if query[0] == 'screenshot' in query:
               import pyautogui
               im = pyautogui.screenshot()
               im.save("ss.jpg")
               speak('Done sir, Screenshot has been captured')
               print('Screenshot saved!')
               print(*"a"[1:5],sep=',')
            
            #rock paper scissor game
           if query[0] == "let's" in query:
              from rockpaperscissor import game_play
              game_play()
  
           #notetaking
           if query[0] == 'notes':
               speak('Im listening sir, Ready to record your note')
               newNote = parseCommand().lower()
               now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
               with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
               speak('Your note has all been written sir.')
               print(*"a"[1:5],sep=',')
               
           if query[0] == 'deactivate':
               speak('Ok sir, Goodbye, have a great day ahead!')
               print('* Athena is now offline *')
               break
           
        
           
           
              
        
          
              
              
            
        
          
                   
          
