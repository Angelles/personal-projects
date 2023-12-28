DROP TABLE IF EXISTS tasks; --Delete the table if it exists already, to avoid confusion.

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT, --Add id column. This is the primary key and it will autoincrement.
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, --Add create time column. Must contain a value. It will use the current timestamp.
    title TEXT NOT NULL, --Add title column. Must contain text.
    content TEXT NOT NULL, --Add content column. Must contain text.
    status TEXT NOT NULL --Add status column. Must contain text.
);