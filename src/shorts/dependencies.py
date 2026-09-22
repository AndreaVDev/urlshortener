# Depends provides a way to declare dependencies for your FastAPI application. 
# It allows you to define functions that can be used as dependencies for your route handlers,
#  and FastAPI will automatically handle the injection of those dependencies when the route is called.\
from fastapi import Depends
from typing import Annotated

from database import urls_collection
from shorts.repository import LinkRepository, MongoLinkRepository
from shorts.service import LinkService

def get_database():
    return urls_collection

def get_link_repository(db: Annotated[object, Depends(get_database)]):
    return MongoLinkRepository(db=db)

def get_link_service(
    repository: Annotated[LinkRepository, Depends(get_link_repository)],
):
    return LinkService(repository=repository)