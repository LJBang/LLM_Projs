from langgraph.graph.state import StateGraph
from dotenv import load_dotenv
from base_workflow import BaseWorkflow
from modules.nodes import parse_node, call_notion_node, call_writer_node
from modules.states import PageState


class MainWorkflow(BaseWorkflow):
    def __init__(self, state):
        """
        Args:
            state (StateGraph): Workflow에서 사용할 상태 클래스
        """
        super().__init__()
        self.state = state

    def build(self):
        builder = StateGraph(self.state)

        builder.add_node("write", call_writer_node)
        builder.add_node("parse", parse_node)
        builder.add_node("call_notion", call_notion_node)

        builder.set_entry_point("write")
        builder.add_edge("write", "parse")
        builder.add_edge("parse", "call_notion")
        builder.add_edge("call_notion", "__end__")

        workflow = builder.compile()
        workflow.name = self.name
        return workflow



load_dotenv()
# 마케팅 Workflow 인스턴스 생성
workflow = MainWorkflow(PageState)
input_state = {
    "user_input": "신생 회사가 할 수 있는 마케팅 방법에 대한 블로그 글을 써줘"
}

final_state = workflow().invoke(input_state)
print("📄 결과:", final_state["result"])
