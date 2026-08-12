BEGIN;

-- DimCompetition
CREATE TABLE warehouse.dim_competition(
    comp_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    comp_id INTEGER NOT NULL,
    comp_name VARCHAR(60),
    country VARCHAR(40),
    tier SMALLINT,
    has_rounds BOOLEAN,
    has_groups BOOLEAN,
    has_playoff_series BOOLEAN,
    logo VARCHAR(100)
);

-- DimSeason
CREATE TABLE warehouse.dim_season(
    season_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    comp_key INTEGER NOT NULL,
    season_id INTEGER NOT NULL,
    season_year VARCHAR(8),
    season_name VARCHAR(30),
    season_start_date DATE,
    season_end_date DATE,
    number_of_competitors SMALLINT,

    CONSTRAINT fk_season_competition
        FOREIGN KEY (comp_key)
        REFERENCES warehouse.dim_competition(comp_key)
);

-- DimDate
CREATE TABLE warehouse.dim_date(
    date_key INTEGER PRIMARY KEY,
    full_date DATE NOT NULL UNIQUE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name VARCHAR(15),
    day INTEGER,
    day_of_the_week INTEGER,
    day_name VARCHAR(10),
    week_of_year INTEGER,
    is_weekend BOOLEAN
);

-- DimTeam
CREATE TABLE warehouse.dim_team(
    team_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    team_id INTEGER NOT NULL UNIQUE,
    team_name VARCHAR(50),
    short_name VARCHAR(15),
    name_code VARCHAR(4),
    slug VARCHAR(100),
    gender CHAR(1),
    country VARCHAR(30),
    country_code VARCHAR(4),
    national BOOLEAN
);

-- DimVenue
CREATE TABLE warehouse.dim_venue(
    venue_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    venue_id INTEGER NOT NULL UNIQUE,
    venue_name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(50),
    capacity INTEGER,
    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6)
);

--FactMatch
CREATE TABLE warehouse.fact_match(
    match_key INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    match_id INTEGER NOT NULL UNIQUE,
    date_key SMALLINT NOT NULL,
    comp_key INTEGER,
    season_key INTEGER,
    home_team_key INTEGER,
    away_team_key INTEGER,
    venue_key SMALLINT,
    match_start_time TIME,
    round_num SMALLINT,
    round_name VARCHAR(50),
    round_slug VARCHAR(50),
    cup_round_type VARCHAR(50),
    home_score SMALLINT,
    away_score SMALLINT,
    home_normal_time_goals SMALLINT,
    away_normal_time_goals SMALLINT,
    home_first_half_goals SMALLINT,
    away_first_half_goals SMALLINT,
    home_second_half_goals SMALLINT,
    away_second_half_goals SMALLINT,
    home_extra_time_goals SMALLINT,
    away_extra_time_goals SMALLINT,
    home_penalty_goals SMALLINT,
    away_penalty_goals SMALLINT,
    winner_code SMALLINT,

    CONSTRAINT fk_match_date
        FOREIGN KEY (date_key)
        REFERENCES warehouse.dim_date(date_key),
    CONSTRAINT fk_match_comp
        FOREIGN KEY (comp_key)
        REFERENCES warehouse.dim_competition(comp_key),
    CONSTRAINT fk_match_season
        FOREIGN KEY (season_key)
        REFERENCES warehouse.dim_season(season_key),
    CONSTRAINT fk_home_team
        FOREIGN KEY (home_team_key)
        REFERENCES warehouse.dim_team(team_key),
    CONSTRAINT fk_away_team
        FOREIGN KEY (away_team_key)
        REFERENCES warehouse.dim_team(team_key),
    CONSTRAINT fk_match_venue
        FOREIGN KEY (venue_key)
        REFERENCES warehouse.dim_venue(venue_key)

);


COMMIT;