import pandas as pd

#############################################################################################
## Please visit the folowing link to download the data file
## https://drive.google.com/drive/folders/1KVszgwh7p3S7_azFJq8APwxyOKsZwD54?usp=drive_link
#############################################################################################


data = pd.read_excel('chicago_daily_ridership.xlsx', header=0)

## A) ##########################################################################

average_rides_by_station = data.groupby('stationname')['rides'].mean()

station_with_highest_average = average_rides_by_station.idxmax()

highest_average = average_rides_by_station.max()
################################################################################

## B) ##########################################################################
total_rides_perDate = data.groupby('date')['rides'].sum().reset_index()

date_with_most_rides = total_rides_perDate.loc[total_rides_perDate['rides'].idxmax(), 'date']

most_rides = total_rides_perDate['rides'].max()
################################################################################

## C) I am unsure if the professor is asking about the least busy weekday every week or least busy in the entire dataset
#     so I will do both ########################################################
data['weekday'] = data['date'].dt.strftime('%A')

average_rides_by_weekday = data.groupby('weekday')['rides'].mean()

least_busy_weekday = average_rides_by_weekday.idxmin()
lowest_average = average_rides_by_weekday.min()

###############################################################################
## C)Part two

date_with_least_rides = total_rides_perDate.loc[total_rides_perDate['rides'].idxmin(), 'date']

least_rides = total_rides_perDate['rides'].min()
################################################################################
print("A) The busiest station in Chicago is", station_with_highest_average, "with average", highest_average.round(), "rides over the span of 20 years.")
print("B) The day with the most rides is", date_with_most_rides, "with", most_rides, "due to Chicago Cubs fans celebrating the team's World Series win.")
print("C) The least busy weekday on is", least_busy_weekday, "with an average of", lowest_average.round(), "weekly.")
print("C_2) The day with the least rides is", date_with_least_rides, "with", least_rides, "due to the BLM demonstration to condemn the murder of George Floyd.")

