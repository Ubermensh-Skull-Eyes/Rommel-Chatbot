# 🪖 Rommel Chatbot

A simple command-line chatbot built in Python that interacts with a locally hosted AI model via a streaming API. The chatbot is themed around **Field Marshal Erwin Rommel**, offering motivational quotes and conversational responses in a historical persona.

---

## 📌 Features

* 🔄 **Streaming Responses** – Displays AI-generated replies in real time.
* 🧠 **Persistent Chat History** – Maintains conversation context across messages.
* 🎯 **Themed Personality** – Responds as a WW2 military strategist.
* 💬 **Interactive CLI Chat Loop** – Continuous conversation until user exits.
* ⚡ **Custom Greetings & Endings** – Motivational quotes at start and exit.

---

## 🛠️ Requirements

Make sure you have the following installed:

* Python 3.x
* `requests` library

Install dependencies using:

```bash
pip install requests
```

---

## ⚙️ Configuration

The chatbot connects to a locally hosted API:

```python
url = "http://127.0.0.1:11434/api/chat"
Model = "Rommel"
```

> ⚠️ Ensure that your local server is running and supports streaming responses in the expected format.

---

## 🚀 How It Works

### 1. **Startup**

* Displays a welcome message.
* Introduces the Rommel persona.
* Calls the `Greeting()` function to generate a motivational quote.

### 2. **Chat Loop**

* Prompts the user for input.
* Sends the conversation history to the API.
* Streams and prints the response in real time.
* Stores responses in `chat_history`.

### 3. **Exit**

* Typing `exit` triggers the `Ending()` function.
* Outputs a final energizing quote and ends the session.

---

## 🧩 Code Structure

### `stream_response(payload)`

Handles API communication and streams responses line-by-line.

### `Greeting()`

Sends a prompt to generate a motivational opening message.

### `Ending()`

Generates a closing quote and farewell message.

### `chat_loop()`

Main interactive loop for continuous user input and responses.

### `main()`

Initializes the chatbot and starts the interaction flow.

---

## ▶️ Running the Program

Run the script using:

```bash
python your_script_name.py
```

---

## 💡 Example Interaction

```
Welcome to Rommel Chat bot...
General Field Marshal
Erwin Rommel

Rommel:- "Victory belongs to the bold. How can I assist you today?"

You:- What is strategy in war?
Rommel:- Strategy is the art of planning and directing...
```

---

## ⚠️ Notes

* The chatbot depends on a **locally hosted AI model/API**.
* Ensure the API returns JSON lines with the structure:

  ```json
  {
    "message": {
      "content": "text here"
    }
  }
  ```
* Errors will be displayed if the API fails to respond properly.

---

## 🧠 Future Improvements

* Implement in websites
* Improve persona realism with system prompts
* Add logging or conversation export
* Handle API errors more gracefully

---

## 📜 License

This project is open-source and free to use for educational purposes.

---

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests!

---

Enjoy commanding your conversations like a true strategist ⚔️
