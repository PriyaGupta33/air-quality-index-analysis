# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 10:19:23 2025

@author: HP
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data= pd.read_csv('air_quality.csv')
data.head()
#basic inspection
data.info()
data.describe()

data.isnull().sum()
data.columns
# Replace NA with NaN and convert to numeric
data[['pollutant_min', 'pollutant_max', 'pollutant_avg']] = data[['pollutant_min', 'pollutant_max', 'pollutant_avg']].replace('NA', pd.NA)
for col in ['pollutant_min', 'pollutant_max', 'pollutant_avg']:
    data[col] = pd.to_numeric(data[col], errors='coerce')

#drop rows with all  three pollutant values as NaN
data = data.dropna(subset=['pollutant_min', 'pollutant_max', 'pollutant_avg'], how='all')

#Check duplicates
duplicates= data.duplicated(subset=['station','pollutant_id','last_update'])
print(f"Number of duplicates: {duplicates.sum()}")

#Outlier check using z_score
pm25_avrage =data[data['pollutant_id']=='PM2.5']['pollutant_avg']
mean, std = pm25_avrage.mean() , pm25_avrage.std()
outliers= pm25_avrage[(pm25_avrage > mean + 3*std) | (pm25_avrage <mean - 3*std)]
print(f"Potential PM2.5 outliers: {outliers}")

#checking for invalid geographic data
#geospatial validation
validlatitute =data['latitude'].between(8,37)  #India's latitude range
validlong= data['longitude'].between(68,97) # India's longitude range
print(f"Invalid coordinates: {((~validlatitute) | (~validlong)).sum()}")

#save the cleaned data to a new csv file
data.to_csv('air_quality_cleanedcleaned.csv', index=False)
print("Cleaned data is  saved!")


data = pd.read_csv('air_quality_cleanedcleaned.csv')
print("Data loaded successfully!")
data.head()



# Import necessary libraries



#objective 1  Pollutant Avg Across Top 5 Cities (Line Plot)
#Shows how average pollution levels vary across the five most monitored cities. Helps compare which city has higher or lower pollution for different pollutants.
plt.figure(figsize=(10, 6))
top_cities = data['city'].value_counts().head(5).index
city_data = data[data['city'].isin(top_cities)]
for pollutant in data['pollutant_id'].unique():
    subset = city_data[city_data['pollutant_id'] == pollutant]
    plt.plot(subset.groupby('city')['pollutant_avg'].mean(), label=pollutant)
plt.title('Average Pollutant Levels in Top 5 Cities')
plt.xlabel('City')
plt.ylabel('Average Concentration')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




#objective 2 Pollutant Distribution by Type (Box Plot)
#Visualizes the spread and variability of pollutant averages. Highlights which pollutants have more extreme or inconsistent values.


plt.figure(figsize=(12, 6))
sns.boxplot(x='pollutant_id', y='pollutant_avg', data=data, palette='Set3')
plt.title('Distribution of Pollutant Concentrations')
plt.xlabel('Pollutant Type')
plt.ylabel('Average Concentration')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# PM2.5 vs PM10 Relationship (Scatter Plot)
#Analyzes how PM2.5 and PM10 values are related. Helps detect patterns, correlations, or unusual data points in particulate matter levels.

plt.figure(figsize=(8, 6))
pm_data = data[data['pollutant_id'].isin(['PM2.5', 'PM10'])].pivot_table(
    values='pollutant_avg', index='station', columns='pollutant_id', aggfunc='mean'
).dropna()
plt.scatter(pm_data['PM2.5'], pm_data['PM10'], color='green', alpha=0.5)
plt.title('PM2.5 vs PM10 Average Concentrations')
plt.xlabel('PM2.5 Avg Concentration')
plt.ylabel('PM10 Avg Concentration')
plt.tight_layout()
plt.show()


# Correlation Between Pollutants (Heatmap)
#Displays how strongly different pollutants are related. Useful for understanding which pollutants rise or fall together.
plt.figure(figsize=(8, 6))
pivot_data = data.pivot_table(values='pollutant_avg', index='station', columns='pollutant_id')
corr_matrix = pivot_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Between Pollutants')
plt.tight_layout()
plt.show()


#Pollutant Proportion in Dataset (Pie Chart)
#Shows the share of each pollutant in the dataset. Helps identify which pollutants are monitored more frequently.
plt.figure(figsize=(8, 8))
pollutant_counts = data['pollutant_id'].value_counts()
plt.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Pollutant Measurements')
plt.tight_layout()
plt.show()

#Pollutant Outliers (Bar Plot)
#Counts how many extreme (above 95th percentile) values each pollutant has. Highlights which pollutants have frequent spikes.
plt.figure(figsize=(10, 6))
outliers = data[data['pollutant_avg'] > data['pollutant_avg'].quantile(0.95)]
outlier_counts = outliers['pollutant_id'].value_counts()
outlier_counts.plot(kind='bar', color='red')
plt.title('Pollutants with Outlier Concentrations (Top 5%)')
plt.xlabel('Pollutant Type')
plt.ylabel('Number of Outliers')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 10 States by Max Pollutant Levels (Bar Plot)
#Ranks states based on highest average pollution peaks. Identifies regions facing the most severe pollution levels.


plt.figure(figsize=(12, 6))
state_max = data.groupby('state')['pollutant_max'].mean().sort_values(ascending=False).head(10)
sns.barplot(x=state_max.index, y=state_max.values, palette='Blues_d')
plt.title('Top 10 States by Maximum Pollutant Levels')
plt.xlabel('State')
plt.ylabel('Max Concentration')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


print("All 10 charts have been generated successfully!")

