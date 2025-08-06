from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_blogs(request: Request, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db)
    return templates.TemplateResponse("index.html", {"request": request, "blogs": blogs})


@app.get("/create")
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})


@app.post("/create")
def create_post(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    crud.create_blog(db, title, content)
    return RedirectResponse("/", status_code=303)


@app.get("/edit/{blog_id}")
def edit_form(blog_id: int, request: Request, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, blog_id)
    return templates.TemplateResponse("edit.html", {"request": request, "blog": blog})


@app.post("/edit/{blog_id}")
def update_post(blog_id: int, title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    crud.update_blog(db, blog_id, title, content)
    return RedirectResponse("/", status_code=303)


@app.get("/delete/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    crud.delete_blog(db, blog_id)
    return RedirectResponse("/", status_code=303)
