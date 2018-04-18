from peewee import *


db = MySQLDatabase("db7fce33ca0ef54c15a0a7a8c5002d2c0b", host="7fce33ca-0ef5-4c15-a0a7-a8c5002d2c0b.mysql.sequelizer.com", port=3306, user="wwfrditfmmpgodzk", passwd="cuUx4AEBhgFsD85TrxzRX7AQLmiMhLCw2FnzNviyvSHbVAQDHY6kRmGe3eUQrZtD")


class MySQLModel(Model):
    class Meta:
        database = db

#Models
class Major(MySQLModel):
    MajorID = PrimaryKeyField()
    MajorName = CharField()

    class Meta:
        db_table = "major"


class StudentLevel(MySQLModel):
    LevelID = PrimaryKeyField()
    LevelName = CharField()

    class Meta:
        db_table = "level"


class ParkingLot(MySQLModel):
    ParkingLotID = PrimaryKeyField()
    Street = CharField()
    City = CharField()
    Zip = CharField()


class Department(MySQLModel):
    DeptNO = PrimaryKeyField()
    DeptName = CharField()

    class Meta:
        db_table = "department"


class Position(MySQLModel):
    PositionID = PrimaryKeyField()
    PositionName = CharField()


class Advisor(MySQLModel):
    AdvisorID = PrimaryKeyField()
    FirstName = CharField()
    LastName = CharField()
    Phone = CharField(null=True)
    Email = CharField(unique=True)
    RoomNumber = CharField()
    DeptNO = ForeignKeyField(Department, to_field="DebtNO")
    PositionID = ForeignKeyField(Position, to_field="PositionID")


class Student(MySQLModel):
    bannerNumber = PrimaryKeyField()
    FirstName = CharField()
    LastName = CharField()
    Street = CharField()
    City = CharField()
    Zip = CharField()
    Phone = CharField(null=True)
    Email = CharField(unique=True)
    DateOfBirth = DateField()
    Gender = CharField()
    Nationality = CharField()
    SpecialNeeds = CharField(null=True)
    Comments = CharField(null=True)
    Status = BooleanField()
    LevelID = ForeignKeyField(StudentLevel, to_field="LevelID")
    ParkingLotID = ForeignKeyField(ParkingLot, to_field="ParkingLotID")
    MajorID = ForeignKeyField(Major, to_field="MajorID")

    class Meta:
        db_table = "student"


class NOK(MySQLModel):
    NOKID = PrimaryKeyField()
    FirstName = CharField()
    LastName = CharField()
    Street = CharField()
    City = CharField()
    Zip = CharField()
    Phone = CharField(null=True)
    Relationship = CharField()
    bannerNumber = ForeignKeyField(Student, to_field='bannerNumber')

    class Meta:
        db_table = "NOK"


class Course(MySQLModel):
    CourseID = PrimaryKeyField()
    CourseName = CharField()

    class Meta:
        db_table = "course"


class StuAttendCourse(MySQLModel):
    BannerNumber = ForeignKeyField(Student, to_field="bannerNumber")
    CourseNO = ForeignKeyField(Course, to_field="CourseID")
    Semester = CharField()
    Year = CharField()
    Instructor = CharField()
    Phone = CharField()
    Email = CharField(unique=True)
    RoomNumber = CharField()
    DeptNo = ForeignKeyField(Department, to_field="DeptNO")

    class Meta:
        db_table = "stuattendcourse"


class Staff(MySQLModel):
    staffNO = PrimaryKeyField()
    FirstName = CharField()
    LastName = CharField()
    Email = CharField(unique=True)
    Street = CharField()
    City = CharField()
    Zip = CharField()
    DateOfBirth = CharField()
    Gender = CharField(null=True)
    Location = CharField()
    Position = CharField()

    class Meta:
        db_table = "staff"


class Flat(MySQLModel):
    FlatNO = PrimaryKeyField()
    Street = CharField()
    City = CharField()
    Zip = CharField()
    NumOfRooms = IntegerField()

    class Meta:
        db_table = "flat"


class Inspection(MySQLModel):
    InspcNO = PrimaryKeyField()
    DateOfInspc = DateField()
    SatisfcCondition = CharField(null=True)
    Comments = CharField(null=True)
    FlatNO = ForeignKeyField(Flat, to_field="FlatNO")
    StaffNO = ForeignKeyField(Staff, to_field="staffNO")

    class Meta:
        db_table = "inspection"


class Hall(MySQLModel):
    HallNO = PrimaryKeyField()
    Street = CharField()
    City = CharField()
    Zip = CharField()
    HallName = CharField()
    Phone = CharField()
    StaffNO = ForeignKeyField(Staff, to_field="StaffNO")

    class Meta:
        db_table = "hall"


class Room(MySQLModel):
    PlaceNO = PrimaryKeyField()
    RoomNO = IntegerField()
    RentRate = CharField()
    FlatNO = ForeignKeyField(Flat, to_field="FlatNO", null=True)
    HallNO = ForeignKeyField(Hall, to_field="HallNo", null=True)

    class Meta:
        db_table = "room"


class Lease(MySQLModel):
    LeaseNO = PrimaryKeyField()
    NumOfSemester = CharField()
    MoveInDate = DateField()
    MoveOutDate = DateField()
    PlaceNO = ForeignKeyField(Hall, to_field="PlaceNO")
    BannerNumber = ForeignKeyField(Student, to_field="bannerNumber")

    class Meta:
        db_table = "lease"


class Invoice(MySQLModel):
    InvoiceNO = PrimaryKeyField()
    Semester = CharField()
    PayDue = DoubleField()
    Date = DateField()
    PayMethod = CharField()
    DateOfFirstRem = DateField()
    DateOfSecondRem = DateField()
    LeaseNo = ForeignKeyField(Lease, to_field="LeaseNO")

