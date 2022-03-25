CREATE TABLE name_table(
    StudentID VARCHAR(4) ,
    Name CHAR(30)
);


INSERT INTO name_table (StudentID, Name)
VALUES 
('V001','Abe'),
('V002','Abhay'),
('V003','Acelin'),
('V004','Adelphos');


CREATE TABLE mark_table(
    StudentID VARCHAR(5),
    Total_marks IntEGER
);

INSERT INTO mark_table (StudentID, Total_marks)
VALUES 
('V001',95),
('V002',80),
('V003',74),
('V004',81);




SELECT a.StudentID, Name, Total_marks
FROM mark_table a, name_table b
WHERE a.StudentID = b.StudentID
AND Total_marks >80;

SELECT *  
FROM `mark_table`  
WHERE studentid = 'V002';
