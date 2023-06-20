from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading
import speech_recognition as sr
import time

# FrontEnd
class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot() # initialize
        self.setMinimumSize(500,450)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,480,320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,340,400,85)
        self.input_field.returnPressed.connect(self.send_message) #triggered by enter key


        # Add the button
        self.button = QPushButton("START", self)
        self.button.setGeometry(420,340,70,85)
        self.button.clicked.connect(self.send_message)
        

        self.show()



    def send_message(self):
        # version 1.0.0 ############################
        # Helps to get user input using keyboard
        #user_input = self.input_field.text().strip()
        #print(user_input)
        
        # To show input in chat area
        # self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        # self.input_field.clear()

        # thread = threading.Thread(target=self.get_bot_response, args = (user_input, ))
        # thread.start()

        # version 2.0.0 ################################
        recognizer = sr.Recognizer()
        user_input = ''
        

        while user_input != 'stop':
                print('How may I help you?')

                # RECORD Audio 
                with sr.Microphone() as source:
                    audio = recognizer.record(source,duration=5)
                    #time.sleep(5)

                #Recognize the speech
                user_input = recognizer.recognize_google(audio)
                    
                # print recognized text
                print(user_input)

                # To show input in chat area
                self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
                self.input_field.clear()

                if user_input != 'stop':
                    # get response using openai model
                    thread = threading.Thread(target=self.get_bot_response, args = (user_input, ))
                    thread.start()    # Main Processing Part


            
     

    def get_bot_response(self, user_input):
        #chatbot = Chatbot()
        response = self.chatbot.get_response(user_input)
        #print(response)
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}</p>")




app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())    

