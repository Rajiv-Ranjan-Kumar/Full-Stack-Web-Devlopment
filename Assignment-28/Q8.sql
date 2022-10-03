--Create Courses table (cid, cname) where cid is a primary key and Student table
--(rollno, name, cid) where rollno is a primary key and cid is a foreign key.

CREATE TABLE Courses(
	cid int,
	cname varchar(10),
	PRIMARY KEY(cid)
);

CREATE TABLE Student(
	rollno int ,
	name varchar(20),
	cid int,
	PRIMARY KEY(rollno),
	CONSTRAINT fk_Courses FOREIGN KEY(cid) REFERENCES Courses(cid)
);
