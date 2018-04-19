import pymysql.cursors

connection = pymysql.connect(host='sql9.freesqldatabase.com',
                             user='sql9233446',
                             password='crjxGGauSm',
                             db='sql9233446',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

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

