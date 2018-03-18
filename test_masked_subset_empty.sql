--  Sample employee database 
--  See changelog table for details
--  Copyright (C) 2007,2008, MySQL AB
--  
--  Original data created by Fusheng Wang and Carlo Zaniolo
--  http://www.cs.aau.dk/TimeCenter/software.htm
--  http://www.cs.aau.dk/TimeCenter/Data/employeeTemporalDataSet.zip
-- 
--  Current schema by Giuseppe Maxia 
--  Data conversion from XML to relational by Patrick Crews
-- 
-- This work is licensed under the 
-- Creative Commons Attribution-Share Alike 3.0 Unported License. 
-- To view a copy of this license, visit 
-- http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to 
-- Creative Commons, 171 Second Street, Suite 300, San Francisco, 
-- California, 94105, USA.
-- 
--  DISCLAIMER
--  To the best of our knowledge, this data is fabricated, and
--  it does not correspond to real people. 
--  Any similarity to existing people is purely coincidental.
-- 

USE masked_subset;

SELECT 'TESTING masked_subset DATABASE IS EMPTY' as 'INFO';

DROP TABLE IF EXISTS expected_values, found_values;
CREATE TABLE expected_values (
    table_name varchar(30) not null primary key,
    recs int not null
) ENGINE=MyISAM;

-- In MySQL 5.0, the creation and update time for  memory tables is not recorded
/*!50130 ALTER TABLE expected_values engine=memory */;

CREATE TABLE found_values LIKE expected_values;

INSERT INTO `expected_values` VALUES 
('employees',    0),
('departments',  0),
('dept_manager', 0),
('dept_emp',     0),
('titles',       0),
('salaries',     0);
                      
SELECT table_name, recs AS expected_records FROM expected_values;

INSERT INTO found_values VALUES ('employees', (SELECT COUNT(*) FROM employees));

INSERT INTO found_values values ('departments', (SELECT COUNT(*) FROM departments));

INSERT INTO found_values values ('dept_manager', (SELECT COUNT(*) FROM dept_manager));

INSERT INTO found_values values ('dept_emp', (SELECT COUNT(*) FROM dept_emp));

INSERT INTO found_values values ('titles', (SELECT COUNT(*) FROM titles));

INSERT INTO found_values values ('salaries', (SELECT COUNT(*) FROM salaries));

SELECT table_name, recs as 'found_records   ' from found_values;

SELECT  
    e.table_name, 
    IF(e.recs=f.recs,'OK', 'not ok') AS records_match
from 
    expected_values e INNER JOIN found_values f USING (table_name); 

set @count_fail=(select count(*) from expected_values e inner join found_values f on (e.table_name=f.table_name) where f.recs != e.recs);

select timediff(
    now(),
    (select create_time from information_schema.tables where table_schema='employees' and table_name='expected_values')
) as computation_time;

DROP TABLE expected_values,found_values;

select 'count' as summary, if(@count_fail = 0, "OK", "FAIL" ) as result;
