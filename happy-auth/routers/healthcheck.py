from fastapi import APIRouter

class Healthcheck:

    router = APIRouter()

    @router.get("/")
    def healthcheck():
        return {"status": "200 OK"}
