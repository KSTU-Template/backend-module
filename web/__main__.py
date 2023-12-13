import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from web.config import APP_HOST
from web.routers import auth, product, information_channel, client

router = APIRouter(prefix="/api")
router.include_router(auth.router)
router.include_router(product.router)
router.include_router(information_channel.router)
router.include_router(client.router)


@router.get('/')
def main():
    return {'message': 'Good day, sir.'}


app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host=APP_HOST)
