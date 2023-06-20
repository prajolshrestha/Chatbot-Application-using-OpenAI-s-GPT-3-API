import openai

class Chatbot:
    def __init__(self):
        # copy api key from openai website
        openai.api_key = "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" #not working right now/ you can buy from openai.com

    def get_response(self, user_input):
        # response = openai.Completion.create(
        #     engine = "text-davinci-003",
        #     prompt = user_input,
        #     max_tokens = 3000,
        #     temperature = 0.5
        # ).choices[0].text

        response = 'Open AI has no free version of model right now! For more details go to openai.com'

        return response
    
