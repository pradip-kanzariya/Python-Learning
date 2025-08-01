from datetime import datetime, timezone
from app import db

class User(db.Model):
    __tablename__ = 'user_register'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    tasks = db.relationship(
        'Task',
        backref='user',
        cascade='all, delete',
        passive_deletes=True
    )

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_register.id', ondelete="CASCADE"), nullable=False)
    task_title = db.Column(db.String(200), nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    task_created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    task_updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
