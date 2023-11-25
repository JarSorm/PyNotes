import pandas as pd
import pathlib
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from pandas.errors import DtypeWarning

plt.style.use('ggplot')
work_path = pathlib.Path.cwd()
data_path = Path(work_path, 'bikes.csv')
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


# 2
def nyc_analise_complaints():
    complaints = None
    plt.rcParams['figure.figsize'] = (10, 5)
    try:
        complaints = pd.read_csv('311-service.csv')
    except DtypeWarning:
        pass
    complaint_counts = complaints['Complaint Type'].value_counts()
    # print(complaint_counts[:10])
    complaint_counts[:10].plot(kind='bar')
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
    year, month = 2012, 3
    pd.options.display.max_rows = 7
    plt.rcParams['figure.figsize'] = (15, 3)
    plt.rcParams['font.family'] = 'sans-serif'
    try:
        weather_final = pd.read_csv(f'weather_{str(year)}_{str(month)}.csv', index_col='Date/Time (LST)',
                                    parse_dates=['Date/Time (LST)'])
    except FileNotFoundError:
        weather_data_saver(year, month)
        print(f'The file was not found. The data was downloaded and saved to: weather_{str(year)}_{str(month)}.csv')
        weather_final = pd.read_csv(f'weather_{str(year)}_{str(month)}.csv', index_col='Date/Time (LST)',
                                    parse_dates=['Date/Time (LST)'])
    # weather_final['Temp (C)'].plot(figsize=(18, 6))
    temperatures = weather_final[['Temp (C)']].copy()
    temperatures.loc[:, 'hour'] = weather_final.index.hour
    temperatures.groupby('hour').aggregate(np.median).plot()
    plt.show()


# 5
def most_snowy_month():
    year = 2012
    try:
        weather_2012 = pd.read_csv('weather_2012.csv', parse_dates=True, index_col='Date/Time (LST)')
    except FileNotFoundError:
        weather_data_saver(year)
        weather_2012 = pd.read_csv('weather_2012.csv', parse_dates=True, index_col='Date/Time (LST)')
    temp = weather_2012['Temp (C)'].resample('M').median()
    is_snowing = weather_2012['Weather'].str.contains('Snow')
    snowiness = is_snowing.astype(int).resample('M').mean()
    temp.name = "Temp"
    snowiness.name = "Snowiness"
    stats = pd.concat([temp, snowiness], axis=1)
    stats.plot(kind='bar', subplots=True, figsize=(15, 10))
    plt.show()


# 6
def contaminated_data():
    pd.options.display.max_columns = 6
    plt.rcParams['figure.figsize'] = (15, 3)
    plt.rcParams['font.family'] = 'Times New Roman'
    # requests = pd.read_csv('311-service.csv')
    # print(requests['Incident Zip'].unique())
    na_values = ['NO CLUE', 'N/A', '0']
    requests = pd.read_csv('311-service.csv', na_values=na_values, dtype={'Incident Zip': str})
    # rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
    # requests[rows_with_dashes]['Incident Zip']
    # len(requests[rows_with_dashes])
    # long_zip_codes = requests['Incident Zip'].str.len() > 5
    # requests['Incident Zip'][long_zip_codes].unique()
    # requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
    # zero_zips = requests['Incident Zip'] == '00000'
    # requests.loc[zero_zips, 'Incident Zip'] = np.nan
    # unique_zips = requests['Incident Zip'].unique()
    # zips = requests['Incident Zip']
    # is_close = zips.str.startswith('0') | zips.str.startswith('1')
    # is_far = ~is_close & zips.notnull()
    # print(zips[is_far])
    print(requests['City'].str.upper().value_counts())


# 7
def unix_timestamps():
    pd.options.display.max_columns = 5
    plt.rcParams['figure.figsize'] = (15, 5)
    popcon = pd.read_csv('popularity-contest.txt', sep=' ')[:-1]
    popcon.columns = ['1st-time', '2nd-time', 'package', 'program', 'tag']
    popcon['1st-time'] = popcon['1st-time'].astype(int)
    popcon['2nd-time'] = popcon['2nd-time'].astype(int)
    # print(popcon['1st-time'].dtype)
    popcon['1st-time'] = pd.to_datetime(popcon['1st-time'], unit='s')
    popcon['2nd-time'] = pd.to_datetime(popcon['2nd-time'], unit='s')
    # print(popcon[:5])
    popcon = popcon[popcon['1st-time'] > '1970-01-01']
    nonlibraries = popcon[~popcon['package'].str.contains('lib')]
    print(nonlibraries.sort_values('2nd-time', ascending=False)[:10])


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


def weather_data_saver(year, month=None):
    if month is None:
        weather = [download_weather_month(year, i) for i in range(1, 13)]
        year_weather = pd.concat(weather)
        year_weather.to_csv(f'weather_{str(year)}.csv')
    elif 1 <= month <= 12:
        weather = download_weather_month(year, month)
        weather.to_csv(f'weather_{str(year)}_{str(month)}.csv')


# bikes_total_plot()
# nyc_analise_complaints()
# bikes_weekdays_plot()
# canadian_weather()
# weather_data_saver(2012)
# most_snowy_month()
# contaminated_data()
unix_timestamps()
