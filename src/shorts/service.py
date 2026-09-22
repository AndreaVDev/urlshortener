# Orchestration
from shorts.domain import ShortLink
from shorts.exceptions import LinkNotFoundError, ShortCodeGenerationError
from shorts.repository import LinkRepository
from shorts.utils import generate_short_code, generate_short_url


class LinkService:
    def __init__(self, repository: LinkRepository):
        self.repository = repository

    async def create_link(self, link: str) -> ShortLink:
        short_code_found = False

        # generate short code using utils
        for _ in range(5):  # Try up to 5 times to generate a unique short code
            short_code = generate_short_code()
            search_existing_short_code = await self.repository.get_link(short_code)
            if not search_existing_short_code:
                short_code_found = True
                break

        # generate link using Link entity
        if short_code_found:
            short_link = ShortLink.create(
                long_url=link,
                short_code=short_code,
                short_url=generate_short_url(short_code),
            )
        if not short_code_found:
            raise ShortCodeGenerationError("Failed to generate a unique short code after multiple attempts.")
        await self.repository.save(short_link)
        return short_link

    async def get_link(self, short_code: str) -> ShortLink | None:
        return await self.repository.get_link(short_code)

    async def record_click(self, short_code: str) -> None:
        search_existing_short_code = await self.repository.get_link(short_code)
        if not search_existing_short_code:
            raise LinkNotFoundError("Link not found")
        await self.repository.record_click(short_code)