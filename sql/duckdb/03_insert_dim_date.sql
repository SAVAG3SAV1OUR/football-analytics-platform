INSERT INTO warehouse.dim_date
SELECT
    CAST(strftime(date_value, '%Y%m%d') AS INTEGER) AS date_key,
    date_value AS full_date,
    EXTRACT(YEAR FROM date_value) AS year,
    EXTRACT(QUARTER FROM date_value) AS quarter,
    EXTRACT(MONTH FROM date_value) AS month,
    strftime(date_value, '%B') AS month_name,
    EXTRACT(DAY FROM date_value) AS day,
    EXTRACT(DOW FROM date_value) AS day_of_the_week,
    strftime(date_value, '%A') AS day_name,
    EXTRACT(WEEK FROM date_value) AS week_of_year,
    EXTRACT(DOW FROM date_value) IN (0,6) AS is_weekend
FROM generate_series(
    DATE '2000-01-01',
    DATE '2035-12-31',
    INTERVAL '1 day'
) AS t(date_value);