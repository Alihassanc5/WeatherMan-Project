from calendar import month_abbr, month_name
from csv import DictReader


def weather_readings(files, mode):
    readings = []

    for file in files:
        with open(file, newline='') as opened_file:
            reader = DictReader(opened_file, skipinitialspace = True)
            
            for reading in reader:
                weather_reading = parse_reading(reading, mode)
                readings.append(weather_reading)

    return readings


def parse_reading(reading, operation):
    max_temperature = -1 if reading['Max TemperatureC'] == '' else int(reading['Max TemperatureC'])
    min_temperature = -1 if reading['Min TemperatureC'] == '' else int(reading['Min TemperatureC'])

    weather_reading = {'Max TemperatureC': max_temperature, 'Min TemperatureC': min_temperature}
    
    if operation == 'yearly operations':
        timezone = 'PKT' if 'PKT' in reading else 'PKST'
        date = list(map(int,reading[timezone].split('-')))
        max_humidity = -1 if reading['Max Humidity'] == '' else int(reading['Max Humidity'])
        weather_reading['date'] = {'Month': date[1], 'Day': date[2]}
        weather_reading['Max Humidity'] = max_humidity
    
    if operation == 'monthly operations':
        mean_humidity = -1 if reading['Mean Humidity'] == '' else int(reading['Mean Humidity'])
        weather_reading['Mean Humidity'] = mean_humidity

    return weather_reading


def calculate_mean_values(weather_readings):
    highest_temperature_sum = sum(weather_reading['Max TemperatureC'] for weather_reading in weather_readings if weather_reading['Max TemperatureC'] != -1)
    lowest_temperature_sum = sum(weather_reading['Min TemperatureC'] for weather_reading in weather_readings if weather_reading['Min TemperatureC'] != -1)
    mean_humidity_sum = sum(weather_reading['Mean Humidity'] for weather_reading in weather_readings if weather_reading['Mean Humidity'] != -1)
    
    average_highest_temperature = highest_temperature_sum / len(weather_readings)
    average_lowest_temperature = lowest_temperature_sum / len(weather_readings)
    average_mean_humidity = mean_humidity_sum / len(weather_readings) 

    return average_highest_temperature, average_lowest_temperature, average_mean_humidity


def display_bar_charts(weather_readings):
    for day,weather_reading in enumerate(weather_readings, start = 1):
        highest_temperature = weather_reading['Max TemperatureC']
        lowest_temperature = weather_reading['Min TemperatureC']
        
        print(f"{day:02d}", end = '')
        if lowest_temperature >= 0:
            print(f"\033[1;36;40m{lowest_temperature * '+'}\033[0;37;40m", end = '')

        if highest_temperature >= 0:
            print(f"\033[1;31;40m{highest_temperature * '+'}\033[0;37;40m", end = ' ')
        
        if lowest_temperature != -1 and highest_temperature != -1:
           print(f"{lowest_temperature:2d}C - {highest_temperature:2d}C",end = '')
        print()        


def generate_report(weather_readings, operation):
    if operation == 'yearly operations':
        filtered_readings = list(filter(lambda reading: reading['Min TemperatureC'] != -1, weather_readings))
        lowest_temp_weather = min(filtered_readings, key = lambda reading: reading['Min TemperatureC'])
        highest_temp_weather = max(filtered_readings, key = lambda reading: reading['Max TemperatureC'])
        most_humid_weather = max(filtered_readings, key = lambda reading: reading['Max Humidity'])

        print(f"Highest: {highest_temp_weather['Max TemperatureC']}C on {month_name[highest_temp_weather['date']['Month']]} {highest_temp_weather['date']['Day']}")
        print(f"Lowest: {lowest_temp_weather['Min TemperatureC']}C on {month_name[lowest_temp_weather['date']['Month']]} {lowest_temp_weather['date']['Day']}")
        print(f"Humidity: {most_humid_weather['Max Humidity']}% on {month_name[most_humid_weather['date']['Month']]} {most_humid_weather['date']['Day']}")

    elif operation == 'monthly operations':
        highest_average, lowest_average, average_mean_humidity = calculate_mean_values(weather_readings)
        print(f"Highest Average: {highest_average:.2f}C")
        print(f"Lowest Average: {lowest_average:.2f}C".format())
        print(f"Average Mean Humidity: {average_mean_humidity:.2f}%")

    elif operation == 'monthly bar charts':
        display_bar_charts(weather_readings)

    else:
        raise Exception('Error in report generation!',operation,'is unknown.')

    print('-' * 30, '\n')
