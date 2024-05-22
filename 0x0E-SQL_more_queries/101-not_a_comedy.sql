-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT DISTINCT tv_shows.id FROM tv_genres, tv_shows, tv_show_genres
	WHERE tv_show_genres.genre_id = tv_genres.id
		AND tv_show_genres.show_id = tv_shows.id
		AND tv_genres.name = 'Comedy'
) ORDER BY tv_shows.title ASC;
