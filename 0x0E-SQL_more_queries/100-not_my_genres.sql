-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT DISTINCT tv_genres.id FROM tv_genres, tv_shows, tv_show_genres
	WHERE tv_show_genres.genre_id = tv_genres.id
		AND tv_show_genres.show_id = tv_shows.id
		AND tv_shows.title = 'Dexter'
) ORDER BY tv_genres.name ASC;
