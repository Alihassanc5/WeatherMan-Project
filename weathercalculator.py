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
