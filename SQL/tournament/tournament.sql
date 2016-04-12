/* First thing is to DROP everything that already exists so I can run multiple
tests. */
DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS tournament;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS match;
DROP VIEW IF EXISTS all_players;

/* Now its possible to CREATE the database after all has been cleaned */
CREATE DATABASE tournament;
\c tournament;

/* With the DATABASE created is time to define all the TABLES for the
tournament project.*/
CREATE TABLE tournament (
    PRIMARY KEY (game_id),
    game_id   VARCHAR(50)
);

CREATE TABLE player (
    PRIMARY KEY (player_id),
    player_id SERIAL,
    full_name VARCHAR(80) UNIQUE                NOT NULL,
    game_id   VARCHAR(50) REFERENCES tournament NOT NULL
);

CREATE TABLE match (
    PRIMARY KEY (match_id, game_id),
    match_id  SERIAL,
    winner    INTEGER REFERENCES player(player_id),
    loser     INTEGER REFERENCES player(player_id),
    draw      BOOLEAN DEFAULT 'FALSE'       NOT NULL,
    game_id   TEXT    REFERENCES tournament ON DELETE CASCADE
);

CREATE VIEW standings AS
    SELECT player.player_id, player.full_name,
           COUNT(match.winner) AS wins,
           COUNT(match.winner) + COUNT(match.loser) AS matches
      FROM player
 LEFT JOIN match ON player.player_id = match.winner
  GROUP BY player.player_id
  ORDER BY wins DESC;
