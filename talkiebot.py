from datetime import datetime

hour = datetime.now().hour
if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

def chatbot():
    print(f"🤖 ChatBot: {greeting}! I'm TalkieBot, here to have a fun little chat with you!")
    print("🤖 ChatBot: You can ask me about hobbies, favorite food, books, movies, or just say hi 😊")
    print("🤖 ChatBot: Type 'bye' anytime to exit.\n")

    name = input("🤖 ChatBot: First things first, what's your name? ")
    print(f"🤖 ChatBot: Nice to meet you, {name}! 🌟")

    while True:
        user_input = input("You: ").lower().strip()
        
        if not user_input:
            print("🤖 ChatBot: Please type something 😊")
            continue
        if user_input in ["hi", "hello", "hey"]:
            print("🤖 ChatBot: Hi again! How can I brighten your day today?")
        elif user_input in ["how are you", "how are you doing"]:
            print("🤖 ChatBot: I'm doing great! Just waiting to have a nice chat with someone like you 😊")
        elif user_input in ["what is your name", "who are you"]:
            print("🤖 ChatBot: I'm your friendly chatbot TalkieBot. built using Python — no caffeine, just pure logic! ☕🤖")
        elif "your creator" in user_input:
            print("🤖 ChatBot: I was created by a Python developer who loves making code fun and interactive! 💻✨")
        elif "hobby" in user_input:
            hobby = input("🤖 ChatBot: I'd love to know — what is your favorite hobby? ")
            print(f"🤖 ChatBot: {hobby.capitalize()} sounds like an awesome way to spend your free time!")
        elif "food" in user_input:
            food = input("🤖 ChatBot: Yum! What's your favorite food? ")
            print(f"🤖 ChatBot: Oh, {food}? That sounds delicious! I wish I could try it too 😅")
        elif "job" in user_input or "career" in user_input:
            job = input("🤖 ChatBot: If you could do anything, what would your dream job be? ")
            print(f"🤖 ChatBot: A {job}? That’s a fantastic choice! Follow your dreams, {name} 🚀")
        elif "movie" in user_input or "book" in user_input:
            media = input("🤖 ChatBot: Quick question — do you prefer movies or books? ")
            if media.lower() == "movies":
                print("🤖 ChatBot: Movies are a great way to relax and escape reality 🎬")
            elif media.lower() == "books":
                print("🤖 ChatBot: Books take you to new worlds without moving an inch 📚✨")
            else:
                print("🤖 ChatBot: That's an interesting pick! Everyone has unique tastes.")
        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖 ChatBot: You're very welcome, always happy to chat with you! 💙")
        elif user_input in ["bye", "exit", "quit"]:
            print(f"🤖 ChatBot: Goodbye, {name}! It was a pleasure chatting with you. Take care! 👋😊")
            break
        else:
            print("🤖 ChatBot: Hmm... I didn't quite catch that. Try asking me about your hobbies, food, or dreams!")
chatbot()
