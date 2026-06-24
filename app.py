import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.openailm import OpenAiLLM

import os
from dotenv import load_dotenv
load_dotenv()

app= FastAPI()

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

@app.post("/blogs")
async def create_blogs(request:Request):
    data= await request.json()
    topic=data.get("topic","")
    language = data.get("language", "")
    openAiLLM = OpenAiLLM()
    openaillm= openAiLLM.get_llm()
    graph_builder= GraphBuilder(openaillm)
    if language and topic:
        graph = graph_builder.setup_graph(usecase="language")
        state = graph.invoke({"topic": topic,"current_language":language.lower()})
    elif topic:
        graph=graph_builder.setup_graph(usecase="topic")
        state= graph.invoke({"topic":topic})
    return {"data":state}


if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)


