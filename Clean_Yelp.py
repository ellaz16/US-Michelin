# Using SQL + Pandas
import pandas as pd
import sqlite3

# Data Visualization
from plotnine import *
import seaborn as sns
import matplotlib.pyplot as plt

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')


# Read in the data
DC_Yelp = pd.read_csv("Data/Yelp/DC_Yelp.csv")
Chicago_Yelp = pd.read_csv("Data/Yelp/Chicago_Yelp.csv")
NY_Yelp = pd.read_csv("Data/Yelp/NY_Yelp.csv")
SF_Yelp = pd.read_csv("Data/Yelp/SF_Yelp.csv")
LA_Yelp = pd.read_csv("Data/Yelp/LA_Yelp.csv")


# View the head of the data
DC_Yelp.head()


# Print the shape of the data
DC_Yelp.shape


# Get the repeated ad business
ad = DC_Yelp.business_name[0]

# Remove the repeated ad business
DC_Yelp = DC_Yelp[DC_Yelp.business_name != ad].reset_index(drop=True)

DC_Yelp


# Split business_name into two columns
DC_Yelp[['index','business_name']] = DC_Yelp.business_name.str.split(".\xa0",expand=True)

# Convert index to int
DC_Yelp['index'] = DC_Yelp['index'].astype(int)

# Sort values along index
DC_Yelp = DC_Yelp.sort_values('index').drop('index',axis=1).reset_index(drop=True)

DC_Yelp


















# -------------
