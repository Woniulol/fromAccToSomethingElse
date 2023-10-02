use `ia`;

/* description

- a corresponding answer VIEW will been created for each question to conclued the final answer and will be
named as "qn_view", e.g. q1_view, q2_view.
- run the entire script to create all the views
- See notes for explainations and additional clarifications.

*/

/* Question 1

1) Table considered: <postalCodeTBL>
What are the unique [generalLoc]?

*/
create or replace view q1_view as
select distinct generalloc as distinct_generalloc
from `postalcodetbl`;

select * from q1_view;

/* Question 2

2) Table considered: <incidentTypeTBL>
How many incident types are related to speed limit issues?

*/
create or replace view q2_view as
select count(distinct detail) as amt_speed_related
from `incidenttypetbl`
where detail like "%speed limit%";

select * from q2_view;

/* Question 3

3) Table considered: <incidentTBL>
For each [year], on each [incidentType], how many incidents are recorded?

*/
create or replace view q3_view as
select 
	right(date, 4) as year, -- the date column is text
	incidenttype as incident_type,
    count(distinct incidentid) as amt_incidnet
from `incidenttbl`
group by 
	right(date, 4), 
    incidenttype;

select * from q3_view;

-- check for q3
-- sum of amt_incidnet should equal to total record number 962 in incidenttbl
select sum(amt_incidnet) as tot_amtincidenttbl
from `q3_view`;

/* Question 4

4) Tables considered: <complaintTBL> + <customerTBL>
For each year (2010 to 2018), on each issue category, display the total number of complaints, and the respective breakdowns between females and males

*/
create or replace view q4_view as
select 
	right(cttbl.date, 4) as year,
	cttbl.issue,
    crtbl.gender,
    count(distinct cttbl.complaintid) as amt_complaint
from `complainttbl` as cttbl
join `customertbl` as crtbl 
	using (customerid)
group by 
	right(cttbl.date, 4), 
	cttbl.issue,
    crtbl.gender;
    
select * from q4_view;

-- check for question 4
-- the total number of records in q4_veiw should equal to the records amount in complainttbl 530
select sum(amt_complaint)
from q4_view;

/* Question 5

5) Tables considered: <vehicleTBL> + <orderTBL> + <customerTBL> + <postalcodeTBL>
For each year, on each generalLoc, display the total customer value (i.e., total rental fees recorded for the year).
Note: You need to sum up the values for the same generalLoc (under different postalCode).

*/
-- a. check if all the orders start and end in the same day
(
	select 
		"different date",
		count(distinct orderid) as amt_orders
	from `ordertbl`
	where startdate <> enddate
)
union
(
	select 
		"same date",
		count(distinct orderid) as amt_orders
	from `ordertbl`
	where startdate = enddate
);
-- since all the orders start and end in the same day, we only need to consider the hhmmss

-- b. answer

create or replace view q5_view as
select 
	order_year, 
	generalLoc,
    sum((fee_per_hour * ordertbl_sub.hr_used)) as fee_per_order
from
(
	select orderid, vehicleid, customerid, startLoc,
		extract(Year from(str_to_date(startdate, '%e-%b-%Y'))) as order_year,
		round((convert(endtime_hr, decimal(0)) + convert(endtime_min, decimal(0)) / 60)) - round((convert(starttime_hr, decimal(0)) + convert(starttime_min, decimal(0)) / 60)) as hr_used
	from `ordertbl` 
    where startLoc = endloc
) as ordertbl_sub  -- 1. calculate the time(hrs) difference for each order
join 
(
	select vehicleid, convert(fee_per_hour, decimal(0)) as fee_per_hour
	from `vehicletbl` 
) as vetbl_sub 
	using (vehicleid) -- 2. get the fee_per_hcustomertblour for the veichal in each order and join with 1. based on vehicleid
join
(
	select postalCode, generalLoc
    from `postalcodetbl`
) as petbl_sub
	on (startLoc = postalCode)
group by order_year, generalLoc;
    
select * from q5_view;

/* Question 6

6)	Tables considered: <complaintTBL> + < orderTBL > + <vehicleTBL>
Complaint analytics. The purpose of this query is to prepare the data for analyses on complaint frequency and patterns.
For each year, on each vehicle, display the average traveled distance for a complaint. 
Note: If you encounter problems with the data, provide a script to illustrate the issue. You can also propose possible workarounds.

*/
-- check the complaintid amt for each customer
select customerID, count(complaintID)
from `complainttbl`
group by customerid;
-- one customer could have multiple compliantid
-- and obviously a customer could also have multiple orderid

-- check if the date is distinct for each customer
select 
	customerid,
    count(distinct date) = count(distinct complaintid)
from `complainttbl`
group by customerid;
-- it is safe the say a customer won't complaint twice in a day

-- check if the order date is distinct for customer
select
	customerid,
    count(distinct startdate) = count(distinct orderid)
from `ordertbl`
group by customerid;
-- not entirly, some customer could order more than once in a single day

