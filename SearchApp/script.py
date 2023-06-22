import csv
from core.models import Restaurant
from decimal import Decimal
import os
import django

# Configure Django settings

django.setup()

def import_data_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            id = row[0]
            name = row[1]
            location = row[2]
            latitude = Decimal(row[4].split(',')[0])
            longitude = Decimal(row[4].split(',')[1])
            menu_items = row[3]
            full_details = row[5]
            Restaurant.objects.create(id=id, name=name, location=location, latitude=latitude, 
                                      longitude=longitude, menu_items=menu_items, full_details=full_details)

import_data_from_csv("restaurants_small.csv")