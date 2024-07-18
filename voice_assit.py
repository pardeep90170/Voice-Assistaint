import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
from googletrans import Translator


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
            return None
        
def speech_txt(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120) # value control to speed in volume
    engine.say(x) 
    engine.runAndWait()

def get_joke_in_hindi():
    joke = pyjokes.get_joke()
    translator = Translator()
    translation = translator.translate(joke, dest='hi')
    return translation.text

def search_youtube(query):
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    youtube = build('youtube', 'v3', credentials=credentials)
    request = youtube.search().list(q=query, part='snippet', maxResults=1)
    response = request.execute()

    for item in response.get('items', []):
        video_id = item['id']['videoId']
        webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
        speech_txt(f"Playing {item['snippet']['title']} on YouTube.")

if __name__ == '__main__':
    

    # if sptext().lower() == "hey prter":
    while True:
        data1 = sptext()
        if data1 is not None:
            if "your name" in data1:
                name = "my name is Heena"
                speech_txt(name)

            elif "old are you" in data1:
                age = "i am tweenty years old"
                speech_txt(age)
            
            elif "now time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speech_txt(time)
                
            elif "search music" in data1 or "search youtube" in data1:
                            speech_txt("What do you want to search for?")
                            query = sptext()
                            if query:
                                search_youtube(query)

            elif "joke" in data1:
                joke1 = get_joke_in_hindi()
                speech_txt(joke1)

            elif "exit" or "Quit" in data1:
                speech_txt("Thank you")
                break

            else:
                speech_txt("Sorry, I did not understand that.")
    # else:
    #     print("Thanks")   