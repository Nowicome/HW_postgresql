CREATE TABLE IF NOT EXISTS Genres (
	id SERIAL PRIMARY KEY,
	name_of_the_genre VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Performers (
	id SERIAL PRIMARY KEY,
	name_or_alias VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre_Performer (
	genre_id INT REFERENCES Genres(id),
	performer_id INT REFERENCES Performers(id),
	CONSTRAINT PK_2 PRIMARY KEY (genre_id, performer_id)
);

CREATE TABLE IF NOT EXISTS Albums (
	id serial PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	year_of_issue DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Performer_Album (
	performer_id INT REFERENCES Performers(id),
	album_id INT REFERENCES Albums(id),
	CONSTRAINT PK_1 PRIMARY KEY (performer_id, album_id)
);

CREATE TABLE IF NOT EXISTS Tracks (
	id serial PRIMARY KEY,
	album_id INT NOT NULL references Albums(id),
	name_of_the_track VARCHAR(60) NOT NULL,
	duration INTERVAL NOT NULL
);

CREATE TABLE IF NOT EXISTS Collections (
	id serial PRIMARY KEY,
	name_of_the_collection VARCHAR(60) NOT NULL,
	year_of_issue DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Track_Collection(
	track_id INT REFERENCES Tracks(id),
	collection_id INT REFERENCES Collections(id),
	CONSTRAINT PK PRIMARY KEY (track_id, collection_id)
);
