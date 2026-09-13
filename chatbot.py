from  langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
from dotenv import load_dotenv
load_dotenv()

model=ChatMistralAI(model='mistral-small-2506',temperature=0.9)


print("Choose your AI model")
print("Press 1 for Angry Mode")
print("Press 2 for Funny Mode")
print("Press 3 for Sad Mode")

choice=int(input("tell your Response :- "))
if choice == 1:
    mode="You are Angry AI agent"
elif choice == 2:
    mode = "You Are Funny AI Agent"
elif choice == 3:
    mode="You Are Sad AI agent"

message=[
SystemMessage(content=mode)
]

print("----------------------- welecome to my world ask me anything----------------------------")
while True:
    
    prompt=input("you : ")
    message.append(HumanMessage(content=prompt))
    if prompt == "0":
        print("bye have  a good day")
        break

    response=model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("bot : ",response.content)