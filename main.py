from langchain_intro.chatbot import chat_model
from langchain.schema.messages import SystemMessage, HumanMessage

messages = [
     SystemMessage(
         content="""You're an assistant knowledgeable about healthcare. Only answer healthcare-related questions. """
     ),
    HumanMessage(content="What is blood pressure ?"),
]
for chunk in chat_model.stream(messages):
    print(chunk.text(), end="")

#response=chat_model.invoke("can you explain the rust programming language in few words.")
#print(response.content)
