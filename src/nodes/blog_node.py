from src.states.blogstate import BlogState,Blog
from langchain_core.messages import  SystemMessage,HumanMessage
class BlogNode:
    def __init__(self,llm):
        self.llm= llm

    def title_creation(self, state:BlogState):
        if "topic" in state and state["topic"] :
            prompt=""" You are an expert blog content writer.USe markdown formatting.
                        Generete blog title from {topic}.
                        This topic should be creative and SEO friendly
            """
            system_message=prompt.format(topic=state["topic"])
            response= self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}

    def content_generation(self, state:BlogState):
        if "topic" in state and state["topic"] :
            prompt=""" You are an expert blog content writer.USe markdown formatting.
                        Generate a detailed blog content with the detailed breakdown for {topic}.
                        This topic should be creative and SEO friendly
            """
            system_message=prompt.format(topic=state["topic"])
            response= self.llm.invoke(system_message)
            return {"blog":{"title":state['blog']['title'],"content":response.content}}

    def translation(self, state:BlogState):
        translation_prompt=""" Translate the following content into {current_language}.
                    Maintain the original tone, style and formatting.
                    Adapt cultural references and idioms to be appropriate for  {current_language}.
                    
                    ORIGINAL_CONTENT:{blog_content}
        """
        blog_content=state["blog"]["content"]
        print(f"current_language:{state['current_language']}")
        message=[HumanMessage(translation_prompt.format(current_language=state["current_language"],blog_content=blog_content))]
        translation_content=self.llm.with_structured_output(Blog).invoke(message)
        return {"blog": {"title": state['blog']['title'], "content": translation_content.content}}

    def route(self,state:BlogState):
        return {"current_language":state["current_language"]}

    def route_decision(self,state:BlogState):
        if state["current_language"] =="hindi":
            return "hindi"
        elif state["current_language"] =="french":
            return "french"
        return state["current_language"]




