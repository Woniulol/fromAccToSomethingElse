use `university`;

-- 1
select * 
from `student`
where LastName = 'Ben'
order by Gender, Age;

-- 2
select StudentID, LastName, FirstName
from `student`
where StudentID in 
(
	select StudentID from `enrollment` where Grade = "F"
);
    
-- 3
select StudentID, LastName, FirstName
from `student`
where StudentID in 
(
	select StudentID from `enrollment` where Grade in ("D", "F")
);

-- 4
-- assuming we dont know the instructor id 
select s.StudentID, s.Lastname, s.Firstname
from `student` as s
where s.StudentID in 
(
	select en.studentid from `enrollment` as en
    where en.sectionid in 
	(
		select se.sectionid from `section` as se
		where InstructorID in 
		(
			select i.InstructorID from `instructor` as i
			where (i.LastName = "John") and (i.FirstName = "Chua")
		)
	)
)
order by s.Lastname;

select st.studentid, st.lastname, st.firstname
from `section` as se join `instructor` as ins using (instructorid)
join `enrollment` as en using (sectionid)
join `student` as st using (studentid)
where ins.lastname = "John" and ins.firstname = "Chua"
order by st.lastname;

-- 5
select count(se.sectionid) as amt_section_john
from `section` as se
where 
( se.InstructorID in 
	(
		select i.InstructorID from `instructor` as i
		where (i.LastName = "John") 
			and (i.FirstName = "Chua")
	)
)
and ( se.Year = 2018 ) 
and ( se.Sem = 2 );

-- 6
select count(en.studentid)
from `enrollment` as en
where en.sectionid in
(
	select se.sectionid
	from `section` as se
	where 
	( se.InstructorID = 
		(
			select i.InstructorID from `instructor` as i
			where (i.LastName = "Kris") 
				and (i.FirstName = "Tan")
		)
	)
	and ( se.courseid = 8881 )
	and ( se.year = "2018" )
	and ( se.sem = 1 )
);

-- 7
select *
from `student` as s
where s.StudentID in
(
	select e.StudentID from `enrollment` as e
    where e.Year in ("2017", "2018")
	group by e.StudentID having count(e.CourseID) >= 3
);

-- 8 
select *
from `instructor` as i
where i.InstructorID in
(
	select se.InstructorID from `section` as se
	where ( se.Year = "2018" ) and ( se.Sem = 2 )
	group by se.InstructorID having count(se.SectionID) >= 3
);

-- 9
select *
from `student` as s
where s.StudentID in
(
	select e.StudentID 
    from `enrollment` as e
	where ( e.Year = "2018" ) 
		and ( e.Sem = 2 )
        and ( e.Grade = "A")
	group by e.StudentID  having count(e.Grade) >= 3
);

-- 10
insert into `course` ( CourseID, CourseName, CourseCredit )
values ( 8887, "Advanced Database Development", 4 );
        
-- 11
-- insert into `instructor` ( InstructorID, LastName, FirstName )
-- values ( 5507, "WuShin", "Yi" );
-- duplicated primary key

-- 12
-- insert into `section` ( CourseID, Sem, Year, InstructorID, SectionID )
-- values ( 8887, 1, 2018, 5507, 15 );
-- duplicated section ID

-- 13
update `course`
set CourseID = 9987
where CourseName = "Advanced Database Development";
-- by default there is already a ADD, we add antoher one, and there is two
-- cannot set two with the same primary key

-- 14
-- what is the specific question? set all grade to A under instructo John Chua?

-- 15
	-- join method
select st.studentid, st.LastName, st.FirstName, st.gender, st.age
from `student` as st
	left join ( 
				select * 
                from `enrollment` as en 
				where ( en.sem = 2 ) 
					and ( en.year = 2018)
				) as en_2018_2 using (studentid)
where courseid is NULL;
	-- subquery method
select st.studentid, st.LastName, st.FirstName, st.gender, st.age
from `student` as st
where st.studentid not in 
(
	select distinct en.studentid
    from `enrollment` as en
    where ( en.sem = 2 )
		and ( en.year = 2018 )
);

-- 16
	-- join method
select i.instructorid, i.lastname, i.firstname
from `instructor` as i
	left join `section` as se using (instructorid)
where sectionid is NULL;

	-- subquery method
-- EXPLAIN
select i.instructorid, i.lastname, i.firstname
from `instructor` as i
where i.instructorid not in
(
	select distinct se.instructorid
    from `section` as se
);

-- 17
select instructorid, lastname, firstname, count(sectionid)
from `instructor`
	left join `section` using (instructorid)
group by instructorid
order by count(sectionid) desc;
-- we updated the instructor list so that the result is different from the doc

select *,
	case 
		when i.instructorid in 
			( 
				select distinct se.instructorid 
				from `section` as se 
			) 
			then 
			( 
				select count( distinct sectionid ) 
				from `section` as se
				where se.instructorid = i.instructorid
			)
		else 0
	end as course_taught
from `instructor` as i
order by course_taught desc;