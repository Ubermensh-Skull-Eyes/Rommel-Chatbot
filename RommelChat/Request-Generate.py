import requests
import json
import time
class ChatBot:
    def __str__(self):
        return "Welcome to ChatBot chose any one to continue:- Rommel"
    def __init__(self,model:str):
        self.url="http://127.0.0.1:11434/api/chat"
        self.model = model
        self.chat_history=[]
    def stream_response(self,payload):
        response = requests.post(self.url,json=payload,stream=True)
        if response.status_code ==200:
            print(f"{self.model}:-",end="",flush=True)
            self.decode(response.iter_lines())
        #     for line in response.iter_lines():
        #         if line:
        #             try:
        #                 decoded_text = line.decode("utf-8")
        #                 result = json.loads(decoded_text)
        #                 if "message" in result:        
        #                     generted_text = result["message"].get("content","")
        #                     print(generted_text,end="",flush=True)
        #                     full_reply=full_reply+generted_text

        #             except json.JSONDecodeError:
        #                 continue
        #     self.chat_history.append({"role":"assistant","content":full_reply})
        #     print('\n')
        else:
            print("Error:-",response.status_code,response.text)
    def decode(self,message):
        full_reply=""
        for line in message:
            if line:
                try:
                    decoded_text = line.decode("utf-8")
                    result = json.loads(decoded_text)
                    if "message" in result:        
                        generted_text = result["message"].get("content","")
                        print(generted_text,end="",flush=True)
                        full_reply=full_reply+generted_text
                except json.JSONDecodeError:
                    continue
        self.chat_history.append({"role":"assistant","content":full_reply})
        print('\n')

    def Greeting(self):
        payload = {
            "model":self.model,
            "messages":[{"role":"user","content":"Give a motivational Quote and then ask How can I help you"}]#Change message for other bots
        }
        self.stream_response(payload)
    def Ending(self):
        payload = {
            "model":self.model,
            "messages":[{"role":"user","content":"Give a highly energising quote and exchange goodbyes"}]#Change message for other bots
        }
        self.stream_response(payload)
    def chat_loop(self):
        while True:
            print("\n")
            Question=input(f"Ask what you want to learn about Sir {self.model} \nYou:-")
            if Question.lower()=='exit' :
                self.Ending()
                break
            self.chat_history.append({"role":"user","content":f"{Question}"})            
            payload = {
                "model":self.model,
                "messages":self.chat_history
            }
            self.stream_response(payload)

    def main(self):
        print("Welcome to Chat bot where you get the chance to learn battle tactics by our Hero of WW2 and THE DESERT FOX")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("General Field Marshal")
        time.sleep(0.5)
        print("Erwin Rommel")
        self.Greeting()
        print('\n')
        self.chat_loop()
if __name__=="__main__":
    chat = ChatBot("Rommel")
    chat.main()