from src.chat import Chat


chat = Chat()

while True:
    request = input("> ")
    if not request:
        raise ValueError("Empty user input")

    if request == 'exit' or request == 'stop':
        print("\nHave a nice day!\n")
        break

    chat.add_user_message(request)
    response = chat.send_message()
    chat.add_assitant_message(response)

    print(f"\n...\n\n{response}\n")
