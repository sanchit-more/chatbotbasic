#Rule based ai python chatbots

import datetime
import time
name=(input(" Swagat hai!,Enter your name : "))

presenthour= datetime.datetime.now().hour

if 5<=presenthour <=11:
    print("Good morning ", name)

elif 11<=presenthour <=17:
    print("Good afternoon",name)

elif 17<=presenthour <=20:    
    print("Good night",name)

else:
    print("Good night!")


print("Namste! Welcome to the chatbot")
print("You can ask basic questions!, Type Bye to exit the bot")

#chat bot memory creation { dictionary of responses}

responses={
    "hello": "heyy how can i help you ",
    "how are you":"I am fine ,Thank You",
    "Who are you":"I am your Ai chatbot",
    "what is python": "Python is a high level language",
    "happy":"Great to hear this "

}

#method/functions to get response of chatbot

def getResponseofBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]

    return "I am not able to tell that yet . I am still in learning mode"

#take yoser input 

while True:
    userInput=input("please ask your question:")
    reply=getResponseofBot(userInput)
    print("Bot Response:",reply)
    
    if "bye" in userInput.lower():
        break