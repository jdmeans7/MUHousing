import models as db


class query(object):
    def getStudent(self, bannerNumber):
        s = db.Student.query(db.Student.bannerNumber == bannerNumber)
        return s

