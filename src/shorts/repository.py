from abc import ABC, abstractmethod

from shorts.domain import ShortLink

# Abstract interface and MongoLinkRepository implementation for link storage and retrieval

class LinkRepository(ABC):
    @abstractmethod
    async def save(self, link: ShortLink) -> ShortLink | None:
        pass

    @abstractmethod
    async def get_link(self, short_code: str) -> ShortLink | None:
        pass

    @abstractmethod
    async def record_click(self, short_code: str) -> None:
        pass


class MongoLinkRepository(LinkRepository):
    def __init__(self, db):
        self.db = db

    async def save(self, link: ShortLink) -> ShortLink | None:
        # Implementation for saving a link to MongoDB
        await self.db.insert_one(link.model_dump())
        return link
    
    async def get_link(self, short_code: str) -> ShortLink | None:
        # Implementation for retrieving a link from MongoDB
        record = await self.db.find_one({"short_code": short_code})
        if record:
            return ShortLink(
                long_url=record["long_url"],
                short_url=record["short_url"],
                short_code=record["short_code"],
                created_at=record["created_at"],
                clicks=record["clicks"],
                is_active=record["is_active"],
            )
        return None

    async def record_click(self, short_code: str) -> None:
        await self.db.update_one(
            {"short_code": short_code},
            {"$inc": {"clicks": 1}}
        )