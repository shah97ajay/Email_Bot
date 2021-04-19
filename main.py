import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk (text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):  
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('email_id', 'password') # enter your email id and password
    email = EmailMessage()
    email['from'] = 'shah97ajay@gmail.com'
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {'demo': 'yikode9437@zcai66.com'
}

def get_email_info():
    talk('to whom you want to send eamil')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('email sent successfully')
    talk('do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()