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
    number_of_competitors SMALLINT

    CONSTRAINT fk_season_competition
        FOREIGN KEY (comp_key)
        REFERENCES warehouse.dim_competition(comp_key)
);

-- DimDate
CREATE TABLE warehouse.dim_date(
    date_key SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
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
    team_key SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
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
    venue_key SMALLINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    venue_id INTEGER NOT NULL UNIQUE,
    venue_name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(50),
    capacity INTEGER,
    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6)
);