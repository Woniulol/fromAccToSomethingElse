use `hospital`;

-- 1
select s.staffname, s.staffno
from `staff` as s
where s.staffno in (
	select d.staffno
	from `doctor` as d
	where d.position = "Associate doctor"
)
order by s.staffno;

-- 2
select p.patientname
from `patient` as p
where doctorno = (
	select s.staffno
	from `staff` as s
	where (s.staffname = "Saanvi Anand")
		and (s.stafftype = "doctor")
);

-- 3
select p.wardno, 
	count(p.patientid) as amt_patients
from `patient` as p
group by p.wardno;

-- 4
select p.wardno, 
	count(p.patientid) as amt_patients,
    w.maxbeds
from `patient` as p
	join `ward` as w using(wardno)
group by p.wardno, w.maxbeds 
having (count(p.patientid) / w.maxbeds) > (1 / 3);

-- 
-- select *
-- from 
--  (select wardno, maxbeds,maxbeds/3 as cutoff
-- from ward) as a,
-- (
-- select wardno, count(*)
-- from patient
-- group by wardno) as b;

-- 5
select p.patientid, p.patientname
from `patient` as p
where patientname in (
	select p.patientname
	from `patient` as p
	group by p.patientname
	having count(p.patientname) > 1
);

-- 6
select s.staffname
from `staff` as s
where s.staffno in (
	select n.staffno
	from `nurse` as n
	where n.supno is NULL
);


-- 7
select s.staffname
from `staff` as s
where s.staffno in (
	select n.staffno
	from `nurse` as n
	where n.supno = (
		select s.staffno
		from staff as s
		where s.staffname = "Cammy Soh"
	)
);

-- 8
select distinct s.staffname
from `staff` as s
where ( s.staffno not in 
	(
		select distinct p.doctorno
		from `patient` as p
	)
) and (s.stafftype = 'doctor')

