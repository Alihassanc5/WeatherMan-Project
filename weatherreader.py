from csv import DictReader


class Reader:
    def __init__(self) -> None:
        self.__weather_readings = []

    def read_weather_files(self, weather_files):
        for weather_file in weather_files:
            with open(weather_file, newline='') as opened_weather_file:
                weather_reader = DictReader(opened_weather_file,
                                            skipinitialspace=True)

                for weather_reading in weather_reader:
                    self.__weather_readings.append(weather_reading)

    def get_weather_readings(self):
        return self.__weather_readings
