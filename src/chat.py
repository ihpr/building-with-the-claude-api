from anthropic import Anthropic
from dotenv import load_dotenv
from os import environ


class Chat:
    MODEL = "claude-sonnet-5"
    MAX_TOKENS = 1000

    ROLE_USER = "user"
    ROLE_ASSISTANT = "assistant"


    def __init__(self):
        load_dotenv()

        claude_api_key = environ.get('CLAUDE_API_KEY')
        self.__assert_claude_api_key(claude_api_key)

        self.__client = Anthropic(api_key=claude_api_key)
        self.__messages = []


    def add_user_message(self, text: str) -> None:
        self.__messages.append({"role": self.ROLE_USER, "content": text})


    def add_assitant_message(self, text: str) -> None:
        self.__messages.append({"role": self.ROLE_ASSISTANT, "content": text})


    def send_message(self, system_prompt=None) -> str:
        self.__assert_empty_messages()
        self.__assert_last_message_is_user_message()

        params = {
            "model": self.MODEL,
            "max_tokens": self.MAX_TOKENS,
            "messages": self.__messages,
        }

        if system_prompt:
            params["system"] = system_prompt

        message = self.__client.messages.create(**params)

        return next(
            # The loop prevents code from failure as content may have a thinking block that doesn't have a text attribute
            (block.text for block in message.content if hasattr(block, 'text')),
            ''
        )


    def __assert_claude_api_key(self, api_key: str) -> None:
        if not api_key:
            raise ValueError("Missed CLAUDE_API_KEY. Please create .env file and define it.")
    
    def __assert_empty_messages(self) -> None:
        if not self.__messages:
            raise ValueError("Empty messages")


    def __assert_last_message_is_user_message(self) -> None:
        if self.__messages[-1]["role"] is self.ROLE_ASSISTANT:
            raise ValueError("Last message in messages history is not a user message. Use add_user_message")