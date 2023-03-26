CREATE SCHEMA extract_news;

CREATE TABLE extract_news.post (
	id serial4 PRIMARY KEY,
	title varchar(500),
	link varchar(500),
	created_at timestamp,
	updated_at timestamp
);

CREATE TABLE extract_news.raw_response (
	id serial4 PRIMARY KEY,
	"data" jsonb,
	created_at timestamp,
	updated_at timestamp
);
