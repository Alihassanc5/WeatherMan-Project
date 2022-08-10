from calendar import month_abbr, month_name
from csv import DictReader


def read_weather_files(weather_files):
    weather_readings = []

    for weather_file in weather_files:
        with open(weather_file, newline='') as opened_weather_file:
            weather_reader = DictReader(opened_weather_file,
                                        skipinitialspace=True)

            for weather_reading in weather_reader:
                weather_readings.append(weather_reading)

    return weather_readings


def parse_weather_reading(weather_reading):
    max_temperature = -1 if weather_reading['Max TemperatureC'] == '' \
        else int(weather_reading['Max TemperatureC'])
    min_temperature = -1 if weather_reading['Min TemperatureC'] == '' \
        else int(weather_reading['Min TemperatureC'])
    max_humidity = -1 if weather_reading['Max Humidity'] == '' \
        else int(weather_reading['Max Humidity'])
    mean_humidity = -1 if weather_reading['Mean Humidity'] == '' \
        else int(weather_reading['Mean Humidity'])
    timezone = 'PKT' if 'PKT' in weather_reading else 'PKST'
    date = list(map(int, weather_reading[timezone].split('-')))

    parsed_weather_reading = {
                              'Max TemperatureC': max_temperature,
                              'Min TemperatureC': min_temperature,
                              'date': {'Month': date[1], 'Day': date[2]},
                              'Mean Humidity': mean_humidity,
                              'Max Humidity': max_humidity
                             }

    return parsed_weather_reading


def parse_weather_readings(weather_readings):
    parsed_weather_readings = []

    for weather_reading in weather_readings:
        parsed_weather_reading = parse_weather_reading(weather_reading)
        parsed_weather_readings.append(parsed_weather_reading)

    return parsed_weather_readings


def calculate_mean_values(weather_readings):
    average_max_temperature = sum(
                                  reading['Max TemperatureC']
                                  for reading in weather_readings
                                  if reading['Max TemperatureC'] != -1
                              ) / len(weather_readings)
    average_min_temperature = sum(
                                  reading['Min TemperatureC']
                                  for reading in weather_readings
                                  if reading['Min TemperatureC'] != -1
                              ) / len(weather_readings)
    average_mean_humidity = sum(
                                reading['Mean Humidity']
                                for reading in weather_readings
                                if reading['Mean Humidity'] != -1
                            ) / len(weather_readings)

    return average_max_temperature, average_min_temperature, \
        average_mean_humidity


def display_bar_charts(weather_readings):
    for day, weather_reading in enumerate(weather_readings, start=1):
        highest_temperature = weather_reading['Max TemperatureC']
        lowest_temperature = weather_reading['Min TemperatureC']

        print(f"{day:02d}", end='')
        if lowest_temperature >= 0:
            print(f"\033[1;36;40m{lowest_temperature * '+'}\033[0;37;40m", end='')
        if highest_temperature >= 0:
            print(f"\033[1;31;40m{highest_temperature * '+'}\033[0;37;40m", end=' ')
        if lowest_temperature != -1 and highest_temperature != -1:
            print(f"{lowest_temperature:2d}C - {highest_temperature:2d}C", end='')
        print()


def generate_report(weather_readings, operation):
    if operation == 'yearly operations':
        filtered_readings = list(
                                filter(
                                    lambda reading:
                                    reading['Min TemperatureC'] != -1,
                                    weather_readings
                                )
                            )
        lowest_temp_weather = min(
                                  filtered_readings,
                                  key=lambda reading:
                                  reading['Min TemperatureC']
                              )
        highest_temp_weather = max(
                                   filtered_readings,
                                   key=lambda reading:
                                   reading['Max TemperatureC']
                               )
        most_humid_weather = max(
                                 filtered_readings,
                                 key=lambda reading:
                                 reading['Max Humidity']
                             )

        print(
            f"Highest: {highest_temp_weather['Max TemperatureC']}C on"
            f"{month_name[highest_temp_weather['date']['Month']]} "
            f"{highest_temp_weather['date']['Day']}"
        )
        print(
            f"Lowest: {lowest_temp_weather['Min TemperatureC']}C on "
            f"{month_name[lowest_temp_weather['date']['Month']]} "
            f"{lowest_temp_weather['date']['Day']}"
        )
        print(
            f"Humidity: {most_humid_weather['Max Humidity']}% on "
            f"{month_name[most_humid_weather['date']['Month']]} "
            f"{most_humid_weather['date']['Day']}"
        )
    elif operation == 'monthly operations':
        highest_average, lowest_average, average_mean_humidity = calculate_mean_values(weather_readings)
        print(f"Highest Average: {highest_average:.2f}C")
        print(f"Lowest Average: {lowest_average:.2f}C".format())
        print(f"Average Mean Humidity: {average_mean_humidity:.2f}%")
    elif operation == 'monthly bar charts':
        display_bar_charts(weather_readings)
    else:
        raise Exception('Error in report generation!',
                        operation, 'is unknown.')

    print('-' * 30, '\n')
