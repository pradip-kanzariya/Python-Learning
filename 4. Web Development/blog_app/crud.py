from sqlalchemy.orm import Session
import models

def get_blogs(db: Session):
    return db.query(models.Blog).all()

def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()

def create_blog(db: Session, title: str, content: str):
    blog = models.Blog(title=title, content=content)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def update_blog(db: Session, blog_id: int, title: str, content: str):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    blog.title = title
    blog.content = content
    db.commit()
    return blog

def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    db.delete(blog)
    db.commit()
