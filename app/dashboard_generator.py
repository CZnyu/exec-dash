import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from datetime import datetime


def to_usd(my_price):
    return f"${my_price:,.2f}"


print(os.path.dirname(__file__))

while True:
    file_name = input("Input name of file for which you are seeking data: ")
    
    if file_name == "sales-201710.csv":
        print("-----------------------")
        print("MONTH: October 2017")
        break
    elif file_name == "sales-201711.csv":
        print("-----------------------")
        print("MONTH: November 2017")
        break
    elif file_name == "sales-201712.csv":
        print("-----------------------")
        print("MONTH: December 2017")
        break
    elif file_name == "sales-201801.csv":
        print("-----------------------")
        print("MONTH: January 2018")
        break
    elif file_name == "sales-201802.csv":
        print("-----------------------")
        print("MONTH: February 2018")
        break
    elif file_name == "sales-201803.csv":
        print("-----------------------")
        print("MONTH: March 2018")
        break
    elif file_name == "sales-201804.csv":
        print("-----------------------")
        print("MONTH: April 2018")
        break
    elif file_name == "sales-201805.csv":
        print("-----------------------")
        print("MONTH: May 2018")
        break    
    elif file_name == "sales-201806.csv":
        print("-----------------------")
        print("MONTH: June 2018")
        break
    elif file_name == "sales-201807.csv":
        print("-----------------------")
        print("MONTH: July 2018")
        break    
    elif file_name == "sales-201808.csv":
        print("-----------------------")
        print("MONTH: August 2018")
        break
    elif file_name == "sales-201809.csv":
        print("-----------------------")
        print("MONTH: September 2018")
        break
    elif file_name == "sales-201810.csv":
        print("-----------------------")
        print("MONTH: October 2018")
        break
    elif file_name == "sales-201811.csv":
        print("-----------------------")
        print("MONTH: November 2018")
        break
    elif file_name == "sales-201812.csv":
        print("-----------------------")
        print("MONTH: December 2018")
        break
    elif file_name == "sales-201901.csv":
        print("-----------------------")
        print("MONTH: January 2019")
        break
    elif file_name == "sales-201902.csv":
        print("-----------------------")
        print("MONTH: February 2019")
        break
    elif file_name == "sales-201903.csv":
        print("-----------------------")
        print("MONTH: March 2019")
        break
    elif file_name == "sales-201904.csv":
        print("-----------------------")
        print("MONTH: April 2019")
        break
    else:
        print("Data is unavailable for that month. Please try a different input.")

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", str(file_name))

csv_filename = file_name
csv_data = pd.read_csv(csv_filepath)

monthly_total = csv_data["sales price"].sum()

print(monthly_total)


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

# print("-----------------------")
# print("CRUNCHING THE DATA...")

# print("-----------------------")
# print("TOTAL MONTHLY SALES: $12,000.71")

# print("-----------------------")
# print("TOP SELLING PRODUCTS:")
# print("  1) Button-Down Shirt: $6,960.35")
# print("  2) Super Soft Hoodie: $1,875.00")
# print("  3) etc.")

# print("-----------------------")
# print("VISUALIZING THE DATA...")