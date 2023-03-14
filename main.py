from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading

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
        self.button = QPushButton("Send", self)
        self.button.setGeometry(420,340,70,85)
        self.button.clicked.connect(self.send_message)
        

        self.show()


    # Main Processing Part
    def send_message(self):
        # Helps to get user input using app
        user_input = self.input_field.text().strip()
        #print(user_input)

        # To show input in chat area
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args = (user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        #chatbot = Chatbot()
        response = self.chatbot.get_response(user_input)
        #print(response)
        self.chat_area.append(f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}</p>")




app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())    
#end

