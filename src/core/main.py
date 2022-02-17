from fastapi import FastAPI
import uvicorn

from .api import routers
from .api.models import Base
from .database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(routers.router, prefix="/books", tags=["books"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)