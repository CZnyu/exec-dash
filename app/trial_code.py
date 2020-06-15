import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import re
from datetime import datetime

data_location = os.path.join(os.path.dirname(__file__), "..", "data")

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(data_location) if isfile(join(data_location, f))]
#abovesource: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

#print(onlyfiles)

while True:
    file_name = input("Input name of file for which you are seeking data: ")
    if [p for p in onlyfiles if p == file_name]:
        print("YAY!")
        break
    else:
        print("Data is unavailable; you may try again using a different input.")

parts = re.split('-|\.',file_name)
str_date = parts[1]
#source: https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/



# def to_usd(my_price):
#     return f"${my_price:,.2f}"


# while True:
#     file_name = input("Input name of file for which you are seeking data: ")
    
#     if file_name == "sales-201710.csv":
#         print("-----------------------")
#         print("MONTH: October 2017")
#         break
#     elif file_name == "sales-201711.csv":
#         print("-----------------------")
#         print("MONTH: November 2017")
#         break
#     elif file_name == "sales-201712.csv":
#         print("-----------------------")
#         print("MONTH: December 2017")
#         break
#     elif file_name == "sales-201801.csv":
#         print("-----------------------")
#         print("MONTH: January 2018")
#         break
#     elif file_name == "sales-201802.csv":
#         print("-----------------------")
#         print("MONTH: February 2018")
#         break
#     elif file_name == "sales-201803.csv":
#         print("-----------------------")
#         print("MONTH: March 2018")
#         break
#     elif file_name == "sales-201804.csv":
#         print("-----------------------")
#         print("MONTH: April 2018")
#         break
#     elif file_name == "sales-201805.csv":
#         print("-----------------------")
#         print("MONTH: May 2018")
#         break    
#     elif file_name == "sales-201806.csv":
#         print("-----------------------")
#         print("MONTH: June 2018")
#         break
#     elif file_name == "sales-201807.csv":
#         print("-----------------------")
#         print("MONTH: July 2018")
#         break    
#     elif file_name == "sales-201808.csv":
#         print("-----------------------")
#         print("MONTH: August 2018")
#         break
#     elif file_name == "sales-201809.csv":
#         print("-----------------------")
#         print("MONTH: September 2018")
#         break
#     elif file_name == "sales-201810.csv":
#         print("-----------------------")
#         print("MONTH: October 2018")
#         break
#     elif file_name == "sales-201811.csv":
#         print("-----------------------")
#         print("MONTH: November 2018")
#         break
#     elif file_name == "sales-201812.csv":
#         print("-----------------------")
#         print("MONTH: December 2018")
#         break
#     elif file_name == "sales-201901.csv":
#         print("-----------------------")
#         print("MONTH: January 2019")
#         break
#     elif file_name == "sales-201902.csv":
#         print("-----------------------")
#         print("MONTH: February 2019")
#         break
#     elif file_name == "sales-201903.csv":
#         print("-----------------------")
#         print("MONTH: March 2019")
#         break
#     elif file_name == "sales-201904.csv":
#         print("-----------------------")
#         print("MONTH: April 2019")
#         break
#     else:
#         print("Data is unavailable for that month. Please try a different input.")

# #locating the proper file path

# csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", str(file_name))

# csv_filename = file_name
# csv_data = pd.read_csv(csv_filepath)

# # CALCULATIONS
# monthly_total = csv_data["sales price"].sum()

# #print(monthly_total)

# product_totals = csv_data.groupby("product").sum()

# product_totals = product_totals.sort_values("sales price", ascending=False)

# top_sellers = []
# rank = 1
# for i, row in product_totals.iterrows():
#     d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
#     top_sellers.append(d)
#     rank = rank + 1

# print(top_sellers)