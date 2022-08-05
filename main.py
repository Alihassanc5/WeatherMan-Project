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
    
        for year in args.mode_e:
            file_paths = []            
            for month_number in range(1, 13):
                file_name = "Murree_weather_" + year + "_" + month_abbr[month_number] + ".txt"
 
                if path.exists(args.path_to_files):
                    file_path = path.join(args.path_to_files, file_name)
                    file_paths.append(file_path)
 
            print(year)
            readings = weather_readings(file_paths, "-e")
            generate_report("-e", readings)

        for date in args.mode_a:
            file_paths = []
            file_path = get_file_path(args.path_to_files, date)
            file_paths.append(file_path)
            readings = weather_readings(file_paths, "-a")
            generate_report("-a", readings)

        for date in args.mode_c:
            file_paths = []
            file_path = get_file_path(args.path_to_files, date)
            file_paths.append(file_path)
            readings = weather_readings(file_paths, "-c")
            generate_report("-c", readings)

    except Exception as e:
        print('Exception Occured!!!')
        print(e)
        

if __name__=='__main__':
    main()
    