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