-- suprisingly, the sum of distance_m in ordertbl of each car is not the same as the total distance_km in vehicletbl
select 
	vehicleID, 
	sum(distance_m) / 1000,
    (
		select total_distance_km 
		from `vehicletbl`
		where vehicleid = 10
	)
from `ordertbl`
where vehicleID = 10;
-- we infer that the ordertbl is not a compelet dataset

-- as in last question, we already checke dthat the stardate and enddate of a order is always the same
create or replace view order_complaint_date_relation_view as
select 
	customerid, 
    orderid, 
    vehicleid,
    orderdate, 
    complaintdate, 
    complaintid,
	(complaintdate - orderdate) as days_complaint_after_order,
	min(complaintdate - orderdate) over (partition by complaintid) as minimal_internal
	-- partition by is used to calculated the minimal interval based on each complaintid
    -- we calculate the minimal date interval between the complaint and a order date and assume the complaint is about that orderid so that we can track the vehicleid
from 
(
	select customerid, orderid, vehicleid, str_to_date(startdate, '%e-%b-%Y') as orderdate
	from `ordertbl`
) as sub_order
join 
(
	select customerid, complaintid, str_to_date(date, '%M %e, %Y') as complaintdate
	from `complainttbl`
) as sub_complaint
	using (customerid)
where ((complaintdate - orderdate) >= 0);  -- complaint about a order(vehicle) should only happen after the order date

select * from `order_complaint_date_relation_view`;

-- some validation process
select distinct complaintid
from `order_complaint_date_relation_view`;
-- only returns 500 rows, doesnot match the complainttbl which has 530 rows
-- some complaintid were removed when building the view

select complaintid, count(complaintid)
from `order_complaint_date_relation_view`
where days_complaint_after_order = minimal_internal
group by complaintid;
-- all complaintids are distinct

select orderid, count(orderid)
from `order_complaint_date_relation_view`
where days_complaint_after_order = minimal_internal
group by orderid;
-- but not all orderid is distinct
-- some complaint is bound to a single orderid. plz see the problem 2 in below

/* potential problems about the dataset

- the root problem is that we don't have a direct and accurate way to link complainttbl to ordertbl, 
i.e. we don't know which orderid (and thus the vehicleid) a complain is talking about

- our way to mitigate such problem is try to find the minimal date interval between an order and a compliant date and assuming that the customer is complaining the most recent order
e.g. if a customer complain in 2000-12-31, and has three orders in 2000-06-30, 2000-07-31, 2000-08-31, we assume the compliant is on the third order on 2000-08-31

- however, it results two problems

- 1. it is resonable to assume that a complaint can only happen after a customer has finished at least one order. i.e. the complaint date should be later than at least one orderdate.
however, we found 30 compliantid dont have a previous orderdate, indicating that the order data is not complete. plz refer to part 6-1 in below.

- 2. the second question is that a customer could have two complaints in a short period, during which no new order has been made, so that the most recent order for both complaints is the same
order. e.g. customer order in 2000-10-31, 2000-11-30, and complaint each order in 2000-12-01 and 2000-12-31, then, in our method, both complaint is believed to be made based on the order 
in 2000-11-30, which, agian, compromise the anaylis result. plz refer to part 6-2 in below.

- based on the findings above, we make the following assumption to guide further analysis

- 0. customer will only complain after placing at least one order
- 1. we assume that one customer won't complain twice on the same order
- 2. we assume that customer only complian about the most recent orderid (as of the complaint date) and thus the vechicle

- any compliantid that violates the above assumptions will be ignored
*/

-- 6-1
select distinct complaintid
from `order_complaint_date_relation_view`;
-- the return row number should be equal to the row number of total complainttble
-- but we only get 500 rows, which means, some complaintid were dropped when creating the viwe by condition where ((complaintdate - orderdate) >= 0)
-- i.e. not every one of the complaintid has a orderdate prior to that complaint, which violates assumption 0
-- (we already checked there is no duplicated compliantid in the view)

create or replace view illegal_complaintid_view as
select distinct complaintid
from `complainttbl` -- include both positive and negative (complaintdate - orderdate) (without the condition where ((complaintdate - orderdate) >= 0) in the view)
where complaintid not in (
	select complaintid
	from `order_complaint_date_relation_view`
);

select * from illegal_complaintid_view;
-- exactly, we get 30 rows. these 30 rows violates our assumption 0

-- we try to verify the date violation condition
select *,
	sub_complaint.complaintdate - sub_order.earliest_orderdate < 0 as illigal_check
from(
	select customerid, complaintid, str_to_date(date, '%M %e, %Y') as complaintdate
	from `complainttbl`
	where complaintid in (select * from illegal_complaintid_view) -- get the compalintdate for those potential illegal complaint
) as sub_complaint
	join (
	select customerid, min(str_to_date(startdate, '%e-%b-%Y')) as earliest_orderdate
	from `ordertbl` 
	group by customerid -- get the earliest orderdate for a customer
) as sub_order
	using (customerid); 
-- clearly, all these complaintid is earlier than the earlest orderdate for the feedback customer
-- you can also easily check if all the complaintid included in the view is legal (i.e. has a earlier orderid) by adding a not in the first where clause

