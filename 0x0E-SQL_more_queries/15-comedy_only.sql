-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres x ON m.genre_id = x.id
WHERE x.name = 'Comedy'
ORDER BY tv_shows.title ASC;
