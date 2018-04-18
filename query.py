import models as db
from peewee import *

class query(object):
    def getStudent(self, bannerNumber):
        s = db.Student.select(db.Student.FirstName).where(db.Student.bannerNumber == bannerNumber)
        return s

