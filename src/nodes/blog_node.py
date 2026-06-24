from src.states.blogstate import BlogState
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