-- 6-2
select orderid, count(orderid)
from `order_complaint_date_relation_view`
where days_complaint_after_order = minimal_internal
group by orderid
having count(orderid) > 1;
-- we check if all corresponded selected orderid is distinct and not surprisingly, no
-- e.g. after orderid 4477 (2016-09-16), before the customer(479) make the next order in 2017-04-01, the customer provided 3 compliant in 2016-10-16, 2017-02-10, and 2017-01-08
-- so that all three complaint id is bounded to order 4477
-- we have 19 distinct orderid that has been bounded by multiple compliantid

-- we also checked if one complaint could be bound to two or more orderid when a customer order more than once a day
-- so that a compalintid has the same minimal date interval with more than one orderid
select customerid from `order_complaint_date_relation_view` 
where minimal_internal = days_complaint_after_order 
group by customerid, complaintid having count(distinct orderid) > 1;
-- it returns null and means one complaint will trace to one and only one orderid, even though on orderid could be traced by multiple complaintid as above

-- to follow our assumption to tackle with problem 2, we will only keey the one complaintid that has the cloest time relationship with the orderid
create or replace view tidy_order_complaint_relation_view as
select *
from 
(
	select *, rank() over (partition by orderid order by minimal_internal) as sequence_num 
    -- we only use the minimal_interval as the order rule since we already checked all no customer is making more than one complaint per day
	from 
		`order_complaint_date_relation_view`
	where minimal_internal = days_complaint_after_order
) as select_from
where sequence_num = 1;

select * from tidy_order_complaint_relation_view;

-- we calculate the total distance and complaint amt based on the corresponding order date
create or replace view q6_view as 
select 
	year, 
	vehicleid,
    tot_distance_km,
	IFNULL(amt_complaint, 0) as amt_complaint,
    case
		when IFNULL(amt_complaint, 0) = 0 then "N.A."  -- handle 0 complaint
        else round(tot_distance_km / amt_complaint, 2)
	end as avg_complaint_per_km
from
(
	select extract(year from str_to_date(startdate, '%e-%b-%Y')) as year, vehicleid, round(sum(distance_m) / 1000, 2) as tot_distance_km
	from `ordertbl`
	group by extract(year from str_to_date(startdate, '%e-%b-%Y')), vehicleid
) as total_distance_of_year_vehicleid  -- 1. get the total distance km for each vehicleid in each year
left join  -- use left outer join since not all vehicle in each year got an complaint
(
	select year, vehicleid, count(complaintid) as amt_complaint
	from
	(
	select extract(year from orderdate) as year, complaintid, orderid, vehicleid
	from `tidy_order_complaint_relation_view`
	) as sub_table
	group by year, vehicleid -- 2. get the total complaint for each vehicleid in each year
) as total_complaint_of_year_vehicleid
	using (year, vehicleid); -- 3. join two sub table based on the two columns

select * from `q6_view`;

/* Question 7

7) Tables considered: <customerTBL> + < orderTBL > + <vehicleTBL>
Who makes the green choices? The purpose of this query is to prepare the data for analyses on green consumption.

*/

-- only volkswagen has two models, all other brands has only one model
select brand,
	count(distinct model)
from `vehicletbl`
group by brand;

-- answer view
create or replace view q7_view as
select 
	age_category, 
    gender, 
    brand, 
    model, 
    count(model) as rent_num,
    round(count(model) / sum(count(model)) over (partition by age_category) * 100, 2) as perc
from ( 
		select orderid, customerid, vehicleID, (select count(*) from `ordertbl`) as total_num
		from `ordertbl`
) as sub_ordertbl  -- get keys to connect revelent infor
join (
		select customerid, gender,
            case
				when (age >= 21) and (age <= 30) then "between 21 and 30"
                when (age >= 31) and (age <= 50) then "between 31 and 50"
                when (age >= 51) then ">=51"
                else "99999"
			end as age_category
		from `customertbl`
) as sub_customertbl  -- get gender, age and classify age group
	using (customerid)
join (
	select vehicleid, brand, model
	from `vehicletbl`
) as sub_vehicletbl  -- get brand and model info
	using (vehicleid)
group by gender, age_category, brand, model, total_num;

select * from `q7_view`;

-- further analysis on green choices
-- we use co2avg_wltp as standard to evalue how environmental friendly a model is
select 
	model,
    avg(CO2avg_WLTP),
	RANK() OVER (ORDER BY avg(CO2avg_WLTP)) AS co2_rank
    -- the higer the value, the worse
from `vehicletbl`
group by model;

select *
from q7_view
join
(
	select model, avg(CO2avg_WLTP), RANK() OVER (ORDER BY avg(CO2avg_WLTP)) AS co2_rank
		-- the higer the value, the worse
	from vehicletbl
	group by model
) as gree_or_not
	using (model);

/* finding

young male contributes to the Avalon model (the most environmental friendly model) most

a large portion of the rent is contributed by environmental friendly model

*/
