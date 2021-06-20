from fastapi import APIRouter, Request
from services.line.login import LineLogin
from services.google.login import GoogleLogin
from services.facebook.login import FacebookLogin
from pydantic import BaseModel

class Login:

    router = APIRouter()

    class Contact(BaseModel):
        client_id:int
        redirect_uri:str
        scope:str

    @router.post("/line")
    def login_line(request: Contact):
        line_login_service = LineLogin()
        # print(request.json())
        # print(request.body())
        line_login_service.login(request)
        print("tywcveyfuvu")
        return  {"status": "200 OK", "data": request}

    @router.post("/google")
    def login_google():
        google_login_service = GoogleLogin()
        google_login_service.login()
        return {"status": "200 OK"}

    @router.post("/facebook")
    def login_facebook():
        facebook_login_service = FacebookLogin()
        facebook_login_service.login()
        return {"status": "200 OK"}
