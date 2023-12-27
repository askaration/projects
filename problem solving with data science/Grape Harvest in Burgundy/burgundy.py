import pandas as pd
import matplotlib.pyplot as plt

# Downloaded and cleaned the data in an excel workbook

df = pd.read_excel("Harvest_refined.xlsx", engine="openpyxl")

years = df["Year"]
burgundy_harvest = df["Burgundy"]

window_size = 20

smoothed_harvest = burgundy_harvest.rolling(window=window_size).mean()


# Plot the data
plt.figure(figsize=(14, 6))
plt.plot(years, smoothed_harvest, color='#800020', label=f'Smoothed Data (Window Size = {window_size})')
plt.title("Average Grape Harvest Over Centuries")
plt.xlabel("Year")
plt.ylabel("Burgundy Harvest")
plt.grid(True)
plt.show()


