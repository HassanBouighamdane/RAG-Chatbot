# Test invocation and the use of the model with langchain
from chatbot import chat_model
from chatbot import review_chain
'''
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
'''
#This part is for using prompts template

context = "I had a great stay!"
question = "Did anyone have a positive experience?"

print(review_chain.invoke({"context": context,"question":question}))
#print(review_prompt_template.format_messages(context=context, question=question))
