--Задание 2
--Название и продолжительность самого длительного трека
SELECT name_of_the_track, duration
FROM tracks
ORDER BY duration DESC
LIMIT 1;

--Название треков, продолжительность которых не менее 3,5 минут
SELECT name_of_the_track, duration
FROM tracks
WHERE duration >= time '00:03:30';

--Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name_of_the_collection, year_of_issue
FROM collections
WHERE EXTRACT (YEAR FROM year_of_issue) BETWEEN 2018 AND 2020;

--Исполнители, чьё имя состоит из одного слова
SELECT name_or_alias
FROM performers
WHERE name_or_alias NOT LIKE '% %';

--Название треков, которые содержат слово «мой» или «my»
SELECT name_of_the_track, duration
FROM tracks
WHERE lower(name_of_the_track) SIMILAR TO '(my|my %|% my %|% my|мой|мой %|% мой %|% мой)';

--Задание 3
--Количество исполнителей в каждом жанре
SELECT name_of_the_genre, count(performer_id) p FROM genres g
JOIN genre_performer gp ON g.id = gp.genre_id
GROUP BY g.name_of_the_genre
ORDER BY p DESC;

--Количество треков, вошедших в альбомы 2019–2020 годов
SELECT count(name_of_the_track) n FROM tracks t
JOIN albums a ON t.album_id = a.id
WHERE EXTRACT (YEAR FROM year_of_issue) BETWEEN 2019 AND 2020;

--Средняя продолжительность треков по каждому альбому
SELECT title, avg(duration) d FROM albums a
JOIN tracks t ON a.id = t.album_id
GROUP BY a.title
ORDER BY d DESC;

--Все исполнители, которые не выпустили альбомы в 2020 году
SELECT name_or_alias FROM performers
WHERE name_or_alias NOT IN (
	SELECT name_or_alias FROM performers p
	JOIN performer_album pa ON p.id = pa.performer_id
	JOIN albums a ON pa.album_id = a.id
	WHERE EXTRACT (YEAR FROM a.year_of_issue) = 2020
	);

--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами)
SELECT DISTINCT name_of_the_collection FROM collections co
JOIN track_collection tc ON co.id = tc.collection_id
JOIN tracks t ON tc.track_id = t.id
JOIN albums al ON t.album_id = al.id
JOIN performer_album pa ON al.id = pa.album_id
JOIN performers p ON pa.performer_id = p.id
WHERE p.name_or_alias = 'Rammstein';

--Задание 4(необязательное)
--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT DISTINCT a.title FROM albums a
JOIN performer_album pa ON a.id = pa.album_id
JOIN performers p ON pa.performer_id = p.id
JOIN genre_performer gp ON p.id = gp.performer_id
GROUP BY a.title, gp.performer_id
HAVING count(gp.genre_id) > 1;

--Наименования треков, которые не входят в сборники
SELECT name_of_the_track FROM tracks t
WHERE t.id NOT IN (
	SELECT t2.id FROM tracks t2
	JOIN track_collection tc2 ON t2.id = tc2.track_id
	);

--Исполнитель или исполнители, написавшие самый короткий по продолжительности
--трек, — теоретически таких треков может быть несколько
SELECT p.name_or_alias, t.duration FROM tracks t
JOIN albums a ON t.album_id = a.id
JOIN performer_album pa ON a.id = pa.album_id
JOIN performers p ON pa.performer_id = p.id
GROUP BY p.name_or_alias, t.duration
HAVING t.duration = (SELECT min(duration) FROM tracks)
ORDER BY p.name_or_alias;

--Названия альбомов, содержащих наименьшее количество треков
SELECT a.title, count(t.id) FROM albums a
JOIN tracks t ON a.id = t.album_id
GROUP BY a.title
HAVING count(t.id) = (
	SELECT count(id) FROM tracks
	GROUP BY album_id
	ORDER BY count
	LIMIT 1
	)
ORDER BY a.title;
