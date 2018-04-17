CREATE TABLE `Student` (
	`bannerNumber` INT(4) NOT NULL AUTO_INCREMENT,
	`FirstName` varchar(25) NOT NULL,
	`LastName` varchar(25) NOT NULL,
	`Street` varchar(50) NOT NULL,
	`City` varchar(25) NOT NULL,
	`Zip` varchar(10) NOT NULL,
	`Phone` varchar(16),
	`Email` varchar(50) NOT NULL UNIQUE,
	`DateOfBirth` DATE NOT NULL,
	`Gender` varchar(10),
	`Nationality` varchar(50) NOT NULL,
	`SpecialNeeds` varchar(200),
	`Comments` varchar(200),
	`Status` bool NOT NULL,
	`LevelID` INT,
	`ParkingLotID` INT,
	`MajorID` INT NOT NULL,
	PRIMARY KEY (`bannerNumber`)
);

CREATE TABLE `StudentLevel` (
	`LevelID` INT NOT NULL AUTO_INCREMENT,
	`LevelName` varchar(50) NOT NULL,
	PRIMARY KEY (`LevelID`)
);

CREATE TABLE `ParkingLot` (
	`ParkingLotID` INT NOT NULL AUTO_INCREMENT,
	`Street` varchar(50) NOT NULL,
	`City` varchar(50) NOT NULL,
	`Zip` varchar(16) NOT NULL,
	PRIMARY KEY (`ParkingLotID`)
);

CREATE TABLE `Major` (
	`MajorID` INT NOT NULL AUTO_INCREMENT,
	`MajorName` varchar(50) NOT NULL,
	PRIMARY KEY (`MajorID`)
);

CREATE TABLE `NOK` (
	`NOKID` INT NOT NULL AUTO_INCREMENT,
	`FirstName` varchar(25) NOT NULL,
	`LastName` varchar(25) NOT NULL,
	`Street` varchar(50) NOT NULL,
	`City` varchar(25) NOT NULL,
	`Zip` varchar(10) NOT NULL,
	`Phone` varchar(16),
	`Relationship` varchar(16) NOT NULL,
	`BannerNumber` INT(4) NOT NULL,
	PRIMARY KEY (`NOKID`)
);

CREATE TABLE `StuAttendCourse` (
	`BannerNumber` INT NOT NULL,
	`CourseNO` INT NOT NULL,
	`Semester` varchar(16) NOT NULL,
	`Year` varchar(4) NOT NULL,
	`Instructor` varchar(50) NOT NULL,
	`Phone` varchar(16),
	`Email` varchar(50) UNIQUE,
	`RoomNumber` varchar(16) NOT NULL,
	`DeptNo` INT(4) NOT NULL
);

CREATE TABLE `Course` (
	`CourseNO` INT NOT NULL AUTO_INCREMENT,
	`CourseName` varchar(50) NOT NULL,
	PRIMARY KEY (`CourseNO`)
);

CREATE TABLE `Department` (
	`DeptNO` INT NOT NULL AUTO_INCREMENT,
	`DeptName` varchar(50) NOT NULL,
	PRIMARY KEY (`DeptNO`)
);

CREATE TABLE `Lease` (
	`LeaseNO` INT NOT NULL AUTO_INCREMENT,
	`NumOfSemester` varchar(2) NOT NULL,
	`MoveInDate` DATE NOT NULL,
	`MoveOutDate` DATE NOT NULL,
	`PlaceNO` INT NOT NULL,
	`BannerNumber` INT NOT NULL,
	PRIMARY KEY (`LeaseNO`)
);

CREATE TABLE `Room` (
	`PlaceNO` INT NOT NULL AUTO_INCREMENT,
	`RoomNO` INT NOT NULL,
	`RentRate` varchar(16) NOT NULL,
	`FlatNO` INT,
	`HallNO` INT,
	PRIMARY KEY (`PlaceNO`)
);

CREATE TABLE `Invoice` (
	`InvoiceNO` INT NOT NULL AUTO_INCREMENT,
	`Semester` varchar(16) NOT NULL,
	`PayDue` double NOT NULL,
	`Date` DATE NOT NULL,
	`PayMethod` varchar(16) NOT NULL,
	`DateOfFirstRem` DATE NOT NULL,
	`DateOfSecondRem` DATE NOT NULL,
	`LeaseNo` INT NOT NULL,
	PRIMARY KEY (`InvoiceNO`)
);

CREATE TABLE `Flat` (
	`FlatNO` INT NOT NULL AUTO_INCREMENT,
	`Street` varchar(50) NOT NULL,
	`City` varchar(50) NOT NULL,
	`Zip` varchar(10) NOT NULL,
	`NumOfRooms` INT NOT NULL,
	PRIMARY KEY (`FlatNO`)
);

CREATE TABLE `Hall` (
	`HallNO` INT NOT NULL AUTO_INCREMENT,
	`Street` varchar(50) NOT NULL,
	`City` varchar(50) NOT NULL,
	`Zip` varchar(10) NOT NULL,
	`HallName` varchar(50) NOT NULL,
	`Phone` varchar(16) NOT NULL,
	`StaffNO` INT(16) NOT NULL,
	PRIMARY KEY (`HallNO`)
);

