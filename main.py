from os import path
import argparse

from calculations import *  

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("path_to_files", type = str, help = "Path of files")
        parser.add_argument("-e", "--mode_e", default=[], action="append", help="To process file in E mode")
        parser.add_argument("-a", "--mode_a", default=[], action="append", help="To process file in A mode")
        parser.add_argument("-c", "--mode_c", default=[], action="append", help="To process file in C mode")
        args = parser.parse_args()

        operations = {"yearly operations": args.mode_e, "monthly operations": args.mode_a, "monthly bar charts": args.mode_c} 
        
        for operation, dates in operations.items():
            for date in dates:
                file_names = []
                file_paths = []

                if operation == 'monthly operations' or operation == 'monthly bar charts':
                    year, month = date.split('/')
                    month = int(month)
                    print(month_name[month], year)
                    
                    file_name = "Murree_weather_" + year + "_" + month_abbr[month] + ".txt"
                    file_names.append(file_name)            
                else:
                    for month_number in range(1, 13):
                        file_name = "Murree_weather_" + date + "_" + month_abbr[month_number] + ".txt"
                        file_names.append(file_name)
                
                for file_name in file_names:
                    file_path = path.join(args.path_to_files, file_name)
                    if path.exists(args.path_to_files):
                        file_paths.append(file_path)

                readings = weather_readings(file_paths, operation)
                generate_report(readings, operation)

    except Exception as e:
        print('Exception Occured!!!')
        print(e)
        

if __name__=='__main__':
    main()
    