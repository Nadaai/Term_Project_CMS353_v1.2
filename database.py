from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TeamsDataBase.db'

db = SQLAlchemy()
db.init_app(app)

class Admin(db.Model):
    ad_id = db.Column(db.Integer, primary_key=True)
    ad_name = db.Column(db.String(50), nullable=False)
    ad_email = db.Column(db.String(), nullable=False)
    ad_password = db.Column(db.String(), nullable=False)

# with app.app_context():
#     db.create_all()

# nour = Admin(ad_id = 1, ad_name='nour', ad_email='Nour@gmail.com',ad_password='barakat3')
# with app.app_context():
#     db.session.add(nour)
#     db.session.commit()
class Instructor(db.Model):
    inst_id = db.Column(db.Integer, primary_key=True)
    inst_name = db.Column(db.String(50), nullable=False)
    inst_email = db.Column(db.String(), nullable=False)
    inst_password = db.Column(db.String(), nullable=False)

class Student(db.Model):
    std_id = db.Column(db.Integer, primary_key=True)
    std_name = db.Column(db.String(50), nullable=False)
    std_email = db.Column(db.String(), nullable=False)
    std_password = db.Column(db.String(), nullable=False)


class Group(db.Model):
    grp_id = db.Column(db.Integer, primary_key=True)
    grp_name = db.Column(db.String(50), nullable=False)

class Channel(db.Model):
    ch_id = db.Column(db.Integer, primary_key=True)
    ch_name = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()