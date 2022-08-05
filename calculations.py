from calendar import month_abbr, month_name
from contextlib import ExitStack
from csv import DictReader
from os import path

def get_file_path(path_to_files, date):
    year, month = date.split('/')
    month = int(month)  
    print(month_name[month], year)

    file_name = "Murree_weather_" + year + "_" + month_abbr[month] + ".txt"
 
    if path.exists(path_to_files):
        file_path = path.join(path_to_files, file_name)
        return file_path


def weather_readings(file_names, mode):
    readings = []
    
    with ExitStack() as stack:
        for file_name in file_names:
            file = stack.enter_context(open(file_name, 'r'))
            readings = file.readlines()
            header = readings[0].split(',')
            
            for reading in readings[1:]:
                reading = reading.strip().split(',')
                
                if mode == '-e':
                    weather_reading = mode_e_parsing(header, reading)
                elif mode == '-a':
                    weather_reading = mode_a_parsing(header, reading)
                else:
                    weather_reading = mode_c_parsing(header, reading)    

                readings.append(weather_reading)
    
    return readings


def mode_e_parsing(header, reading):
    date_index = header.index('PKT')    
    max_temp_index = header.index('Max TemperatureC')
    min_temp_index = header.index('Min TemperatureC')
    max_humidity_index = header.index('Max Humidity')
    
    date = list(map(int,reading[date_index].split('-')))
    max_temperature = -1 if reading[max_temp_index] == '' else int(reading[max_temp_index])
    min_temperature = -1 if reading[min_temp_index] == '' else int(reading[min_temp_index])
    max_humidity = -1 if reading[max_humidity_index] == '' else int(reading[max_humidity_index])
    
    weather_reading = [date, max_temperature, min_temperature, max_humidity]

    return weather_reading

def mode_a_parsing(header, reading):
    max_temp_index = header.index('Max TemperatureC')
    min_temp_index = header.index('Min TemperatureC')
    max_humidity_index = header.index(' Mean Humidity')
    
    max_temperature = -1 if reading[max_temp_index] == '' else int(reading[max_temp_index])
    min_temperature = -1 if reading[min_temp_index] == '' else int(reading[min_temp_index])
    mean_humidity = -1 if reading[max_humidity_index] == '' else int(reading[max_humidity_index])
    
    weather_reading = [max_temperature, min_temperature, mean_humidity]  
     
    return weather_reading


def mode_c_parsing(header, reading):
    max_temp_index = header.index('Max TemperatureC')
    min_temp_index = header.index('Min TemperatureC')
    
    max_temperature = -1 if reading[max_temp_index] == '' else int(reading[max_temp_index])
    min_temperature = -1 if reading[min_temp_index] == '' else int(reading[min_temp_index])

    weather_reading = [max_temperature, min_temperature]
       
    return weather_reading


def mode_e_calculations(weather_readings):
    lowest_temp_weather = highest_temp_weather = most_humid_weather = weather_readings[0]

    for weather_reading in weather_readings[1:]:
        max_temperature = weather_reading[1]
        min_temperature = weather_reading[2]
        most_humid_temperature = weather_reading[3]
        
        if max_temperature > highest_temp_weather[1] and max_temperature != -1:
            highest_temp_weather = weather_reading

        if min_temperature < lowest_temp_weather[2] and min_temperature != -1:
            lowest_temp_weather = weather_reading

        if most_humid_temperature > most_humid_weather[3] and most_humid_temperature != -1:
            most_humid_weather = weather_reading

    return  highest_temp_weather, lowest_temp_weather, most_humid_weather


def mode_a_calculations(weather_readings):
    highest_temp_sum = 0
    lowest_temp_sum = 0
    mean_humidity_sum = 0

    for weather_reading in weather_readings:
        if weather_reading[0] != -1:
            highest_temp_sum += weather_reading[0]  
        
        if weather_reading[1] != -1:
            lowest_temp_sum += weather_reading[1]
        
        if weather_reading[2] != -1:
            mean_humidity_sum += weather_reading[2]
    
    highest_average = highest_temp_sum / len(weather_readings)
    lowest_average = lowest_temp_sum / len(weather_readings)
    average_mean_humidity = mean_humidity_sum / len(weather_readings) 

    return highest_average, lowest_average, average_mean_humidity


def display_bar_charts(weather_readings):
    for day,weather_reading in enumerate(weather_readings, start = 1):
        highest_temperature = weather_reading[0]
        lowest_temperature = weather_reading[1]
        
        print(f"{day:02d}", end = '')
        if lowest_temperature >= 0:
            print(f"\033[1;36;40m{lowest_temperature * '+'}\033[0;37;40m", end = '')

        if highest_temperature >= 0:
            print(f"\033[1;31;40m{highest_temperature * '+'}\033[0;37;40m", end = ' ')
        
        if lowest_temperature != -1 and highest_temperature != -1:
           print(f"{lowest_temperature:2d}C - {highest_temperature:2d}C",end = '')
        print()        


def generate_report(mode, weather_readings):
    if mode == '-e':
        highest_temp_weather, lowest_temp_weather, most_humid_weather = mode_e_calculations(weather_readings)
        print(f"Highest: {highest_temp_weather[1]}C on {month_name[highest_temp_weather[0][1]]} {highest_temp_weather[0][2]}")
        print(f"Lowest: {lowest_temp_weather[2]}C on {month_name[lowest_temp_weather[0][1]]} {lowest_temp_weather[0][2]}")
        print(f"Humidity: {most_humid_weather[3]}% on {month_name[most_humid_weather[0][1]]} {most_humid_weather[0][2]}")

    elif mode == '-a':
        highest_average, lowest_average, average_mean_humidity = mode_a_calculations(weather_readings)
        print(f"Highest Average: {highest_average:.2f}C")
        print(f"Lowest Average: {lowest_average:.2f}C".format())
        print(f"Average Mean Humidity: {average_mean_humidity:.2f}%")

    elif mode == '-c':
        display_bar_charts(weather_readings)

    else:
        raise Exception('Error in report generation!',mode,'is unknown mode.')

    print('-' * 30, '\n')
