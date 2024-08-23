from fastapi import FastAPI, APIRouter, Request, Response


router = APIRouter()

@router.get("/")
async def some_route(response: Response):
    response.headers["Cache-Control"] = "public, max-age=10"
    return {"answer": 42}


def get_app():
    app = FastAPI()
    app.include_router(router)
    return app