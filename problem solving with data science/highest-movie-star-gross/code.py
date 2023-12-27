import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to get CPI data for a specific year from the cpi data file
# Received help from ChatGPT to make this function work
# OpenAI. (2023). ChatGPT [Large language model]. https://chat.openai.com
# CPI data retreived from https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/
# Please download the CPI data file from https://drive.google.com/drive/folders/12-acYLRPxx8-1QP9x5_WAgeiRg-Yq8XX?usp=drive_link

cpi_data = pd.read_excel('CPI.xlsx')

def get_cpi_data(year, cpi_data):
    try:
        # Search for the CPI value for the specified year in the DataFrame
        cpi = cpi_data.loc[cpi_data['Year'] == year, 'Avg'].values
        if len(cpi) > 0:
            return cpi[0]
        else:
            return np.nan 
    except (IndexError, KeyError):
        return np.nan



imdb_data = pd.read_csv('imdb5000.csv')

# creating a new column for adjusted revenues
imdb_data['Adjusted_Revenue'] = np.nan

# iterating through each movie to calculate adjusted revenue
for index, row in imdb_data.iterrows():
    release_year = row['title_year']
    cpi = get_cpi_data(release_year, cpi_data)
    
    if not np.isnan(cpi):
        revenue = row['gross']
        adjusted_revenue = revenue / cpi
        imdb_data.at[index, 'Adjusted_Revenue'] = adjusted_revenue


star_data = imdb_data.groupby('actor_1_name')['Adjusted_Revenue'].sum().reset_index()

# sorting stars by total adjusted revenue
ranked_stars = star_data.sort_values(by='Adjusted_Revenue', ascending=False)


topTen = 10  
top_stars = ranked_stars.head(topTen)
print(f"Top {topTen} Stars by their Approximate Adjusted Movie Revenues:")
for index, row in top_stars.iterrows():
    refinedRevenue = '{:,.2f}'.format(row['Adjusted_Revenue'])
    print(f"{row['actor_1_name']}: ${refinedRevenue}")

# visualizing the results
plt.figure(figsize=(10, 6))
plt.barh(top_stars['actor_1_name'], top_stars['Adjusted_Revenue'])
plt.xlabel('Total Adjusted Revenue')
plt.ylabel('Stars')
plt.title(f'Top {topTen} Stars by Adjusted Movie Revenues')
plt.gca().invert_yaxis() 
plt.show()
