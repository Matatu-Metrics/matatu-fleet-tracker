CREATE TABLE routes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    route_number TEXT NOT NULL,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    strain_factor REAL NOT NULL
);

CREATE TABLE vehicles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number_plate TEXT UNIQUE NOT NULL,
    current_route_id INTEGER,
    total_odometer REAL DEFAULT 0.0,
    FOREIGN KEY (current_route_id) REFERENCES routes(id)
);

INSERT INTO routes (route_number, origin, destination, strain_factor) 
VALUES ('102', 'CBD', 'Kikuyu', 1.2), ('46', 'CBD', 'Kawangware', 1.4);

INSERT INTO vehicles (number_plate, current_route_id, total_odometer) 
VALUES ('KAA 123X', 1, 15000.50), ('KBB 789Y', 2, 8500.00);

