use socialgram;

-- 1
select 
	name
from 
	`user`
where userid in (
	select distinct userid
	from `user-group`
	where isModerator = "Y"
);

-- 2
select 
	name
from
	`user`
where userid in (
	select userid
	from `user-group`
	where isbanned = "Y"
	group by userid
	having count(userid) >= 1
);

-- 3
select name, total_photo_filesize
from (
	select userid, sum(filesize) as total_photo_filesize
	from `user-photo`
	join `photo`
		using (photoid)
	group by userid
	having sum(filesize) > 1000
) as user_size_sum
join `user` using (userid);

-- 4
select albumname, count(userid)
from `album`
where photoid in (
	select photoid
	from `user-photo`
	group by photoid
	having count(userid) > 1
	-- get photo id that owned by more than one user
)
group by albumname;

-- 5 
create or replace view user_following_username_view as
select 
	uf.userid as userid,
	u.name,
    uf.followinguserid as followinguserid
from `user-following` as uf join `user` as u
using (userid);

select * from user_following_username_view;

select 
	a.userid,
	a.name,
    b.userid,
    b.name
from `user_following_username_view` as a join `user_following_username_view` as b on a.userid = b.followinguserid
where a.userid = b.followinguserid and a.followinguserid = b.userid;

-- 6
select 
	sub_table_1.a_name as user1,
	sub_table_1.b_name as user2,
    c.name as user3
from (
	select 
		a.userid as a_userid,
		a.followinguserid as a_followinguserid,
		a.name as a_name,
		b.userid as b_userid,
		b.followinguserid as b_followinguserid,
		b.name as b_name
	from `user_following_username_view` as a
	join `user_following_username_view` as b
	on a.followinguserid = b.userid
) as sub_table_1
join `user_following_username_view` as c
on (sub_table_1.b_followinguserid = c.userid)
where c.followinguserid = sub_table_1.a_userid
	

