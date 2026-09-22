from fastapi import FastAPI

from shorts.router import router
from shorts.redirect_router import redirect_router

# FastAPI app instantiation, router registration

app = FastAPI()

app.include_router(router, prefix="/api", tags=["shorts"])

app.include_router(redirect_router, tags=["shorts"])