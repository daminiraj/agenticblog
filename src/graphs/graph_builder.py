from langgraph.graph import StateGraph,START,END
from src.llms.openailm import OpenAiLLM
from src.states.blogstate import Blog,BlogState
from src.nodes.blog_node import BlogNode
class GraphBuilder:
    def __init__(self,llm):
        self.llm= llm
        self.graph= StateGraph(BlogState)

    def build_topic_graph(self):
        self.blog_node_obj = BlogNode(self.llm)
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
        # self.graph.add_edge("title_creation", "content_generation")
        # self.graph.add_edge("content_generation", END)

        return self.graph

    def setup_graph(self,usecase):
        if usecase == "topic":
            print("DEBUG: Condition matched! Building topic graph...")
            self.build_topic_graph()
        else:
            print("DEBUG: WARNING! Condition did NOT match. Skipping build!")
        return self.graph.compile()



