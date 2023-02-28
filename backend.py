import openai

class Chatbot:
    def __init__(self):
        # copy api key from openai website
        openai.api_key = "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" 

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = user_input,
            max_tokens = 3000,
            temperature = 0.5
        ).choices[0].text
        return response
    
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)