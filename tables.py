import pandas as pd
import numpy as np
import sqlite3

# Connect to the data base.

conn = sqlite3.connect('traffic_data.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Create the "routes" table.

cursor.execute('''CREATE TABLE routes
        (route_name text PRIMARY KEY, origin text, destination text) ''')

# Insert routes.

cursor.execute(''' INSERT INTO routes VALUES
        ("atirantado_leones_entrada", "Av Raúl Rangel Frías 3234, Cumbres 1º. Sector Secc a, 64610 Monterrey, N.L., Mexico",
        "Avenida Humberto Lobo 707, Del Valle, 66225 San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("atirantado_leones_salida", "Avenida Humberto Lobo 707, Del Valle, 66225 San Pedro Garza García, N.L., Mexico",
        "Av Raúl Rangel Frías 107-C, Cumbres 1º. Sector Secc a, 64610 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("atirantado_periferico_entrada", "Blvd. Rogelio Cantú Gómez 1000-C, Sin Nombre de Col 72, 64639 Monterrey, N.L., Mexico",
        "Avenida Humberto Lobo 707, Del Valle, 66225 San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("atirantado_periferico_salida", "Avenida Humberto Lobo 707, Del Valle, 66225 San Pedro Garza García, N.L., Mexico",
        "Blvd. Rogelio Cantú Gómez 210, Sin Nombre de Col 72, Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("calzada_entrada", "Calz San Pedro 107-S, Miravalle, 64660 Monterrey, N.L., Mexico",
        "Calz San Pedro 106, Del Valle, 66220 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("calzada_salida", "Calz San Pedro 103, Del Valle, 66220 Monterrey, N.L., Mexico",
        "Calz San Pedro 105, Miravalle, 64660 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("ladiana_entrada", "Dr. José Eleuterio González (Gonzalitos), Mitras Nte., 64320 Monterrey, N.L., Mexico",
        "Monterrey-Santiago 20, Los Doctores, Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("ladiana_salida", "Dr. José Eleuterio González (Gonzalitos), Los Doctores, Monterrey, N.L., Mexico",
        "Dr. José Eleuterio González (Gonzalitos), Mitras Nte., 64320 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("tunel_entrada", "Av. Venustiano Carranza 1068, Industrial, 64440 Monterrey, N.L., Mexico",
        "Av. Real San Agustin, Zona Loma Larga Oriente, San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("tunel_salida", "Av. Real San Agustin & Eje Metropolitano 11, San Pedro Garza García, N.L., Mexico",
        "Av. Venustiano Carranza 1001, Industrial, 64440 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("lazaro_entrada", "Estatua Lázaro Cárdenas, México 85, Las Torres, Monterrey, N.L., Mexico",
        "Calz. del Valle Alberto Santos 433-555, Valle de Santa Engracia, San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("lazaro_salida", "Avenida José Vasconcelos 265, Valle del Campestre, 66265 San Pedro Garza García, N.L., Mexico",
        "Estatua Lázaro Cárdenas, México 85, Las Torres, Monterrey, N.L., Mexico")''')

conn.commit()

# Create the "traffic" table.

cursor.execute('''CREATE TABLE traffic
        (traffic_id integer PRIMARY KEY, route_name text, date_time text, distance integer, velocity integer,
        duration_traffic integer, avg_delay integer, FOREIGN KEY (route_name) REFERENCES routes (route_name)) ''')

conn.close()




















