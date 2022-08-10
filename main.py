from os import path
import argparse

from weatherreader import read_weather_files
from weatherparser import parse_weather_readings
from weatherprinter import *


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("path_to_files", type=str, help="Path of files")
        parser.add_argument("-e", "--mode_e", default=[], action="append", help="To do yearly operations")
        parser.add_argument("-a", "--mode_a", default=[], action="append", help="To do monthly operations")
        parser.add_argument("-c", "--mode_c", default=[], action="append", help="To display bar charts of a month")
        args = parser.parse_args()

        operations = {
                      "yearly operations": args.mode_e,
                      "monthly operations": args.mode_a,
                      "monthly bar charts": args.mode_c
        }

        for operation, dates in operations.items():
            for date in dates:
                weather_file_names = []
                weather_files = []

                if (operation == 'monthly operations' or
                        operation == 'monthly bar charts'):
                    year, month = date.split('/')
                    month = int(month)
                    print(month_name[month], year)
                    weather_file_name = ("Murree_weather_"
                                         + year + "_"
                                         + month_abbr[month]
                                         + ".txt")
                    weather_file_names.append(weather_file_name)
                else:
                    for month_number in range(1, 13):
                        weather_file_name = ("Murree_weather_"
                                             + date + "_"
                                             + month_abbr[month_number]
                                             + ".txt")
                        weather_file_names.append(weather_file_name)

                for weather_file_name in weather_file_names:
                    weather_file = path.join(args.path_to_files,
                                             weather_file_name)
                    if path.exists(args.path_to_files):
                        weather_files.append(weather_file)

                weather_readings = read_weather_files(weather_files)
                parsed_weather_readings = parse_weather_readings(weather_readings)
                generate_report(parsed_weather_readings, operation)

    except Exception as e:
        print('Exception Occured!!!')
        print(e)


if __name__ == '__main__':
    main()
