-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Displays NULL if show is without genres.
-- Records are ordered by ascending title and genre.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;

