from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    email: str = Field(index=True)
    password: str
    

class Post(SQLModel, table=True):
    id: int | None = Field(primary_key=True)

    date: datetime.datetime = Field(index=True)

    owner_id: int = Field(foreign_key="user.id")

class Booking(SQLModel, table=True):
    id: int | None = Field(primary_key=True)

    guests: int

    user_id: int = Field(foreign_key="user.id")
    post_id: int = Field(foreign_key="post.id")

# create sql instance
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request, name="login.html"
    )

@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/create", response_class=HTMLResponse)
async def create(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )