import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker 1.1 created by Utkarsha Jadhav")
    
    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            print("Stopped!!!")
            break
        engine.say(x)
        engine.setProperty('rate', 145)     # Speed of speech
        engine.setProperty('volume', 0.9)   # Volume (0.0 to 1.0)
        engine.runAndWait()
