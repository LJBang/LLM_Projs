from langchain_openai import ChatOpenAI
import os

def get_openai_model() -> ChatOpenAI:
    return ChatOpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        model_name="gpt-4",  # 모델 이름 (gpt-4 사용)
        temperature=0.7,  # 창의성 조절 (0.7은 균형 잡힌 창의성)
        max_tokens=6000,  # 최대 토큰 수
    )
