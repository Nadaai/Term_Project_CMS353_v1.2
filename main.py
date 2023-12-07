from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_ckeditor import CKEditor


app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ourdatabase.db'

db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120),nullable=False)

# to put the tables in db file
# with app.app_context():
#     db.create_all()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
 
with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


with app.app_context():
    user = User(id=1,name='Hassaan', email='hahajaj')
    db.session.add(user)
    db.session.commit()

static = {"firstName": "name",
            "lastName": "lastname",
            "userName": "userName",
            "email": "email@at.com",
            "password": "password",
            "type": "type"
            }

@app.route('/')
def home():
    return render_template("instructor_page.html")

@app.route('/home_student')
def home_student():
    return render_template("student_page.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        result = {"firstName": request.form['firstName'],
                  "lastName": request.form['lastName'],
                  "userName": request.form['userName'],
                  "email": request.form["email"],
                  "password": request.form["password"],
                  "type": request.form['type']}
        print(result)

        return redirect(url_for('home'))

    return render_template('addForm.html')

@app.route('/signin', methods=['POST', 'GET'])
def signin():

    if request.method == "POST":

        result1 = {"email": request.form["email"],
                  "password": request.form['password']}

        if result1["email"] == static["email"] and result1["password"] == static["password"]:
            return redirect(url_for('home_student'))
        else:
            return render_template('signin.html')

    return render_template('signin.html')


@app.route('/group')
def group():
    return redirect(url_for('home'))


# if __name__ == '__main__':
#     app.run(debug=True)
