from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Student(db.Model):
    bannerNumber = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(25), nullable=False)
    LastName = db.Column(db.String(25), nullable=False)
    Street = db.Column(db.String(50), nullable=False)
    City = db.Column(db.String(25), nullable=False)
    Zip = db.Column(db.String(10), nullable=False)
    Phone = db.Column(db.String(16), nullable=True)
    Email = db.Column(db.String(25), nullable=False, unique=True)
    DateOfBirth = db.Column(db.Date, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Nationality = db.Column(db.String(50), nullable=False)
    SpecialNeeds = db.Column(db.String(200), nullable=False)
    Comments = db.Column(db.String(200), nullable=False)
    Status = db.Column(db.Boolean)
    #LevelID
    #ParkingLotID
    #MajorID


