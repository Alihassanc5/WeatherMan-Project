class Calculator():
    def __init__(self) -> None:
        pass

    def get_mean_values(self, parsed_weather_readings):
        lowest_average = sum(
            reading['Max TemperatureC'] for reading in parsed_weather_readings if reading['Max TemperatureC'] != -1
        ) / len(parsed_weather_readings)
        highest_average = sum(
            reading['Min TemperatureC'] for reading in parsed_weather_readings if reading['Min TemperatureC'] != -1
        ) / len(parsed_weather_readings)
        average_mean_humidity = sum(
            reading['Mean Humidity'] for reading in parsed_weather_readings if reading['Mean Humidity'] != -1
        ) / len(parsed_weather_readings)

        return {
            'Lowest Average': lowest_average,
            'Highest Average': highest_average,
            'Average Mean Humidity': average_mean_humidity
        }
