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
