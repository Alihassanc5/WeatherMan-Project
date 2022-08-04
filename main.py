from os import listdir, path
import sys
from calculations import *


def main():
    path_to_files = sys.argv[1]
    
    try:
        for index in range(2, len(sys.argv), 2):            
            weather_readings = []
            mode = sys.argv[index]
            
            if mode == '-a' or mode== '-c':
                year, month = list(map(int, sys.argv[index+1].split('/')))
            else:
                year = int(sys.argv[index+1])
            
            file_names = []
            for file_name in listdir(path_to_files):
                file = path.join(path_to_files,file_name)
                file_year = int(file_name.split('_')[2]) 
                file_month = list(month_abbr).index(file_name.split('_')[3][:3])
            
                if ((mode == '-a' and year == file_year and month == file_month) or
                    (mode == '-c' and year == file_year and month == file_month) or
                    (mode == '-e' and year == file_year)):
                     file_names.append(file)

                if mode == '-c' and year == file_year and month == file_month:
                    print(month_name[month], year)

            weather_readings = read_weathers(file_names, mode)
            generate_report(mode, weather_readings)             
    
    except Exception as e:
        print('Exception Occured!!!')
        print(e)
        

if __name__=='__main__':
    main()
