from fastapi import Depends, HTTPException
from fastapi.responses import RedirectResponse

from shorts.exceptions import LinkNotFoundError
from shorts.service import LinkService
from shorts.dependencies import get_link_service

# FastAPI redirecT router

from fastapi import APIRouter, HTTPException

redirect_router = APIRouter()

@redirect_router.get("/{short_code}")
async def get_link_redirect(
    short_code: str,
    link_service: LinkService = Depends(get_link_service),
):
    short_link = await link_service.get_link(short_code)
    if not short_link:
        raise HTTPException(status_code=404, detail="Link not found")
    await link_service.record_click(short_code)
    return RedirectResponse(url=short_link.long_url)
