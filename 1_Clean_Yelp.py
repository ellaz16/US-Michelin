# Using SQL + Pandas
import pandas as pd
import numpy as np
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


# Remove "star rating" in the rating column
DC_Yelp['rating'] = DC_Yelp.rating.str.rstrip(' star rating')

# Convert rating to float
DC_Yelp['rating'] =  DC_Yelp['rating'].astype(float)

DC_Yelp


# Convert review_count to int
DC_Yelp['review_count'] =  DC_Yelp['review_count'].astype(int)


# Split price_category into two columns
DC_Yelp[['price_range','category']] = DC_Yelp.price_category.str.rsplit("$",1,expand=True)
DC_Yelp = DC_Yelp.drop('price_category',axis=1)

DC_Yelp


# Save the indices of NaN in category
swap = DC_Yelp.index[DC_Yelp['category'].isna()]

# Fill NaN in category with price_range
DC_Yelp['category'] = DC_Yelp['category'].fillna(DC_Yelp['price_range'])

# Add back one $ to price_range
DC_Yelp['price_range'] = DC_Yelp['price_range']+'$'

# Replace missing values with NaN
DC_Yelp['price_range'].loc[swap] = np.nan


DC_Yelp

# Convert category into list of strings
DC_Yelp['category'] = DC_Yelp.category.str.split(", ",expand=False)




# Build a function to clean Yelp data
def Yelp_clean(df):
    """
    This is a function that takes Yelp data as an input and output a cleaned version.

    Args:
        df (DataFrame): raw Yelp dataframe.

    Returns:
        DataFrame: cleaned Yelp dataframe.
    """
    # Get the repeated ad business
    ad = df.business_name[0]

    # Remove the repeated ad business
    df = df[df.business_name != ad].reset_index(drop=True)


    # Split business_name into two columns
    df[['index','business_name']] = df.business_name.str.split(".\xa0",expand=True)

    # Convert index to int
    df['index'] = df['index'].astype(int)

    # Sort values along index
    df = df.sort_values('index').drop('index',axis=1).reset_index(drop=True)


    # Remove "star rating" in the rating column
    df['rating'] = df.rating.str.rstrip(' star rating')

    # Convert rating to float
    df['rating'] =  df['rating'].astype(float)


    # Convert review_count to int
    df['review_count'] =  df['review_count'].astype(int)


    # Split price_category into two columns
    df[['price_range','category']] = df.price_category.str.rsplit("$",1,expand=True)
    df = df.drop('price_category',axis=1)

    # Save the indices of NaN in category
    swap = df.index[df['category'].isna()]

    # Fill NaN in category with price_range
    df['category'] = df['category'].fillna(df['price_range'])

    # Add back one $ to price_range
    df['price_range'] = df['price_range']+'$'

    # Replace missing values with NaN
    df['price_range'].loc[swap] = np.nan


    # Convert category into list of strings
    df['category'] = df.category.str.split(", ",expand=False)


    # Return data
    return df


# Clean SF_Yelp and export
# Yelp_clean(SF_Yelp).to_csv('Data/Yelp/SF_Yelp_cleaned.csv',index=False)








# -------------
