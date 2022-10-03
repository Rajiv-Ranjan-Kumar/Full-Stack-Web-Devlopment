-- Select all the students who are doing a specific course, eg. Python.

SELECT * FROM Student WHERE cid = (SELECT cid FROM Courses WHERE cname = 'Python');
