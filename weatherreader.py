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
