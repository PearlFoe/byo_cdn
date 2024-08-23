from fastapi import FastAPI, APIRouter


router = APIRouter()

@router.get("/")
async def some_route():
    return {"answer": 42}


def get_app():
    app = FastAPI()
    app.include_router(router)
    return app