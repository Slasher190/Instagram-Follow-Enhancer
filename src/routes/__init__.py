from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
# from fastapi.encoders import jsonable_encoder
# from typing import List
from src.webDriver import Instagram
import json

router = APIRouter()

def get_webdriver():
    return Instagram()

@router.get("/", response_description="Instagram")
def test(request: Request, response: Response, webdriver: Instagram = Depends(get_webdriver)):
    try:
        webdriver.diver_initialization('https://www.instagram.com/')
        webdriver.login_instagram("iplug_bhopal", "iplugmp0987")
        webdriver.close_driver()
        response.status_code = status.HTTP_200_OK
        message = "Logged in successful!!!"
        return {"message": message, "success": True}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=json.dumps(e))

