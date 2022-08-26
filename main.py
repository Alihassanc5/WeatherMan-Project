from os import path
import argparse

from weathercalculator import Calculator
from weatherparser import Parser
from weatherprinter import *
from weatherreader import Reader


def generate_file_names(date, operation):
    weather_file_names = []
    date = date.split('/')

    for month_number in range(1, 13):
        weather_file_name = ("Murree_weather_" + date[0] + "_" + month_abbr[month_number] + ".txt")
        if operation == 'yearly operations' or int(date[1]) == month_number:
            weather_file_names.append(weather_file_name)

    return weather_file_names
    

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
                weather_reader = Reader()
                weather_parser = Parser()
                weather_calculator = Calculator()
                weather_printer = Printer()
                weather_files = []
                weather_file_names = generate_file_names(date, operation)

                for weather_file_name in weather_file_names:
                    weather_file = path.join(args.path_to_files, weather_file_name)
                    if path.exists(args.path_to_files):
                        weather_files.append(weather_file)

                weather_readings = weather_reader.get_weather_readings(weather_files)
                parsed_weather_readings = weather_parser.get_parsed_weather_readings(weather_readings)
                maen_values = weather_calculator.get_mean_values(parsed_weather_readings)
                weather_printer.print_report(parsed_weather_readings, maen_values, operation)

    except Exception as e:
        print('Exception Occured!!!')
        print(e)

if __name__ == '__main__':
    main()
