import os
import pygame

voice2 = 'hr-HR-GabrijelaNeural'
def speak(data):
    voice = 'zh-CN-XiaoyiNeural'
    command = f'edge-tts --voice "{voice2}" --text "{data}" --write-media "data.mp3"'
    os.system(command)
    
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    
    
    try:
        pygame.mixer.music()
        
        while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        
speak('hello steven, im athena this is a test run for my new voice')

# from custom_voice import speak custome voice not working for debugging
# import this on main