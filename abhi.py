

def chatbot_response(user_input):
    user_input=user_input.lower()

    if "hello"in user_input or"hi"in user_input:
            return "Hello! How  can I help you today?"
    elif "how are you"in user_input:
          return "I'm just a chatbot,but I am doing great ! How about you?"
    elif "your name"in user_input:
          return "I am Chatbot , your assistant."
    elif "time"in user_input:
          from datetime import datetime
          now=datetime.now().strftime("%H: %M: %S")
          return f"The current time is {now}" 
    elif "bye"in user_input or "exit"in user_input:
          return "Good Bye!"
    else:
          return"Sorry I don't understand"


print("Welcome to your personal Chatbot Assistant ,type bye to exit:")
while True:
      user_input=input("You:")
      response=chatbot_response(user_input)
      print("Chatbot:",response)
      if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

