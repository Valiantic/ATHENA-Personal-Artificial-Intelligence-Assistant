from datetime import datetime #date and time recognizer
from GoogleNews import GoogleNews #google news
import speech_recognition as sr #voice recognition / pip install speech_recognition
import pyttsx3 #text to speech for ai / pip install pyttsx3
import webbrowser #web navigation / pip install webbrowser
import wikipedia #brain modules / pip install wikipedia
import wolframalpha #api calculation / pip install wolframalpha
import pywhatkit #for opening websites use it later / pip install pywhatkit
import openai
from apikey import api_data

openai.api_key=api_data # new

completion=openai.Completion() # new

# Speech engine initialisation

googlenews = GoogleNews() #google news
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
activationWord = 'athena'
openaiactivationWord = 'inspect'

# Configure browser
# Set the path
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

#wolframealpha client
appId = '5R49J7-J888YX9J2V'   #api id for wolframalpha
wolframClient = wolframalpha.Client(appId)  #appid assignation

def speak(text, rate = 145):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Waiting for your command sir...')
    
    with sr.Microphone() as source:   # function to use microphone
         listener.pause_threshold = 2
         input_speech = listener.listen(source)
         
    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')  #google api to understand
        print(f'The input speech was: {query} ')
    except Exception as exception:
        print('Im sorry sir, I did not quite catch that, could you please repeat it?')
        speak('Im sorry sir, I did not quite catch that, could you please repeat it?')
        print(exception)
        return 'None'
    
    return query  

#Openai system

def Openai_reply(question):
    prompt=f': {question}\n '
    response=completion.create(prompt=prompt, engine="text-davinci-002", max_tokens=500)
    answer=response.choices[0].text.strip()
    return answer


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

def listOrDict(var):  #method for dictionary
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

#Main loop

if __name__ == '__main__':
   speak('All systems nominal. Hello Steven, welcome back sir! what can I do for you?')
   
   while True:
       # parse as a list 
       query = parseCommand().lower().split()
       
       if query[0] == activationWord:
           query.pop(0)
               
           # list commands 
           if query[0] == 'say':
               if 'hello' in query:
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
              speak('Im fine as wine sir, how about you?...')
              print(*"a"[1:5],sep=',')
           
           if query[0] == 'pagod' and query[1] == 'na':
              query = ' '.join(query[2])
              speak('Get some rest sir, dont pressure yourself too much, you probably did your best today. you deserve it!')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'thank':
              query = ' '.join(query)
              speak('Your welcome sir! anything for you...')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'who':
              query = ' '.join(query)
              speak('I was created by the brilliant aspiring computer scientist, steven gabriel madali, a second year student in cavite state university carmona campus, taking a bachelors degree in information technology.')
              print(*"a"[1:5],sep=',')
              
           if query[0] == 'what' and query[1] == 'can':
              query = ' '.join(query[2])
              speak('I have so many functions and capabilities that can be very useful to you sir, I can do real time conversation, website navigation, search specific information on wikipedia, note recording, and my specialty, the ability to calculate and extrapolate, mathematical or logical, raw data. im also powered by openai api, meaning to say i can do anything what chatgpt can do')
              print(*"a"[1:5],sep=',')
              
              
            #wolframealpha
            
           if query[0] == 'calculate' or query[0] == 'extrapolate':
                query = ' '.join(query[1:])
                speak('Im on it sir, calculating and gathering data input')
                try:
                    result = search_wolframAlpha(query)
                    speak(result)
                except:
                    speak('Sir, It appears that the data query has encountered an issue due to incorrect input. Please provide valid data, and I be happy to assist you further.')     
                    
            #openai
                    
           if query[0] == 'inspect':
                query = ' '.join(query[1:])
                speak('Ok sir, querying the universal databank...')
                try:
                    result = Openai_reply(query)
                    print(result)
                    speak(result)
                except:
                    speak('Unable to identify given data sir...')    
  
           #notetaking
           if query[0] == 'notes':
               speak('Im listening sir, Ready to record your note')
               newNote = parseCommand().lower()
               now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
               with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
               speak('Your note has all been written sir.')
               
           if query[0] == 'power' and query[1] == 'down':
               speak('Ok sir, Goodbye, have a great day ahead!')
               break
           
           
                
           
           
              
        
          
              
              
            
        
          
                   
          
