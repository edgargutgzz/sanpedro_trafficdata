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


# Insert traffic data.


# Atirantado desde Leones - Entrada

response = gmaps.distance_matrix(('25.704677, -100.36991499999999'),('25.665602, -100.380839'),
                                 departure_time = "now")

route_name = 'atirantado_leones_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Atirantado desde Leones - Salida

response = gmaps.distance_matrix(('25.665587, -100.380774'),('25.704632999999998, -100.369858'),
                                 departure_time = "now")

route_name = 'atirantado_leones_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Atirantado desde Periferico - Entrada

response = gmaps.distance_matrix(('25.696251, -100.38030099999999'),('25.665605, -100.380838'),
                                 departure_time = "now")

route_name = 'atirantado_periferico_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Atirantado desde Periferico - Salida

response = gmaps.distance_matrix(('25.665591, -100.380774'),('25.696168, -100.380245'),
                                 departure_time = "now")

route_name = 'atirantado_periferico_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Calzada Entrada

response = gmaps.distance_matrix(('25.673569, -100.367882'),('25.658122, -100.370288'),
                                 departure_time = "now")

route_name = 'calzada_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Calzada Salida

response = gmaps.distance_matrix(('25.658008, -100.369799'),('25.673565999999997, -100.367599'),
                                 departure_time = "now")

route_name = 'calzada_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# La Diana - Entrada

response = gmaps.distance_matrix(('25.714492, -100.35020899999999'),('25.670654, -100.353571'),
                                 departure_time = "now")

route_name = 'ladiana_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# La Diana - Salida

response = gmaps.distance_matrix(('25.670606, -100.353427'),('25.714427999999998, -100.35011'),
                                 departure_time = "now")

route_name = 'ladiana_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Tunel - Entrada

response = gmaps.distance_matrix(('25.68706, -100.330349'),('25.655851, -100.337745'),
                                 departure_time = "now")

route_name = 'tunel_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Tunel - Salida

response = gmaps.distance_matrix(('25.655701, -100.33733799999999'),('25.687103, -100.330219'),
                                 departure_time = "now")

route_name = 'tunel_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Lazaro - Entrada

response = gmaps.distance_matrix(('25.614269999999998, -100.274222'),('25.653682999999997, -100.357254'),
                                 departure_time = "now")

route_name = 'lazaro_entrada'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))


# Lazaro - Salida

response = gmaps.distance_matrix(('25.652925999999997, -100.357528'),('25.614036, -100.274339'),
                                 departure_time = "now")

route_name = 'lazaro_salida'
date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
distance = np.round((response['rows'][0]['elements'][0]['distance']['value']) / 1000, decimals = 1)
duration_traffic = np.round((response['rows'][0]['elements'][0]['duration_in_traffic']['value']) / 60,
                            decimals = 1)
velocity = np.round((distance / duration_traffic) * 60, decimals = 0)
avg_delay = np.round(duration_traffic / distance, decimals = 2)

cursor.execute('''INSERT INTO traffic(route_name, date_time, distance, duration_traffic,
                velocity, avg_delay) VALUES(?, ?, ?, ?, ?, ?)''', (route_name, date_time, distance,
                                                      duration_traffic, velocity, avg_delay))

conn.commit()
conn.close()