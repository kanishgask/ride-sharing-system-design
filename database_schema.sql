CREATE TABLE riders (
rider_id INT PRIMARY KEY,
name VARCHAR(100)
);

CREATE TABLE drivers (
driver_id INT PRIMARY KEY,
location VARCHAR(100),
available BOOLEAN
);

CREATE TABLE rides (
ride_id INT PRIMARY KEY,
rider_id INT,
driver_id INT,
status VARCHAR(50)
);
