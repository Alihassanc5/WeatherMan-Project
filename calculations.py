from calendar import month_name, month_abbr


def parse_reading(reading):
    weather_reading = []
    date = list(map(int,reading[0].split('-')))
    weather_reading.append(date)
    
    integer_data_indexes = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 17, 18, 20)

    for i in range(1,21):
        if i in integer_data_indexes:
            data = -1 if reading[i]=='' else int(reading[i])
        else:
            data = -1 if reading[i]=='' else float(reading[i])
        
        weather_reading.append(data)

    event = reading[21]
    wind_dir_degrees = -1 if reading[22] == '' else int(reading[22])    
    weather_reading.append(event)
    weather_reading.append(wind_dir_degrees)

    return weather_reading


def read_weathers(file_name, weather_readings):
    weather_file = open(file_name,'r')    
    readings = weather_file.readlines()[1:]
    
    for reading in readings:
        reading = reading.strip().split(',')
        weather_reading = parse_reading(reading)
        weather_readings.append(weather_reading)


def mode_e_calculations(weather_readings):
    lowest_temp_weather = highest_temp_weather = most_humid_weather = weather_readings[0]

    for weather_reading in weather_readings[1:]:
        max_temperature = weather_reading[1]
        min_temperature = weather_reading[3]
        most_humid_temperature = weather_reading[7]
        
        if max_temperature > highest_temp_weather[1] and max_temperature != -1:
            highest_temp_weather = weather_reading

        if min_temperature < lowest_temp_weather[3] and min_temperature != -1:
            lowest_temp_weather = weather_reading

        if most_humid_temperature > most_humid_weather[7] and most_humid_temperature != -1:
            most_humid_weather = weather_reading

    return  highest_temp_weather, lowest_temp_weather, most_humid_weather


def mode_a_calculations(weather_readings):
    highest_temp_sum = 0
    lowest_temp_sum = 0
    mean_humidity_sum = 0

    for weather_reading in weather_readings:
        if weather_reading[1] != -1:
            highest_temp_sum += weather_reading[1]  
        
        if weather_reading[3] != -1:
            lowest_temp_sum += weather_reading[3]
        
        if weather_reading[8] != -1:
            mean_humidity_sum += weather_reading[8]
    
    highest_average = highest_temp_sum / len(weather_readings)
    lowest_average = lowest_temp_sum / len(weather_readings)
    average_mean_humidity = mean_humidity_sum / len(weather_readings) 

    return highest_average, lowest_average, average_mean_humidity


def display_bar_charts(weather_readings):
    for day,weather_reading in enumerate(weather_readings, start = 1):
        highest_temperature = weather_reading[1]
        lowest_temperature = weather_reading[3]
        
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
        print(f"Lowest: {lowest_temp_weather[3]}C on {month_name[lowest_temp_weather[0][1]]} {lowest_temp_weather[0][2]}")
        print(f"Humidity: {most_humid_weather[7]}% on {month_name[most_humid_weather[0][1]]} {most_humid_weather[0][2]}")

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
