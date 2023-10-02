use employees;

-- 1
SHOW TABLES;
-- two 'table' that we get through SHOW TABLES commnad are not listed under Tables tab
-- namely, the 'current_dept_emp' and the 'dept_emp_latest_date'
-- they are not tables but rather 'views' that created and stored within the database

-- 2
SELECT first_name, last_name, gender
FROM `employees`
Limit 9999999;

-- 3
SELECT DISTINCT title 
FROM `titles`
Limit 9999999;

-- 4
SELECT COUNT(*) as "emp_amt"
FROM `employees`;
    
-- 5
SELECT COUNT(*) as "salary_amt"
FROM `salaries`;

-- 6
SELECT COUNT(*) as "depart_amt"
FROM `departments`;

-- 7
SELECT dept_name
FROM `departments`;

-- 8
SELECT first_name, last_name
FROM `employees`
WHERE gender = "F";
    
-- 9
SELECT COUNT(gender)
FROM `employees`
WHERE gender = "M";

-- 10
SELECT *
FROM `employees`
WHERE hire_date < "19900101";

-- 11
SELECT *
FROM `employees`
WHERE ( hire_date >= "19960101" ) 
	AND ( gender = "M" );
-- "after 1995" means after 1996, not after 19950101

-- 12
SELECT COUNT(*)
FROM `employees`
WHERE first_name IN ("Adin", "Deniz", "Youssef", "Roded");

-- 13
	-- a
SELECT COUNT(*) AS amt
FROM `titles` as t
WHERE title LIKE '%engineer%'
LIMIT 999999;
-- return a value when title inclue "engineer"
-- return 227881
SELECT COUNT(distinct t.emp_no) AS amt
FROM `titles` AS t
WHERE t.to_date = "9999-01-01"
LIMIT 999999;
-- return a value when title equal to "engineer" exactly
-- 45136 94870 258978 290852
	-- b
SELECT COUNT(*) AS amt
FROM `titles` as t
WHERE title NOT LIKE "%engineer%";
-- return 215427
SELECT COUNT(t.emp_no) AS amt
FROM `titles` AS t
		JOIN `dept_emp_latest_date` AS deld ON t.emp_no = deld.emp_no
WHERE t.title NOT LIKE '%engineer%' AND t.to_date = deld.to_date
LIMIT 999999;

-- 14
SELECT COUNT(*) as amt
FROM `employees`
WHERE ( hire_date >= "19900101" )
	AND ( hire_date <= "19940101" );
-- return 86393
	
    
-- 15
SELECT DISTINCT last_name
FROM `employees`
WHERE ( birth_date < "19700101" )
	AND ( hire_date >= "19970101" ) and ( gender = "F" )
ORDER BY last_name;
-- hired afted 1996 means 19970101

-- 16
SELECT gender, 
	COUNT(gender) as amt
FROM `employees`
WHERE hire_date < "19890101"
GROUP BY gender;

-- 17
SELECT e.gender, 
	d.dept_name, 
	COUNT(d.dept_name) AS amt
FROM `employees` AS e 
    JOIN `dept_emp` AS de USING (emp_no)
    JOIN `departments` AS d USING (dept_no)
GROUP BY e.gender, d.dept_name;
-- cannot coun(*) here

SELECT e.gender, 
	COUNT(e.gender) AS amt
FROM `employees` AS e 
WHERE
	( e.hire_date BETWEEN "19940101" AND "19961231" )
GROUP BY e.gender;
-- between is inclusive on both side

-- 18
SELECT first_name,
	last_name
FROM `employees` AS e 
	JOIN `dept_emp` AS de USING (emp_no)
WHERE
	de.dept_no = 
		( 
        SELECT dept_no
			FROM `dept_emp` as de
			WHERE emp_no = 
            ( 
            SELECT emp_no
				FROM `employees` AS e
					JOIN `titles` AS t USING (emp_no)
				WHERE ( t.title = "Manager" ) 
					AND ( t.from_date >= "19920908" ) 
                    AND ( t.to_date <= "19960103" )
			)
		);
-- returns 23580

-- 19
SELECT
	e.first_name,
    e.last_name,
    t.title
FROM
	`employees` AS e
    JOIN `titles` AS t USING(emp_no)
LIMIT 9999999;
-- returns 4433308

SELECT e.first_name, e.last_name, tt.title
FROM `employees` AS e
    JOIN
    (	SELECT t_2.emp_no, t_2.title
		FROM `titles` AS t_1
			JOIN `titles` AS t_2 ON (t_1.to_date = t_2.to_date)
		WHERE (t_2.to_date > t_1.to_date OR t_2.to_date = "99990101") 
			AND t_2.emp_no = t_1.emp_no	) AS tt ON (e.emp_no = tt.emp_no)
LIMIT 9999999;
-- 240124

-- 20
-- employee who have changed their department all changed 1 time
SELECT dept_no, 
	AVG(s.salary) as avg_sal
FROM `dept_emp` AS de
	JOIN `salaries` AS s ON de.emp_no = s.emp_no
GROUP BY de.dept_no;

-- 21
SELECT a.dept_no, a.n_emp as empAmt, b.avg_sal
FROM 
( SELECT
		de.dept_no,
		COUNT(emp_no) as n_emp	
	FROM `dept_emp` as de
	GROUP BY de.dept_no) AS a
	JOIN
	( SELECT dept_no,
			AVG(s.salary) as avg_sal
		FROM `dept_emp` AS de
			JOIN `salaries` AS s ON de.emp_no = s.emp_no
		GROUP BY de.dept_no) AS b ON a.dept_no = b.dept_no;

-- 22
SELECT m.dept_no, 
	sum(count_e) as empAmt
FROM
( SELECT COUNT(DISTINCT s.emp_no) as count_e, de.dept_no
	FROM `salaries` AS s 
		JOIN `dept_emp` AS de USING(emp_no)
	WHERE s.salary > 130000
	GROUP BY de.to_date = "99990101", de.dept_no ) as m
GROUP BY m.dept_no
ORDER BY m.dept_no;







		
    


