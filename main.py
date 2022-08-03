import sys
from os import listdir, path
from calculations import *


def main():
    path_to_files = sys.argv[1]
    
    try:
        for i in range(2, len(sys.argv), 2):            
            weather_readings = []
            mode = sys.argv[i]

            if mode =='-a' or mode=='-c':
                year, month = list(map(int, sys.argv[i+1].split('/')))
            else:
                year = int(sys.argv[i+1])

            for file_name in listdir(path_to_files):
                file_name = path.join(path_to_files,file_name)
                file_year = int(file_name.split('_')[2])
                file_month = get_month_number(file_name.split('_')[3][:3])
            
                if mode=='-e' and year==file_year:
                    read_weathers(file_name, weather_readings)
                        
                if (mode=='-a' or mode=='-c') and year==file_year and month==file_month:
                    read_weathers(file_name, weather_readings)
                    
                    if mode=='-c':
                        print(get_month_name(month),year)
                    
                    break

            generate_report(mode, weather_readings)             
    
    except Exception as e:
        print('Exception Occured!!!')
        print(e)
        

if __name__=='__main__':
    main()