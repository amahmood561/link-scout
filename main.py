from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.utils import fetch_metadata, take_screenshot

router = APIRouter()

class URLRequest(BaseModel):
    url: str

@router.post("/parse")
async def parse_url(request: URLRequest, screenshot: bool = Query(False)):
    data = fetch_metadata(request.url)

    if screenshot:
        shot_path = await take_screenshot(request.url)
        data["screenshot"] = shot_path

    return data
