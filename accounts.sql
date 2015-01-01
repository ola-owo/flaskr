DROP TABLE if exists users;
CREATE TABLE users(
  id INTEGER PRIMARY KEY autoincrement,
  username TEXT NOT NULL,
  salted_hash TEXT NOT NULL
);
