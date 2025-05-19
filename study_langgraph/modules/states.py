from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TypedDict


@dataclass
class PageState(TypedDict):
    user_input: str
    page_content: Optional[str]
    notion_payload: Optional[dict]
    result: Optional[str]