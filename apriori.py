import csv

with open('market_basket_data_set.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
