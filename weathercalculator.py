class Calculator():
    def __init__(self) -> None:
        self.__lowest_average = 0.0
        self.__highest_average = 0.0
        self.__average_mean_humidity = 0.0

    def calculate_mean_values(self, parsed_weather_readings):
        self.__lowest_average = sum(
            reading['Max TemperatureC'] for reading in parsed_weather_readings if reading['Max TemperatureC'] != -1
        ) / len(parsed_weather_readings)
        self.__highest_average = sum(
            reading['Min TemperatureC'] for reading in parsed_weather_readings if reading['Min TemperatureC'] != -1
        ) / len(parsed_weather_readings)
        self.__average_mean_humidity = sum(
            reading['Mean Humidity'] for reading in parsed_weather_readings if reading['Mean Humidity'] != -1
        ) / len(parsed_weather_readings)

    def get_mean_values(self):
        return {
            'Lowest Average': self.__lowest_average,
            'Highest Average': self.__highest_average,
            'Average Mean Humidity': self.__average_mean_humidity
        }
