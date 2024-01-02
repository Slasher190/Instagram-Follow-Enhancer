from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
# from fastapi.encoders import jsonable_encoder
# from typing import List
from src.Selenium.DriverInit import DriverInitialization
import json

router = APIRouter()

def get_webdriver():
    return DriverInitialization()

@router.get("/", response_description="Instapage")
def test(request: Request, response: Response, webdriver: DriverInitialization = Depends(get_webdriver)):
    try:
        webdriver.diver_initialization('https://www.instagram.com/')
        webdriver.close_driver()
        response.status_code = status.HTTP_200_OK
        message = "Driver works fine!!!"
        return {"message": message, "success": True}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=json.dumps(e))