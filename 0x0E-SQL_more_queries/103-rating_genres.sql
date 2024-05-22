-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) AS rating FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS sg ON g.id = sg.genre_id
INNER JOIN `tv_shows` AS s ON s.id = sg.show_id
INNER JOIN `tv_show_ratings` AS r ON s.id = r.show_id
GROUP BY g.id
ORDER BY rating DESC;
