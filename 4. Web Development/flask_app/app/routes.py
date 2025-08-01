from flask import render_template, request, redirect, url_for, session, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from app.models import User, Task

routes = Blueprint('routes', __name__)

@routes.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        user_email = request.form["email"].strip()
        user_password = request.form["password"].strip()
        try:
            user = User.query.filter_by(email=user_email).first()
            if user and check_password_hash(user.password, user_password):
                session["user_id"] = user.id
                session["name"] = user.name
                session["email"] = user.email
                return redirect(url_for("routes.home"))
            else:
                message = "User Not Exists."
        except Exception as e:
            print(f"Error : {e}")
            message = "Invalid credentials."
    
    return render_template("login.html", message=message)

@routes.route("/register", methods=["GET", "POST"])
def register():
    message = None
    try:
        if request.method == "POST":
            user_name = request.form["name"].strip()
            user_email = request.form["email"].strip()
            user_password = request.form["password"].strip()
            user = User.query.filter_by(email=user_email).first()
            if not user:
                hashed_password = generate_password_hash(user_password, method='pbkdf2:sha256', salt_length=16)
                new_user = User(name=user_name, email=user_email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("routes.success"))
            else:
                message = "Email already Exists."
    except Exception as e:
        print(f"Error : {e}")
        db.session.rollback()
    return render_template("register.html", message=message)

@routes.route("/home", methods=["GET"])
def home():
    user_name = session.get("name")
    user_id = session.get("user_id")
    tasks = None
    try:
        tasks = Task.query.filter_by(user_id=user_id).all()
    except Exception as e:
        print(f"Error : {e}")
    return render_template("home.html", user_name=user_name, tasks=tasks)

@routes.route("/success", methods=["GET"])
def success():
    return render_template("success.html")

@routes.route('/logout', methods=['POST'])
def logout():
    session.clear()
    print("Session Cleared.")
    return redirect(url_for('routes.login'))
    
@routes.route('/add_task', methods=["POST"])
def add_task():
    task_title = request.form["title"]
    task_description = request.form["description"]
    user_id = session.get("user_id")

    if user_id and task_title and task_description:
        try:
            new_task = Task(user_id=user_id, task_title=task_title, task_description=task_description)
            db.session.add(new_task)
            db.session.commit()
            print("Task Added")
        except Exception as e:
            print(f"Error : {e}")
            db.session.rollback()
    return redirect(url_for('routes.home'))

@routes.route('/delete_task/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        print("Task Deleted.")
    except Exception as e:
        db.session.rollback()
        print(f"Error : {e}")
    return redirect(url_for('routes.home'))

@routes.route('/edit_task/<int:task_id>', methods=["GET", "POST"])
def edit_task(task_id):
    try:
        task = Task.query.get_or_404(task_id)
    except Exception as e:
        print(f"Error : {e}")
    if request.method == "POST":
        task_title = request.form["title"]
        task_description = request.form["description"]
        task.task_title = task_title
        task.task_description = task_description
        db.session.commit()
        print("Task Updated.")
        return redirect(url_for('routes.home'))
    return render_template("edit_task.html", task=task)