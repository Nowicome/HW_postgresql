INSERT INTO performers (name_or_alias)
VALUES('Linkin Park');

INSERT INTO performers
VALUES(3, 'Rammstein');

INSERT INTO performers
VALUES(4, 'EastNewSound');

INSERT INTO performers
VALUES(10, 'Red Hot Chili Peppers');

INSERT INTO performers
VALUES(11, 'Robert Ziegler');

INSERT INTO genres (name_of_the_genre)
VALUES('rock');

INSERT INTO genres
VALUES(3, 'industrial metal');

INSERT INTO genres
VALUES(4, 'Electronic');

INSERT INTO genres
VALUES(9, 'trance');

INSERT INTO genres
VALUES(10, 'OST');

INSERT INTO genre_performer (genre_id, performer_id)
VALUES('1', '1');

INSERT INTO genre_performer (genre_id, performer_id)
VALUES('3', '3');

INSERT INTO genre_performer (genre_id, performer_id)
VALUES('4', '4');

INSERT INTO genre_performer (genre_id, performer_id)
VALUES('9', '4');

INSERT INTO genre_performer (genre_id, performer_id)
VALUES('1', '10');

INSERT INTO genre_performer (genre_id, performer_id)
VALUES('10', '11');

INSERT INTO albums (title, year_of_issue)
VALUES('Mutter', '02.04.2001');

INSERT INTO albums (title, year_of_issue)
VALUES('A Thousand Suns', '08.09.2010');

INSERT INTO albums (title, year_of_issue)
VALUES('EastNewSound 5th Anniversary Premium Best', '11.05.2014');

INSERT INTO albums (title, year_of_issue)
VALUES('By the Way', '09.07.2002');

INSERT INTO albums (title, year_of_issue)
VALUES('Californication', '08.06.1999');

INSERT INTO albums (title, year_of_issue)
VALUES('MUSIC FROM THE STAR WARS SAGA - THE ESSENTIAL COLLECTION', '04.04.2020');

INSERT INTO albums (title, year_of_issue)
VALUES('Zenyamikyoku', '15.07.2020');

INSERT INTO albums (title, year_of_issue)
VALUES('Living Things', '26.06.2012');

INSERT INTO performer_album (performer_id, album_id)
VALUES('3', '1');

INSERT INTO performer_album (performer_id, album_id)
VALUES('1', '2');

INSERT INTO performer_album (performer_id, album_id)
VALUES('4', '3');

INSERT INTO performer_album (performer_id, album_id)
VALUES('10', '4');

INSERT INTO performer_album (performer_id, album_id)
VALUES('10', '5');

INSERT INTO performer_album (performer_id, album_id)
VALUES('11', '6');

INSERT INTO performer_album (performer_id, album_id)
VALUES('4', '7');

INSERT INTO performer_album (performer_id, album_id)
VALUES('1', '8');

INSERT INTO collections (name_of_the_collection, year_of_issue)
VALUES('Made in Germany 1995—2011', '02.12.2011');

INSERT INTO collections (name_of_the_collection, year_of_issue)
VALUES('Studio Collection', '15.01.2013');

INSERT INTO collections (name_of_the_collection, year_of_issue)
VALUES('EastNewSound 5th Anniversary Premium Best', '11.05.2014');

INSERT INTO collections (name_of_the_collection, year_of_issue)
VALUES('Greatest Hits', '03.11.2003');

INSERT INTO collections (name_of_the_collection, year_of_issue)
VALUES('MUSIC FROM THE STAR WARS SAGA - THE ESSENTIAL COLLECTION', '04.04.2020');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('1', 'Mein Herz brennt', '4 minutes 39 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('1', 'Mutter', '4 minutes 28 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('1', 'Links 2 3 4', '3 minutes 40 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('1', 'Sonne', '4 minutes 05 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('1', 'Feuer frei!', '4 minutes 10 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('1', 'Ich will', '3 minutes 37 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('2', 'The Requiem', '2 minutes 01 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('2', 'When They Come for Me', '4 minutes 54 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('2', 'Waiting for the End', '3 minutes 52 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('2', 'Blackout', '4 minutes 40 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('2', 'Wretches and Kings', '4 minutes 11 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('2', 'Iridescent', '4 minutes 57 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('3', 'contrivance', '5 minutes 35 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('3', 'Urahara ff', '4 minutes 44 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('3', 'Rot in hell !!', '6 minutes 28 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('3', 'Limited Dimension', '5 minutes 26 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('4', 'By the Way', '3 minutes 35 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('4', 'Universally Speaking', '4 minutes 16 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('5', 'Californication', '5 minutes 29 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('5', 'Parallel Universe', '4 minutes 29 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('6', 'STAR WARS: MAIN TITLE', '5 minutes 52 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('6', 'YODA"S THEME', '3 minutes 26 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('6', 'BATTLE OF THE HEROES', '3 minutes 45 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('6', 'THE FOREST BATTLE', '4 minutes 06 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('7', 'Same Nightmare', '4 minutes 29 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('7', 'Wither', '5 minutes 27 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('7', 'Requiem of Revenge', '4 minutes 32 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('8', 'Lost in the Echo', '3 minutes 25 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('8', 'In My Remains', '3 minutes 20 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('8', 'Burn It Down', '3 minutes 52 seconds');

INSERT INTO tracks (album_id, name_of_the_track, duration)
VALUES('8', 'Lies Greed Misery', '2 minutes 27 seconds');

INSERT INTO track_collection (track_id, collection_id)
VALUES('2', '1');

INSERT INTO track_collection (track_id, collection_id)
VALUES('3', '1');

INSERT INTO track_collection (track_id, collection_id)
VALUES('4', '1');

INSERT INTO track_collection (track_id, collection_id)
VALUES('5', '1');

INSERT INTO track_collection (track_id, collection_id)
VALUES('6', '1');

INSERT INTO track_collection (track_id, collection_id)
VALUES('7', '1');

INSERT INTO track_collection (track_id, collection_id)
VALUES('8', '2');

INSERT INTO track_collection (track_id, collection_id)
VALUES('9', '2');

INSERT INTO track_collection (track_id, collection_id)
VALUES('10', '2');

INSERT INTO track_collection (track_id, collection_id)
VALUES('11', '2');

INSERT INTO track_collection (track_id, collection_id)
VALUES('12', '2');

INSERT INTO track_collection (track_id, collection_id)
VALUES('13', '2');

INSERT INTO track_collection (track_id, collection_id)
VALUES('14', '3');

INSERT INTO track_collection (track_id, collection_id)
VALUES('15', '3');

INSERT INTO track_collection (track_id, collection_id)
VALUES('16', '3');

INSERT INTO track_collection (track_id, collection_id)
VALUES('17', '3');

INSERT INTO track_collection (track_id, collection_id)
VALUES('18', '4');

INSERT INTO track_collection (track_id, collection_id)
VALUES('19', '4');

INSERT INTO track_collection (track_id, collection_id)
VALUES('20', '4');

INSERT INTO track_collection (track_id, collection_id)
VALUES('21', '4');

INSERT INTO track_collection (track_id, collection_id)
VALUES('22', '5');

INSERT INTO track_collection (track_id, collection_id)
VALUES('23', '5');

INSERT INTO track_collection (track_id, collection_id)
VALUES('24', '5');

INSERT INTO track_collection (track_id, collection_id)
VALUES('25', '5');