CREATE TABLE `Inspection` (
	`InspcNO` INT NOT NULL AUTO_INCREMENT,
	`DateOfInspc` DATE NOT NULL,
	`SatisfcCondition` varchar(16),
	`Comments` varchar(200),
	`FlatNO` INT NOT NULL,
	`StaffNO` INT NOT NULL,
	PRIMARY KEY (`InspcNO`)
);

CREATE TABLE `Staff` (
	`staffNO` INT(4) NOT NULL AUTO_INCREMENT,
	`FirstName` varchar(25) NOT NULL,
	`LastName` varchar(25) NOT NULL,
	`Email` varchar(50) NOT NULL UNIQUE,
	`Street` varchar(50) NOT NULL,
	`City` varchar(25) NOT NULL,
	`Zip` varchar(10) NOT NULL,
	`DateOfBirth` DATE NOT NULL,
	`Gender` varchar(10),
	`Location` varchar(50) NOT NULL,
	`Position` varchar(50) NOT NULL,
	PRIMARY KEY (`staffNO`)
);

CREATE TABLE `Advisor` (
	`AdvisorID` INT NOT NULL AUTO_INCREMENT,
	`FirstName` varchar(25) NOT NULL,
	`LastName` varchar(25) NOT NULL,
	`Phone` varchar(25),
	`Email` varchar(25) NOT NULL UNIQUE,
	`RoomNumber` varchar(25) NOT NULL,
	`DeptNO` INT NOT NULL,
	`PositionID` INT NOT NULL,
	PRIMARY KEY (`AdvisorID`)
);

CREATE TABLE `Position` (
	`PositionID` INT NOT NULL AUTO_INCREMENT,
	`PositionName` varchar(50) NOT NULL,
	PRIMARY KEY (`PositionID`)
);

ALTER TABLE `Student` ADD CONSTRAINT `Student_fk0` FOREIGN KEY (`LevelID`) REFERENCES `StudentLevel`(`LevelID`);

ALTER TABLE `Student` ADD CONSTRAINT `Student_fk1` FOREIGN KEY (`ParkingLotID`) REFERENCES `ParkingLot`(`ParkingLotID`);

ALTER TABLE `Student` ADD CONSTRAINT `Student_fk2` FOREIGN KEY (`MajorID`) REFERENCES `Major`(`MajorID`);

ALTER TABLE `NOK` ADD CONSTRAINT `NOK_fk0` FOREIGN KEY (`BannerNumber`) REFERENCES `Student`(`bannerNumber`);

ALTER TABLE `StuAttendCourse` ADD CONSTRAINT `StuAttendCourse_fk0` FOREIGN KEY (`BannerNumber`) REFERENCES `Student`(`bannerNumber`);

ALTER TABLE `StuAttendCourse` ADD CONSTRAINT `StuAttendCourse_fk1` FOREIGN KEY (`CourseNO`) REFERENCES `Course`(`CourseNO`);

ALTER TABLE `StuAttendCourse` ADD CONSTRAINT `StuAttendCourse_fk2` FOREIGN KEY (`DeptNo`) REFERENCES `Department`(`DeptNO`);

ALTER TABLE `Lease` ADD CONSTRAINT `Lease_fk0` FOREIGN KEY (`PlaceNO`) REFERENCES `Room`(`PlaceNO`);

ALTER TABLE `Lease` ADD CONSTRAINT `Lease_fk1` FOREIGN KEY (`BannerNumber`) REFERENCES `Student`(`bannerNumber`);

ALTER TABLE `Room` ADD CONSTRAINT `Room_fk0` FOREIGN KEY (`FlatNO`) REFERENCES `Flat`(`FlatNO`);

ALTER TABLE `Room` ADD CONSTRAINT `Room_fk1` FOREIGN KEY (`HallNO`) REFERENCES `Hall`(`HallNO`);

ALTER TABLE `Invoice` ADD CONSTRAINT `Invoice_fk0` FOREIGN KEY (`LeaseNo`) REFERENCES `Lease`(`LeaseNO`);

ALTER TABLE `Hall` ADD CONSTRAINT `Hall_fk0` FOREIGN KEY (`StaffNO`) REFERENCES `Staff`(`staffNO`);

ALTER TABLE `Inspection` ADD CONSTRAINT `Inspection_fk0` FOREIGN KEY (`FlatNO`) REFERENCES `Flat`(`FlatNO`);

ALTER TABLE `Inspection` ADD CONSTRAINT `Inspection_fk1` FOREIGN KEY (`StaffNO`) REFERENCES `Staff`(`staffNO`);

ALTER TABLE `Advisor` ADD CONSTRAINT `Advisor_fk0` FOREIGN KEY (`DeptNO`) REFERENCES `Department`(`DeptNO`);

ALTER TABLE `Advisor` ADD CONSTRAINT `Advisor_fk1` FOREIGN KEY (`PositionID`) REFERENCES `Position`(`PositionID`);

