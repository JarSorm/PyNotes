import pandas as pd
import pathlib
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
work_path = pathlib.Path.cwd()
data_path = Path(work_path, 'datasets', 'bikes.csv')
bikes = pd.read_csv(data_path, sep=',', encoding='latin1', parse_dates=['Date'],
                    dayfirst=True, index_col='Date')

url_template = ("http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={"
                "year}&Month={month}&timeframe=1&submit=Download+Data")


# 1
def bikes_total_plot():
    plt.rcParams['figure.figsize'] = (15, 5)
    print(bikes['Rachel1'].sum(axis=0))
    # bikes['Berri 1'].plot()
    # plt.title('Берри')
    bikes.plot(figsize=(15, 10))
    plt.title('Чертовы велосипедисты')
    plt.show()


# 3
def bikes_weekdays_plot():
    plt.rcParams['figure.figsize'] = (10, 5)
    berri_bikes = bikes[['Berri 1']].copy()
    berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday
    weekday_counts = berri_bikes.groupby('weekday').max()
    weekday_counts.index = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    weekday_counts.plot(kind='bar')
    plt.show()


# 4
def canadian_weather():
    pd.options.display.max_rows = 7
    plt.rcParams['figure.figsize'] = (15, 3)
    plt.rcParams['font.family'] = 'sans-serif'
    weather_2012_final = pd.read_csv('weather_2012.csv', index_col='Date/Time (LST)',
                                     parse_dates=['Date/Time (LST)'])
    # weather_2012_final['Temp (C)'].plot(figsize=(18, 6))
    temperatures = weather_2012_final[['Temp (C)']].copy()
    temperatures.loc[:, 'hour'] = weather_2012_final.index.hour
    temperatures.groupby('hour').aggregate(np.median).plot()
    plt.show()


# refactored basic scripts:
def download_weather_month(year, month):
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, index_col='Date/Time (LST)', parse_dates=True, encoding='latin1')
    weather_data = weather_data.dropna(axis=1, how='any')
    weather_data = weather_data.drop(['Year', 'Month', 'Day', 'Time (LST)', 'ï»¿"Longitude (x)"',
                                      'Latitude (y)', 'Station Name', 'Climate ID'], axis=1)
    weather_data.columns = [u'Temp (C)', u'Dew Point Temp (C)', u'Rel Hum (%)',
                            u'Wind Spd (km/h)', u'Visibility (km)', u'Stn Press (kPa)', u'Weather']
    return weather_data


def weather_data_saver(year, month):
    weather = download_weather_month(year, month)
    weather.to_csv(f'weather_{str(year)}_{str(month)}.csv')


#5

# bikes_total_plot()
# bikes_weekdays_plot()
canadian_weather()
# weather_data_saver(2012, 4)
