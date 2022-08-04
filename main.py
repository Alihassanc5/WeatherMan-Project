import argparse
from calculations import *
    

def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("path_to_files", type = str, help = "Path of files")
        parser.add_argument("-e", "--mode_e", default=[],type=int, action="append", help="To process file in E mode")
        parser.add_argument("-a", "--mode_a", default=[], action="append", help="To process file in A mode")
        parser.add_argument("-c", "--mode_c", default=[], action="append", help="To process file in C mode")
        args = parser.parse_args()
    
        for year in args.mode_e:            
            file_names = []
            for file_name in listdir(args.path_to_files):
                file = path.join(args.path_to_files, file_name)
                file_year = int(file_name.split('_')[2]) 
                if year == file_year:
                    file_names.append(file)

            print(year)
            weather_readings = read_weathers(file_names, "-e")
            generate_report("-e", weather_readings)

        for date in args.mode_a:
            file_name = get_file_name(args.path_to_files, date)
            weather_readings = read_weathers(file_name, "-a")
            generate_report("-a", weather_readings)

        for date in args.mode_c:
            file_name = get_file_name(args.path_to_files, date)
            weather_readings = read_weathers(file_name, "-c")
            generate_report("-c", weather_readings)

    except Exception as e:
        print('Exception Occured!!!')
        print(e)
        

if __name__=='__main__':
    main()