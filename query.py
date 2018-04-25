import pymysql.cursors

connection = pymysql.connect(host='sql9.freesqldatabase.com',
                             user='sql9233446',
                             password='crjxGGauSm',
                             db='sql9233446',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='',
#                             db='test',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)

class query(object):
    def test(self, email):
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `FirstName`, `LastName` FROM `Advisor` WHERE `email`=%s"
                cursor.execute(sql, email)
                result = cursor.fetchone()
        finally:
            connection.close()
        return result

    def getStudent(self, bannerNumber):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `Student` WHERE `BannerNumber`=%s"
                cursor.execute(sql, bannerNumber)
                result = cursor.fetchone()
        finally:
            connection.close()
        return result

    # Query 1
    def getManagers(self, hallName):
        try:
            if connection.open == False:
                connection.begin()
            with connection.cursor() as cursor:
                sql = "SELECT `FirstName`, `LastName`, Staff.`Phone` " \
                      "FROM `Staff` " \
                      "INNER JOIN `Position` ON `Staff`.`Position` = `Position`.`PositionID` " \
                      "INNER JOIN `Hall` ON `HallName` = %s " \
                      "WHERE `PositionName` = 'Manager'"
                cursor.execute(sql, hallName)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result


    # Query 2
    def getStudentsLeases(self):
        try:
            if connection.open == False:
                connection.begin()
            with connection.cursor() as cursor:
                sql = "SELECT `FirstName`, `LastName`, Student.`BannerNumber`, " \
                      "`NumOfSemester`, `MoveInDate`, `MoveOutDate` " \
                      "FROM `Student` INNER JOIN Lease ON Student.bannerNumber = Lease.BannerNumber"
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 3
    def getLeases(self, semester):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `NumOfSemester`, `MoveOutDate`, `MoveInDate` FROM `Invoice` " \
                      "INNER JOIN Lease L ON Invoice.LeaseNo = L.LeaseNO " \
                      "WHERE Invoice.Semester=%s"
                cursor.execute(sql, semester)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 4
    def getTotalRent(self, bannerNumber):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT SUM(PayDue) FROM Invoice " \
                      "INNER JOIN Lease L on Invoice.LeaseNo = L.LeaseNO " \
                      "INNER JOIN Student S on L.BannerNumber = S.bannerNumber WHERE S.bannerNumber = %s"
                cursor.execute(sql, bannerNumber)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 5
    def getStudentsNotPaid(self, date):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT Student.BannerNumber, Student.FirstName, Student.LastName FROM Student " \
                      "INNER JOIN Lease L on Student.bannerNumber = L.BannerNumber " \
                      "INNER JOIN Invoice I on L.LeaseNO = I.LeaseNo WHERE I.Date < %s AND Paid = 0"
                cursor.execute(sql, date)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 6
    def inspcDetails(self, satisfcCondition):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `InspcNO`, `DateOfInspc`, `SatisfcCondition`, `Comments`, `StaffNO`, `FlatNO` " \
                      "FROM `Inspection` " \
                      "WHERE `SatisfcCondition` = %s"
                cursor.execute(sql, satisfcCondition)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 7
    def roomAndPlaceNO(self, HallName):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT `FirstName`, `LastName`, Student.`BannerNumber`, R.PlaceNO, R.RoomNO " \
                      "FROM `Student` INNER JOIN Lease L on Student.bannerNumber = L.BannerNumber " \
                      "INNER JOIN Room R on L.PlaceNO = R.PlaceNO " \
                      "INNER JOIN Hall H on R.HallNO = H.HallNO WHERE HallName = %s"
                cursor.execute(sql, HallName)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 8
    def getWaitingStudents(self):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Student WHERE Student.Status = 0"
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 9
    def getCountStudentsInCategory(self, category):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT COUNT(*) FROM Student " \
                      "INNER JOIN StudentLevel S on Student.LevelID = S.LevelID " \
                      "WHERE LevelName = %s"
                cursor.execute(sql, category)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

    # Query 10
    def getStudentsWithNoNOK(self):
        try:
            with connection.cursor() as cursor:
                sql = "SELECT COUNT(Student.bannerNumber) FROM Student " \
                      "WHERE Student.bannerNumber NOT IN " \
                      "(SELECT Student.bannerNumber FROM Student INNER JOIN NOK N on Student.bannerNumber = N.BannerNumber)"
                cursor.execute(sql)
                result = cursor.fetchall()
        except Exception:
            print(Exception)
        return result

