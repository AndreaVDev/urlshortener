from pydantic import BaseModel
from datetime import datetime

# Link entity and business rules

class ShortLink(BaseModel):
    long_url: str
    short_url: str
    short_code: str
    created_at: datetime
    clicks: int = 0
    is_active: bool = True

    @classmethod
    def create(cls, long_url: str, short_url: str, short_code: str) -> "ShortLink":
        """Factory method to create a new ShortLink instance."""
        return ShortLink(
            long_url=long_url,
            short_url=short_url,
            short_code=short_code,
            created_at=datetime.utcnow(),
            clicks=0,
            is_active=True
        )

