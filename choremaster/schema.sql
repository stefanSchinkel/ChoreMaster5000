CREATE TABLE IF NOT EXISTS chores (
    chore_id integer PRIMARY KEY AUTOINCREMENT,
    description text NOT NULL,
    multiplier integer,
    target integer
);

CREATE TABLE IF NOT EXISTS log (
    day date,
    chore_id text NOT NULL,
    counter integer,
    PRIMARY KEY (day, chore_id),
    FOREIGN KEY(chore_id) REFERENCES chores(chore_id)

);
