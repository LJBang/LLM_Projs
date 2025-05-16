from modules.models import get_openai_model
from modules.prompts import get_page_creation_prompt, get_write_contents_prompt
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSerializable

def create_page_chain() -> RunnableSerializable:
    model = get_openai_model()
    prompt = get_page_creation_prompt()

    return prompt | model | StrOutputParser()


def write_blog_contents() -> RunnableSerializable:
    model = get_openai_model()
    prompt = get_write_contents_prompt()

    return prompt | model | StrOutputParser()
