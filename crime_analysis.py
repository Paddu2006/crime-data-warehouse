# Crime Data Warehouse — India
# By Padma Shree
# Project 6 of 25

import pandas as pd
import matplotlib.pyplot as plt

# Step 1 - Load data
print("=== CRIME DATA WAREHOUSE — INDIA ===")
df = pd.read_csv(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\05_resources\datasets\crime_india.csv")

print("Total records:", len(df))
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Step 2 - Clean data
print("\n=== CLEANING DATA ===")
df_clean = df.dropna(subset=['TOTAL IPC CRIMES'])
print("Rows after cleaning:", len(df_clean))

# Step 3 - Most crime-prone states
print("\n=== TOP 10 STATES BY TOTAL CRIMES ===")
state_crime = df_clean.groupby('STATE/UT')['TOTAL IPC CRIMES'].sum().sort_values(ascending=False)
print(state_crime.head(10))

# Step 4 - Most dangerous crime types
print("\n=== TOP CRIME TYPES (INDIA TOTAL) ===")
crime_columns = ['MURDER', 'RAPE', 'KIDNAPPING & ABDUCTION', 'ROBBERY', 'THEFT', 'DOWRY DEATHS']
crime_totals = df_clean[crime_columns].sum().sort_values(ascending=False)
print(crime_totals)

# Step 5 - Chart 1: Top states
plt.figure(figsize=(12,6))
state_crime.head(10).plot(kind='bar', color='red')
plt.title('Top 10 States with Highest Total Crimes (2001-2012)')
plt.xlabel('State')
plt.ylabel('Total Crimes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\02_phase2\crime_warehouse\top_states.png")
plt.show()
print("\nChart 1 saved!")

# Step 6 - Chart 2: Crime types
plt.figure(figsize=(10,6))
crime_totals.plot(kind='bar', color='orange')
plt.title('Most Common Crime Types in India (2001-2012)')
plt.xlabel('Crime Type')
plt.ylabel('Total Incidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r"C:\Users\Padma shree jena\Desktop\PadduDS_Journey\02_phase2\crime_warehouse\crime_types.png")
plt.show()
print("Chart 2 saved!")

print("\n✅ PROJECT 6 COMPLETE!")