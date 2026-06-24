from typing import TypedDict
from langgraph.graph import StateGraph
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str= Field(description="title of the blog post")
    content: str = Field(description="main content of the blog post")

class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str