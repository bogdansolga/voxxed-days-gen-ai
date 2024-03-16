from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def main():
    load_dotenv()
    invokeChatGPT()

def invokeChatGPT():
    chat = ChatOpenAI(temperature=1)
    systemMessage = SystemMessage("Act as a friendly and funny comedian")
    humanMessage = HumanMessage("Explain the AI domain, in a few funny sentences")
    promptMessage = [systemMessage, humanMessage]

    aiMessage = chat.invoke(promptMessage)
    print(aiMessage.content)

if __name__ == '__main__':
    main()
