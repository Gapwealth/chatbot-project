def chatbot():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input:
            print("Chatbot: Hi there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just code, but I'm doing great!")
        else:
            print("Chatbot: I don't understand that yet.")

chatbot()
