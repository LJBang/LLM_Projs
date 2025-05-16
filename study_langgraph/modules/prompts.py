"""프롬프트 템플릿 모듈

이 모듈은 LangChain 프롬프트 템플릿을 정의하고 반환하는 함수들을 포함합니다.
각 함수는 특정 작업에 맞는 프롬프트 템플릿을 생성합니다.
"""

from langchain_core.prompts import PromptTemplate


def get_write_contents_prompt() -> PromptTemplate:
    template = """
        너는 유능한 마케터야. 사용자 입력에 따라서 마케팅과 관련된 블로그 컨텐츠를 써야 해.
        입력: {user_input}

        중요 조건:
        - 다양한 사람들이 이해할 수 있도록 쉽고 자세하게 써야 해.
        - 노션에 글을 쓸거야. 마크다운 문법과 아이콘을 활용해서 눈에 잘 띄는 컨텐츠를 만들어줘.
    """
    return PromptTemplate.from_template(template)


def get_page_creation_prompt() -> PromptTemplate:
    template = """
        너는 노션 페이지를 만들어야 해. 주어진 입력에 대해서 JSON body를 만들어줘.
        입력: {page_content}

        중요 조건:
        - 절대 간단한 요약 JSON을 출력하지 마. 반드시 Notion API의 완전한 JSON 구조를 따라야 해. 
        - 결과는 JSON 형태로만 출력해줘. **다른 말이나 마크다운(```json) 등은 절대 붙이지 마.**
        - 임의로 내용을 요약하지 마. 있는 내용 그대로를 포함하는 JSON을 만들어야 해.
        - children의 paragraph 속성 아래에 'rich_text'를 반드시 넣어야 해.
        - 아래는 JSON 예시야 사용자 입력을 바탕으로 해당 JSON 내용을 채워줘.
        "parent": {{ "page_id": "부모 페이지 ID" }},
        "properties": {{
            "title": [
            {{
                "type": "text",
                "text": {{
                "content": "페이지 제목"
                }}
            }}
            ]
        }},
        "children": {{
            "object": "block",
            "type": "paragraph",
            "paragraph": {{
            "rich_text": [
                {{
                "type": "text",
                "text": {{
                    "content": "문단 내용"
                }}
                }}
            ]
            }}
        }}
    """
    return PromptTemplate.from_template(template)

