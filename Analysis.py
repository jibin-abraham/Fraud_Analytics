# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:36:06 2020

@author: Jibin Jiju Abraham
"""


## Variable description
# step : maps unit of time. Here, one step is one hour
# type : type of transaction
# amount : amount of transaction
# nameOrig : customer who started the transaction
# oldbalanceOrg : initial balance before the transaction
# newbalanceOrg : new balance after the transaction
# nameDest : customer who is recipient of the transaction
# oldbalanceDest : initial balance of recipient before transaction
# newbalanceDest : new balance of recipient after transaction
# isFraud : Fraudelent transaction
# isFlaggedFraud : An illegal attempt where more than 200000 are transfered in one transaction

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("D:\\Hackathon\\Kaggle\\Financial Fraud\\Data.csv")

# Descriptive statistics of the data
data.head()
data.info()
data.describe()

# Finding unique payment types
data["type"].unique()

# Finding null values
data.isnull().sum()

# Plotting the columns
plt.plot(data["amount"])

# Changing transaction type to numeric
labelencoder=LabelEncoder()
data["type"]=labelencoder.fit_transform(data["type"])
data.head()

## As per the above encoding, the payment types are encoded as:
# Payment : 3
# Transfer : 4
# Cash_out : 1
# Debit : 2
# Cash_in : 0


# Plotting the fraud transactions detected as per payment types
pay=data[(data.type==3)& (data.isFraud==1)]
plt.plot(pay)
transfer=data[(data.type==4)& (data.isFraud==1)]
cashout=data[(data.type==1)& (data.isFraud==1)]
debit=data[(data.type==2)& (data.isFraud==1)]
cashin=data[(data.type==0)& (data.isFraud==1)]
fraud_types=[len(pay),len(transfer),len(cashout),len(debit),len(cashin)]


