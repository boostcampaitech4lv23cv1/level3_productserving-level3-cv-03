from fastapi import FastAPI, APIRouter
from routers import OD, SS

import uvicorn

app = FastAPI()

if __name__ == '__main__':
    app.include_router(OD.router)
    app.include_router(SS.router)
    uvicorn.run(app, host='0.0.0.0', port=30011)