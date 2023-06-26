import pandas as pd
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    @classmethod
    def DB_From_CSV(cls, csv_file):
        df = pd.read_csv(csv_file)
        restaurants = []
        items = []
        
        # Clear existing data from tables
        Restaurant.objects.all().delete()
        Item.objects.all().delete()
        
        for index, row in df.iterrows():
            lat, long = map(float, row['lat_long'].split(','))
            restaurant = cls(name=row['name'], location=row['location'], latitude=lat, longitude=long)
            restaurants.append(restaurant)

            restaurant_items = eval(row['items'])
            for item_name, item_price in restaurant_items.items():
                item = Item(restaurant=restaurant, name=item_name, price=item_price)
                items.append(item)

        Restaurant.objects.bulk_create(restaurants)
        Item.objects.bulk_create(items)

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name
