import uvicorn
from fastapi import FastAPI, Depends, HTTPException

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.routes import auth, check, check_view
from src.conf.config import config

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api")
app.include_router(check.router, prefix="/api")
app.include_router(check_view.router)

templates = Jinja2Templates(directory="src/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.mount("/css", StaticFiles(directory="src/static/css"), name="static")



@app.get("/")
def index():
    return {"message": "Checkbox TT"}


@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    """
    The healthchecker function is used to check the health of the database.
    It does this by making a simple query to the database and checking if it returns any results.
    If no results are returned, then we know that there is an issue with our connection.

    :param db: AsyncSession: Inject the database session into the function
    :return: A dictionary with a message
    :doc-author: Boldysheva Aleksandra
    """
    try:
        # Make request
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "App is healthy"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=config.HOST, port=config.PORT, reload=True
    )
