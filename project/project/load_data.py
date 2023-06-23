import csv
from app.models import Dish

def load_data():
    with open('restaurants_small.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = row[0]
            Dish.objects.create(name=name)

if __name__ == '__main__':
    load_data()
