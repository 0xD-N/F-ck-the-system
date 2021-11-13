import speech_recognition as sr
import pywhatkit as kit
from textblob import *
from nltk.tokenize import sent_tokenize, word_tokenize
import shutil
import time
import os
import glob
import requests
from mega import Mega
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source,timeout = 900)
        
        
       
        try:
            x = (r.recognize_google(audio))
           
            z = TextBlob(x)
            a = (z.correct())
            print(z.correct())
            a = str(a)
            if x == "terminate listening":
                break
            
            
                
            with open('person.txt', 'a') as f:

                lines = sent_tokenize(x)

                for line in lines:
                    f.write(line)
                    f.write('\n')
                    NAME = "notes.png"
                      #kit.text_to_handwriting(line, NAME)
                    if os.path.exists('notes.png'):

                        lmao = 'notes_{}.png'.format(int(time.time()))
                        kit.text_to_handwriting(line, lmao)
                        email = 'your registered email address'
                        password = 'Your mega passowrd'
                        mega = Mega()
                        m = mega.login(email, password)
                          # login using a temporary anonymous account
                        arr_txt = [x for x in os.listdir() if x.endswith(".png")]
                        for file in arr_txt:
                            folder = m.find('Misc')
                            f = m.upload(file, folder[0])
                        m = (m.get_upload_link(f))
                        url = "https://www.fast2sms.com/dev/bulk"
                        payload = "sender_id=FSTSMS&message=" + m + "&language=english&route=p&numbers=yournumber here"
                        headers = {
                        'authorization': "Your fast2sms key",
                        'Content-Type': "application/x-www-form-urlencoded",
                        'Cache-Control': "no-cache",
                        }
                        response = requests.request("POST", url, data=payload, headers=headers)
                        print(response.text)
                        continue



                    else:
                      kit.text_to_handwriting(line, NAME)
                
                
                
                        
                        
                    
                    

        except sr.UnknownValueError:
            print("Could not understand audio")

arr_txt = [x for x in os.listdir() if x.endswith(".png")]
print(arr_txt)

