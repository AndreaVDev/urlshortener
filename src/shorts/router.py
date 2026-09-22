from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from shorts.exceptions import ShortCodeGenerationError
from shorts.schemas import CreateLinkRequest, LinkResponse
from shorts.service import LinkService
from shorts.dependencies import get_link_service

# FastAPI routes

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/links", response_model=LinkResponse)
async def create_link(
    link: CreateLinkRequest,
    link_service: LinkService = Depends(get_link_service),
):
    try:
        short_link = await link_service.create_link(link.long_url)
    except ShortCodeGenerationError:
        raise HTTPException(status_code=503, detail="...")    
    return LinkResponse(
        long_url=short_link.long_url,
        short_url=short_link.short_url,
        short_code=short_link.short_code,
        created_at=short_link.created_at,
        clicks=short_link.clicks,
    )


@router.get("/links/{short_code}", response_model=LinkResponse)
async def get_link(
    short_code: str,
    link_service: LinkService = Depends(get_link_service),
):
    short_link = await link_service.get_link(short_code)
    if not short_link:
        raise HTTPException(status_code=404, detail="Link not found")
    return LinkResponse(
        long_url=short_link.long_url,
        short_url=short_link.short_url,
        short_code=short_link.short_code,
        created_at=short_link.created_at,
        clicks=short_link.clicks,
    )

