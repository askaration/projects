import pandas as pd

################################################################################################
## Please visit the following link to download the data files
## https://drive.google.com/drive/folders/1RCNCUsFtoZYfmO4t3pBjkNdgC_8DynKr?usp=drive_link
################################################################################################


bartTenth = pd.read_excel('BARTtenth.xlsx', header=0)

average_rides_by_hour = bartTenth.groupby('Hour')['Count'].mean()

hour_with_highest_average = average_rides_by_hour.idxmax()

highest_average = average_rides_by_hour.max()

print("The busiest hour in the Bay area is", hour_with_highest_average, "with average", highest_average.round(), ", according to the Bart Tenth File.")

###############################################################################################################################
bartHundredth = pd.read_excel('BARThundredth.xlsx', header=0)

average_counts_by_hour = bartHundredth.groupby('Hour')['Count'].mean()

hour_with_highest_count = average_counts_by_hour.idxmax()

highest_count_average = average_counts_by_hour.max()

print("The busiest hour in the Bay area is", hour_with_highest_count, "with average", highest_count_average.round(), ", according to the Bart Hundredth File.")