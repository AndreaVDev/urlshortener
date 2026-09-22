from fastapi import Depends, FastAPI

from shorts.schemas import CreateLinkRequest, LinkResponse
from shorts.service import LinkService
from shorts.dependencies import get_link_service

# FastAPI app instantiation, router registration

app = FastAPI()

@app.post("/api/links", response_model=LinkResponse)
async def create_link(
    link: CreateLinkRequest,
    link_service: LinkService = Depends(get_link_service),
):
    short_link = await link_service.create_link(link.long_url)
    return LinkResponse(
        long_url=short_link.long_url,
        short_url=short_link.short_url,
        short_code=short_link.short_code,
        created_at=short_link.created_at,
        clicks=short_link.clicks,
    )
   

    
