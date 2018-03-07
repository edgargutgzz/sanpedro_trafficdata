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
        ("calzada_entrada", "Calz San Pedro 107-S, Miravalle, 64660 Monterrey, N.L., Mexico",
        "Eje Metropolitano 7 420, Del Valle, 66220 San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("calzada_salida", "Calz San Pedro 501, Fuentes del Valle, 66220 San Pedro Garza García, N.L., Mexico",
        "México 40 104, Miravalle, 64660 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("ladiana_entrada", "Dr. José Eleuterio González (Gonzalitos) 10, Leones, 64600 Monterrey, N.L., Mexico",
        "Av. Ricardo Margain Zozaya 315, Zona Santa Engracia, 66267 San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("ladiana_salida", "Av. Ricardo Margain Zozaya 400, Santa Engracia, 66267 San Pedro Garza García, N.L., Mexico",
        "Dr. José Eleuterio González (Gonzalitos) 10, Leones, 64600 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("tunel_entrada", "Av. Venustiano Carranza 820, Centro, 64000 Monterrey, N.L., Mexico",
        "Av. Real San Agustin, Zona Loma Larga Oriente, San Pedro Garza García, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("tunel_salida", "Av. Real San Agustin & Eje Metropolitano 11, San Pedro Garza García, N.L., Mexico",
        "Av. Venustiano Carranza 817, Centro, 64000 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("lazaro_entrada", "Estatua Lázaro Cárdenas, México 85, Las Torres, Monterrey, N.L., Mexico",
        "Av Lázaro Cárdenas 2506, Zona San Agustín, 66278 Monterrey, N.L., Mexico")''')

cursor.execute(''' INSERT INTO routes VALUES
        ("lazaro_salida", "Av Lázaro Cárdenas 329-S, Haciendas de La Sierra, San Pedro Garza García, N.L., Mexico",
        "México 85, Mederos Uanl, 64980 Monterrey, N.L., Mexico")''')

conn.commit()

# Create the "traffic" table.

cursor.execute('''CREATE TABLE traffic
        (traffic_id integer PRIMARY KEY, route_name text, date_time text, distance integer, duration_traffic integer,
        avg_delay integer, FOREIGN KEY (route_name) REFERENCES routes (route_name)) ''')

conn.close()




















