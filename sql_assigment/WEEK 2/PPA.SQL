SELECT m.name
FROM managers m
INNER JOIN teams t ON m.team_id = t.team_id
WHERE t.name = 'All Stars'

select b.title 
from book_catalogue b 
inner join book_authors a on  b.ISBN_no= a.ISBN_no 
where  a.author_fname= 'Joh Paul'
and a.author_lname = 'Mueller';

select  s.student_fname , s.student_lname from students s 
where s.roll_no in (select m.roll_no from members m where m.member_type= 'PG');
