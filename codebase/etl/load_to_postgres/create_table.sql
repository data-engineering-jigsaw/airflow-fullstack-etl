CREATE TABLE flights (
    id serial PRIMARY KEY,
    departure_time timestamp,
    arrival_time timestamp,
    departure_airport VARCHAR(3),
    arrival_airport VARCHAR(3)
);