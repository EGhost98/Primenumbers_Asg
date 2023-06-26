import pandas as pd
import sqlite3


df = pd.read_csv('restaurants_small.csv')

conn = sqlite3.connect('your_database.db')

conn.execute('DROP TABLE IF EXISTS items')
conn.execute('DROP TABLE IF EXISTS restaurants')

conn.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        latitude FLOAT,
        longitude FLOAT
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        restaurant_id INTEGER,
        name TEXT,
        price TEXT,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
    )
''')


for index, row in df.iterrows():
    items = eval(row['items'])
    lat, long = map(float, row['lat_long'].split(','))
    # print(lat,long)
    restaurant_data = (row['id'], row['name'], row['location'], lat, long)
    conn.execute('INSERT INTO restaurants (id, name, location, latitude, longitude) VALUES (?, ?, ?, ?, ?)', restaurant_data)

    restaurant_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]

    for item_name, item_price in items.items():
        item_data = (restaurant_id, item_name, item_price)
        conn.execute('INSERT INTO items (restaurant_id, name, price) VALUES (?, ?, ?)', item_data)

conn.commit()
conn.close()
