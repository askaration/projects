import pandas as pd
import matplotlib.pyplot as plt


# Downloaded and cleaned the data in an excel workbook
data = pd.read_excel("Harvest_refined.xlsx", engine="openpyxl")

years = data["Year"]
burgundy_harvest = data["Burgundy"]

smooting_window_size = 20

refined_harvest = burgundy_harvest.rolling(window=smooting_window_size).mean()


plt.figure(figsize=(14,7))
plt.plot(years, refined_harvest, color='#800020')
plt.title(f"Average Grape Harvest in Burgundy over Centuries")
plt.xlabel("Year")
plt.ylabel("Harvest")
plt.grid(True)
plt.legend()
plt.show()
