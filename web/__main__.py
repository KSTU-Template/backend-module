import uvicorn
from fastapi import FastAPI, APIRouter

from web.routers import auth
from web.config import APP_HOST

router = APIRouter(prefix="/api")
router.include_router(auth.router)


@router.get('/')
def main():
    return {'message': 'Good day, sir.'}


app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host=APP_HOST)
