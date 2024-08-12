from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
prompt = ChatPromptTemplate.from_messages({
    ('system','you are a private assistant , reply to user queries'),
    ('user','Question:{question}')
})
output_parser = StrOutputParser()
llm = Ollama(model='llama3.1')
chain = prompt|llm|output_parser
while(1):
    question = input(">> ")
    res = chain.invoke(question)
    print(res)