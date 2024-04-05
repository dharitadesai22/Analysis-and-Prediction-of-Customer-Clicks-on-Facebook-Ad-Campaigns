from IPython.display import display
import pandas as pd
import numpy as np 
import seaborn as sns 

def data(file, if_excel=True, debug_output=False):
    if if_excel==True:
        data = pd.read_excel(file)
    else:
        data = pd.read_csv(file)
    print(f"Shape of the dataset is {data.shape}")
    
    if debug_output==True:
        display(data[['Impressions','Clicks','Spent','Total_Conversion','Approved_Conversion']].describe())
        print("-"*90)
        print("Count of each target class category - Clicks")
        display(data['Clicks'].value_counts())
        print("Count of each target class category - Total Conversion")
        display(data['Total_Conversion'].value_counts())
        print("Count of each target class category - Approved_Conversion")
        display(data['Approved_Conversion'].value_counts())
        print("-"*90)
        print("Number of Unique Ads :", data['ad_id'].nunique())
        print("Number of Campaigns :", data['xyz_campaign_id'].nunique())
#         print("Number of Facebook Campaigns :", data['fb_campaign_id'].nunique())
        print("Number of Interest Groups :", data['interest'].nunique())
        print("Number of Age Groups :", data['age'].nunique())
        print("-"*90)
        
    return data

def preprocessing(data):
    data = data.drop(['ad_id', 'fb_campaign_id'], axis = 1)
    data['gender'].replace(['M','F'],[0,1],inplace=True)
    data['age'].replace(['30-34', '35-39', '40-44', '45-49'],[30,35,40,45], inplace=True)
    
    return data
    
def preprocessAfterFeatureEngg(data, debug_output=False):
    # Lets remove all the records where we have any Nan, value or Infinity Value
    data = data.replace([np.inf, -np.inf], np.nan).dropna(axis=0)
    
    if (debug_output==True):
        print("Shape of the Data After Removing Nans and Infs :", data.shape)
        
    return data