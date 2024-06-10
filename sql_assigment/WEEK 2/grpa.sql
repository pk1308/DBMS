select match_num from matches where host_team_score > guest_team_score

select jersey_home_color, jersey_away_color from teams where name = 'All Stars'

select players.player_id , players.name 
	from players 
	left join teams on  
	players.team_id = teams.team_id 
	where teams.name = 'Arawali'

select  s.student_fname , s.mobile_no 
	from students s
	Where s.department_code = 'EE';

select faculty.id  from faculty 
	where faculty.department_code = 
	(select departments.department_code from departments
	where departments.department_name='Mechanical Engineering')
	and faculty.doj = '2016-04-08';