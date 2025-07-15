from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()
    

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        db.session.add(Task(title=request.form["title"]))
        db.session.commit()
        return redirect(url_for("index"))
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.post("/complete/<int:task_id>")
def complete(task_id):
    t = Task.query.get_or_404(task_id)
    t.done = True
    db.session.commit()
    return redirect(url_for("index"))

@app.post("/delete/<int:task_id>")
def delete(task_id):
    db.session.delete(Task.query.get_or_404(task_id))
    db.session.commit()
    return redirect(url_for("index"))
    
    
if __name__ == "__main__":
    app.run(debug=True)
    