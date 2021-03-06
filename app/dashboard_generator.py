import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
import math
import re
from datetime import datetime


def to_usd(my_price):
    return f"${my_price:,.2f}"

data_location = os.path.join(os.path.dirname(__file__), "..", "data")

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(data_location) if isfile(join(data_location, f))]
#abovesource: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

#print(onlyfiles)

while True:
    file_name = input("Input name of file for which you are seeking data: ")
    if [p for p in onlyfiles if p == file_name]:
        break
    else:
        print("Data is unavailable; you may try again using a different input.")

parts = re.split('-|\.',file_name)
str_date = parts[1]
#source: https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/

report_date = datetime.strptime(str_date, "%Y%m")
formatted_date = report_date.strftime("%B %Y")
#print(formatted_date)
#source for above: https://stackoverflow.com/questions/55978255/extract-the-file-name-yyyymmdd-csv-and-display-the-string-yyyy-mm-dd

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


print("-----------------------")
print("MONTH: " + str(formatted_date))

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
    ax.text(v + 3, i + .25, str(to_usd((v))), color='blue')
#https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
ax.invert_yaxis()
plt.title('Top-Selling Products ' + '(' + str(formatted_date) + ')')
formatter = ticker.FormatStrFormatter('$%1.2f')
ax.xaxis.set_major_formatter(formatter)
#Source of above code: https://matplotlib.org/3.1.1/gallery/pyplots/dollar_ticks.html
plt.show()

# Generate a Pie Chart for data
fig, ax1 = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

data = [y["monthly_sales"] for y in top_sellers]
products = [x["name"] for x in top_sellers]

def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct)

wedges, texts, autotexts = ax1.pie(data, autopct=lambda pct: func(pct, data), textprops=dict(color="w"))

ax1.legend(wedges, products, title="Products", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax1.set_title('Top-Selling Products by % Total Monthly Sales ' + '(' + str(formatted_date) + ')')

plt.show()

#above code source: https://matplotlib.org/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=pie%20chart%20legend

# labels = [x["name"] for x in top_sellers]
# values = [(y["monthly_sales"])/monthly_total for y in top_sellers]
# fig1, ax1 = plt.subplots()
# plt.legend(title="Products", loc="center left")
# plt.title('Top-Selling Products by % ' + '(' + str(formatted_date) + ')')
# ax1.pie(values, autopct='%1.0f%%', startangle=90)
# ax1.axis('equal')
# plt.show()
