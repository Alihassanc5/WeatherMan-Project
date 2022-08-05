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

        modes = {"-e": args.mode_e, "-a": args.mode_a, "-c": args.mode_c} 
        
        for mode, dates in modes.items():
            for date in dates:
                file_names = []
                file_paths = []

                if mode =='-a' or mode=='-c':
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

                readings = weather_readings(file_paths, mode)
                generate_report(readings, mode)

    except Exception as e:
        print('Exception Occured!!!')
        print(e)
        

if __name__=='__main__':
    main()
    