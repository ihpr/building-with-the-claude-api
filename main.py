from src.chat import Chat


def main() -> None:
    chat = Chat()

    while True:
        request = input("> ")
        if not request:
            raise ValueError("Empty user input")

        if request == 'exit' or request == 'stop':
            print("\nHave a nice day!\n")
            break

        SYSTEM_PROMPT = "Provide answers as concise as possible."

        chat.add_user_message(request)
        response = chat.send_message(system_prompt=SYSTEM_PROMPT, effort=Chat.EFFORT_MAX)
        chat.add_assitant_message(response)

        print(f"\n...\n\n{response}\n")

    return None


if __name__ == "__main__":
    main()
