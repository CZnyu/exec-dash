import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from datetime import datetime


def to_usd(my_price):
    return f"${my_price:,.2f}"


print(os.path.dirname(__file__))

#csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "sales-201710.csv")

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

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")