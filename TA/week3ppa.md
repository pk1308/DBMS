```pgsql
SELECT t.name
FROM teams t
WHERE EXISTS (
    SELECT 1
    FROM matches m
    WHERE (m.host_team_id = t.team_id OR m.guest_team_id = t.team_id)
    GROUP BY t.team_id
    HAVING COUNT(*) > 3
)
```



```pgsql
SELECT f.faculty_fname, f.faculty_lname
FROM faculty f
INNER JOIN members m ON f.id = m.id
INNER JOIN book_issue b ON m.member_no = b.member_no
WHERE f.department_code = 'ME'

```
