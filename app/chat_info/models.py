from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime as dt

class ChatType(str, Enum):
    group = 'group'
    channel = 'channel'
    supergroup = 'supergroup'

class ChatInfoParams(BaseModel):
    chat_id: Optional[str] = None
    name: Optional[str] = None
    chat_type: Optional[ChatType] = None
    language: Optional[list[str]] = None
    category: Optional[list[str]] = None
    label: Optional[list[str]] = None
    num: Optional[int] = 100

class UpdateChatInfo(BaseModel):
    chat_id: str  # required
    name: str = None
    chat_type: ChatType = None
    language: list[str] = None
    category: list[str] = None
    label: list[str] = None

class Chat(BaseModel):
    chat_id: str  # fixed can't be changed
    name: str
    chat_type: ChatType
    language: list[str]
    category: list[str]
    label: list[str]
    created_timestamp: dt = Field(default_factory=lambda: dt.now())
    updated_timestamp: dt = Field(default_factory=lambda: dt.now())

    def update(self, params: UpdateChatInfo):
        if params.name:
            self.name = params.name
        if params.chat_type:
            self.chat_type = params.chat_type
        if params.language:
            self.language = params.language
        if params.category:
            self.category = params.category
        if params.label:
            self.label = params.label

        self.updated_timestamp = dt.now()
        