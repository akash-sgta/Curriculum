create database giraffe;

connect giraffe;

create table student(
	s_id int primary key not null auto_increment,
	name varchar(32) not null,
	major varchar(16)
);

describe student;

-- drop table student;

alter table student add gpa decimal(3,2);

-- alter table student drop column gpa;

insert into student (s_id, name, major)
values
(1, 'Jack', 'Biology');

insert into student (name, major)
values
('Kate','Sociology');

insert into student (name, major)
values
('Jake', 'Biology'),
('Akash', 'Computer');

update student
set major = "Bio"
where major like "Bio%" or major like "bio%";

update student
set name = "Default", major = null
where s_id = 3;

update student
set gpa = 0.00;

delete from student
where s_id = 3;

select *
from student;

select name
from student
where major like "%i%";

select name, major
from student
order by major asc, name desc;

select *
from student
limit 2;

truncate table student;

insert into student (name, major) values ('KEVIN','Law'),('DANIEL','Computer_Science'),('DANIEL','Construction'),('BRIAN','Computer_Science'),('MICHAEL','Biology'),('DONALD','Biology'),('JASON','Law'),('MATTHEW','Economics'),('JOSE','Politics'),('WILLIAM','Construction');

update student
set major = "CS"
where major like "Compu%";

update student
set major = "Const"
where major like "Const%";

update student
set major = "Bio"
where major like "Bio%";

update student
set gpa = 0.00;

drop table student;
-- ------------------------------
create database giraffe;

CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);

CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

CREATE TABLE works_with (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);

CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);


-- -----------------------------------------------------------------------------

-- Corporate
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);

-- Scranton
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);

INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');

UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);
-- -------------------------------------------------
create table trigger_test(
	message varchar(128)
);

alter table trigger_test
add log_id int primary key auto_increment;

DELIMITER $$
CREATE
	TRIGGER insert_trigger_2 BEFORE INSERT
	ON employee
	FOR EACH ROW BEGIN
		insert into trigger_test(message) values('added new employee '+New.first_name);
	END$$
DELIMITER;

insert into employee values(110, 'Mucho', 'Gusto', '1961-05-11', 'F', 1000, NULL, NULL);
select * from trigger_test;

DELIMITER $$
CREATE
	TRIGGER delete_trigger_2 AFTER DELETE
	ON employee
	FOR EACH ROW BEGIN
		insert into trigger_test(message) values('deleted an employee ');
	END$$
DELIMITER;

delete
from employee
where emp_id=110;

DROP TRIGGER insert_trigger;
DROP TRIGGER insert_trigger_2;
DROP TRIGGER delete_trigger;

-- -------------------------------------------------