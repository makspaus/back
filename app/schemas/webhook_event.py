from pydantic import BaseModel
from typing import Any
from uuid import UUID
from datetime import datetime

class WebhookEventBase(BaseModel):
    event_type: str
    payload: Any

class WebhookEventRead(WebhookEventBase):
    id: UUID
    received_at: datetime

    model_config = {
        "from_attributes": True  # pydantic v2
    }
