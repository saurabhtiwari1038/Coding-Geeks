from datetime import *
import csv
gst_rates=[]
#more lib
Cart=[]
Product_=""
while Product_!="":
    Product_=input("enter article")
    Cart.append(article_)
def records_init():
    product_type=[]
    gst_rate=[]
    with open('xyz.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             product_type.append(row['Products_type'])
             print(row['Products_type'])
             gst_rate.append(row['Tax_Rates'])
             print(row['Tax_Rates'])
def commodity_cost():
    records_()
#cost of single article
def tax():
    #tax of commodity corresponding to per unit of article
    return 0
def total_cost():
    return 0
    #net cost without tax
def tax_ammount():
    return 0
def invoice():
    return 0
records_init()

