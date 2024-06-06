from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


app = FastAPI(
    title = "LLM Server",
    Version = "1.0",
    description = "LLM Server with multiple routes"
)

add_routes(
    app, 
    ChatOpenAI(),
    path="/openai"
)

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("Provide me the India rules and regulation about {topic}")
prompt1 = ChatPromptTemplate.from_template("Provide me the U.S. rules and regulation about {topic}")


add_routes(
    app,
    prompt|model,
    path="/India"
)

add_routes(
    app,
    prompt1|model,
    path="/US"
)


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port =8000)