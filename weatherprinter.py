from calendar import month_abbr, month_name

from weathercalculator import calculate_mean_values


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
