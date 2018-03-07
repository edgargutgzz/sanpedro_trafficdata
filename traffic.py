import config
import pandas as pd
import numpy as np 
import sqlite3
import googlemaps
from datetime import datetime

# Connect to data base.

conn = sqlite3.connect('traffic_data.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# Call Google's API.

gmaps = googlemaps.Client(key = config.api_key)
now = datetime.now()


# Insert traffic data.

# Calzada Entrada

response = gmaps.distance_matrix(('25.673569, -100.367882'),('25.662387, -100.368835'),
                                 departure_time = now)

route_name = 'calzada_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# Calzada Salida

response = gmaps.distance_matrix(('25.662583, -100.368320'),('25.674073, -100.367404'),
                                 departure_time = now)

route_name = 'calzada_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# La Diana - Entrada

response = gmaps.distance_matrix(('25.694560, -100.351416'),('25.652983, -100.352807'),
                                 departure_time = now)

route_name = 'ladiana_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# La Diana - Salida

response = gmaps.distance_matrix(('25.653755, -100.352757'),('25.694564, -100.351219'),
                                 departure_time = now)

route_name = 'ladiana_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# Tunel - Entrada

response = gmaps.distance_matrix(('25.684975, -100.330676'),('25.655845, -100.337746'),
                                 departure_time = now)

route_name = 'tunel_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# Tunel - Salida

response = gmaps.distance_matrix(('25.655696, -100.337337'),('25.684963, -100.330551'),
                                 departure_time = now)

route_name = 'tunel_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# Lazaro - Entrada

response = gmaps.distance_matrix(('25.614267, -100.274253'),('25.650744, -100.332098'),
                                 departure_time = now)

route_name = 'lazaro_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, avg_delay))

# Lazaro - Salida

response = gmaps.distance_matrix(('25.645605, -100.324049'),('25.613813, -100.273075'),
                                 departure_time = now)

route_name = 'lazaro_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = response['rows'][0]['elements'][0]['distance']['value']
duration_traffic = response['rows'][0]['elements'][0]['duration_in_traffic']['value']
avg_delay = float(np.round((duration_traffic/60)/(distance/1000), decimals = 2))

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                avg_delay) VALUES(?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                   duration_traffic, avg_delay))

conn.commit()
conn.close()