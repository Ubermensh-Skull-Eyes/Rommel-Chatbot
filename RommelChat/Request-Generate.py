import requests
import json
import time
url="http://127.0.0.1:11434/api/chat"
Model = "Rommel"
chat_history=[]
def stream_response(payload):
    response = requests.post(url,json=payload,stream=True)
    if response.status_code ==200:
        print("Rommel:-",end="",flush=True)
        full_reply=""
        for line in response.iter_lines():
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
        chat_history.append({"role":"assistant","content":full_reply})
        print('\n')
    else:
        print("Error:-",response.status_code,response.text)
def Greeting():
    payload = {
        "model":Model,
        "messages":[{"role":"user","content":"Give a motivational Quote and then ask How can I help you"}]
    }
    stream_response(payload)
def Ending():
    payload = {
        "model":Model,
        "messages":[{"role":"user","content":"Give a highly energising quote and exchange goodbyes"}]
    }
    stream_response(payload)
def chat_loop():
     while True:
        print("\n")
        Question=input("Ask what you want to learn about Sir Rommel \nYou:-")
        if Question.lower()=='exit' :
            Ending()
            break
        chat_history.append({"role":"user","content":f"{Question}"})            
        payload = {
            "model":Model,
            "messages":chat_history
        }
        stream_response(payload)

def main():
    print("Welcome to Rommel Chat bot where you get the chance to learn battle tactics by our Hero of WW2 and THE DESERT FOX")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("General Field Marshal")
    time.sleep(0.5)
    print("Erwin Rommel")
    Greeting()
    print('\n')
    chat_loop()
if __name__=="__main__":
    main()