import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
import math
from datetime import datetime


def to_usd(my_price):
    return f"${my_price:,.2f}"

data_location = os.path.join(os.path.dirname(__file__), "..", "data")

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(data_location) if isfile(join(data_location, f))]

#print(onlyfiles)

while True:
    file_name = input("Input name of file for which you are seeking data: ")
    if [p for p in onlyfiles if p == file_name]
        break
    else:
        print("Data is unavailable; you may try again using a different input.")

#locating the proper file path

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", str(file_name))

csv_filename = file_name
csv_data = pd.read_csv(csv_filepath)

# CALCULATIONS
monthly_total = csv_data["sales price"].sum()

#print(monthly_total)

product_totals = csv_data.groupby("product").sum()

product_totals = product_totals.sort_values("sales price", ascending=False)

top_sellers = []
rank = 1
for i, row in product_totals.iterrows():
    d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
    top_sellers.append(d)
    rank = rank + 1

# df = pd.read_csv(csv_filepath)
# print(type(df))
# print(df.head())

#products = df.to_dict("records")

#  sales_files = []
#  for root, dirs, files in os.walk(r"(__file__), "..", "data")":
#       for file in files:
#           if file.endswith('.csv'):
#               sales_files.append(file)

#print(sales_files)

# print("-----------------------")
# print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(monthly_total)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
for d in top_sellers:
    print("  " + str(d["rank"]) + ") " + d["name"] +
          ": " + to_usd(d["monthly_sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")
#Generate Bar Chart for data
fig, ax = plt.subplots()
#Source: https://pythonspot.com/matplotlib-bar-chart/
best = [x["name"] for x in top_sellers]
y_pos = (np.arange(len(best)))
actuals = [y["monthly_sales"] for y in top_sellers]
plt.barh(y_pos, actuals, align='center')
plt.yticks(y_pos, best)
plt.xlabel('Sales (USD)')
#add value above bar graphs
for i, v in enumerate(actuals):
    ax.text(v + 3, i + .25, str(to_usd((v))), color='blue', fontweight='bold')
#https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
ax.invert_yaxis()
plt.title('Top-Selling Products')
formatter = ticker.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)
#Source of above code: https://matplotlib.org/3.1.1/gallery/pyplots/dollar_ticks.html
plt.show()

