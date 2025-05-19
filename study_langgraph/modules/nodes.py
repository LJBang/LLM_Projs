from modules.chains import create_page_chain, write_blog_contents
from modules.states import PageState
import requests
import os
import json
import re


# a. LangChain으로 블로그 컨텐츠 작성
def call_writer_node(state: PageState) -> PageState:
    print(" Writing Contents...")
    page_content = write_blog_contents().invoke({"user_input": state["user_input"]})
    print(page_content)
    return {**state, "page_content": page_content}

# b. LangChain으로 payload 생성
def parse_node(state: PageState) -> PageState:
    print("🧠 Parsing input with LangChain...")
    output_str = create_page_chain().invoke({"page_content": state["page_content"]})
    print(output_str)
    output_str = re.sub(r"```json|```", "", output_str).strip()
    

    notion_json = json.loads(output_str)
    return {**state, "notion_payload": notion_json}

# c. Notion API 호출
def call_notion_node(state: PageState) -> PageState:
    print("📤 Calling Notion API...")
    NOTION_PARENT_ID = os.environ["NOTION_PARENT_ID"]
    NOTION_API_KEY = os.environ["NOTION_API_KEY"]

    payload = state["notion_payload"]
    payload["parent"] = {"page_id": NOTION_PARENT_ID}

    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload)

    
    if res.status_code == 200:
        return {**state, "result": "success ✅"}
    else:
        return {**state, "result": f"failed ❌: {res.status_code}, {res.text}"}


