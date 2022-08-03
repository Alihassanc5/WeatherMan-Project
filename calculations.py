def get_month_name(month):   
    if month==1:
        return "January"
    elif month==2:
        return "February"
    elif month==3:
        return "March"
    elif month==4:
        return "April"
    elif month==5:
        return "May"
    elif month==6:
        return "June"
    elif month==7:
        return "July"
    elif month==8:
        return "August" 
    elif month==9:
        return "September"
    elif month==10:
        return "October"
    elif month==11:
        return "November"
    else:
        return "December"


def get_month_number(name):
    if name=='Jan':
        return 1
    elif name=='Feb':
        return 2
    elif name=='Mar':
        return 3
    elif name=='Apr':
        return 4
    elif name=='May':
        return 5
    elif name=='Jun':
        return 6
    elif name=='Jul':
        return 7
    elif name=='Aug':
        return 8
    elif name=='Sep':
        return 9
    elif name=='Oct':
        return 10
    elif name=='NOV':
        return 11
    elif name=='Dec':
        return 5
    

def parse_reading(reading):
    weather_reading = []
    date = list(map(int,reading[0].split('-')))
    weather_reading.append(date)
    
    integer_data_indexes = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 17, 18, 20)

    for i in range(1,21):
        if i in integer_data_indexes:
            data = -1 if reading[i]=='' else int(reading[i])
        else:
            data = -1 if reading[i]=='' else float(reading[i])
        
        weather_reading.append(data)

    event = reading[21]
    wind_dir_degrees = -1 if reading[22] =='' else int(reading[22])    
    weather_reading.append(event)
    weather_reading.append(wind_dir_degrees)

    return weather_reading


def read_weathers(file_name, weather_readings):
    weather_file = open(file_name,'r')    
    readings = weather_file.readlines()[1:]
    
    for reading in readings:
        reading = reading.strip().split(',')
        weather_reading = parse_reading(reading)
        weather_readings.append(weather_reading)


def mode_e_calculations(weather_readings):
    lowest_temp_weather = highest_temp_weather = most_humid_weather = weather_readings[0]

    for weather_reading in weather_readings[1:]:
        max_temperature = weather_reading[1]
        min_temperature = weather_reading[3]
        most_humid_temperature = weather_reading[7]
        
        if max_temperature>highest_temp_weather[1] and max_temperature!=-1:
            highest_temp_weather = weather_reading

        if min_temperature<lowest_temp_weather[3] and min_temperature!=-1:
            lowest_temp_weather = weather_reading

        if most_humid_temperature>most_humid_weather[7] and most_humid_temperature!=-1:
            most_humid_weather = weather_reading

    return  highest_temp_weather, lowest_temp_weather, most_humid_weather


def mode_a_calculations(weather_readings):
    highest_temp_sum = 0
    lowest_temp_sum = 0
    mean_humidity_sum = 0

    for weather_reading in weather_readings:
        if weather_reading[1]!=-1:
            highest_temp_sum += weather_reading[1]  
        
        if weather_reading[3]!=-1:
            lowest_temp_sum += weather_reading[3]
        
        if weather_reading[8]!=-1:
            mean_humidity_sum += weather_reading[8]
    
    highest_average = highest_temp_sum / len(weather_readings)
    lowest_average = lowest_temp_sum / len(weather_readings)
    average_mean_humidity = mean_humidity_sum / len(weather_readings) 

    return highest_average, lowest_average, average_mean_humidity


def display_bar_charts(weather_readings):
    for day,weather_reading in enumerate(weather_readings, start=1):
        highest_temperature = weather_reading[1]
        lowest_temperature = weather_reading[3]
        
        print(f"{day:02d}", end='')
        if lowest_temperature>=0:
            print('\033[1;36;40m{}\033[0;37;40m'.format(lowest_temperature * '+'), end='')

        if highest_temperature>=0:
            print('\033[1;31;40m{}\033[0;37;40m'.format(highest_temperature * '+'), end=' ')
        
        if lowest_temperature!=-1 and highest_temperature!=-1:
           print('{:2d}C - {:2d}C'.format(lowest_temperature, highest_temperature),end='')
        print()
        

def generate_report(mode, weather_readings):
    if mode=='-e':
        highest_temp_weather, lowest_temp_weather, most_humid_weather = mode_e_calculations(weather_readings)
        print("Highest: {}C on {} {}".format(highest_temp_weather[1], get_month_name(highest_temp_weather[0][1]), highest_temp_weather[0][2]))
        print("Lowest: {}C on {} {}".format(lowest_temp_weather[3], get_month_name(lowest_temp_weather[0][1]), lowest_temp_weather[0][2]))
        print("Humidity: {}% on {} {}".format(most_humid_weather[7], get_month_name(most_humid_weather[0][1]), most_humid_weather[0][2]))

    elif mode=='-a':
        highest_average, lowest_average, average_mean_humidity = mode_a_calculations(weather_readings)
        print("Highest Average: {:.2f}C".format(highest_average))
        print("Lowest Average: {:.2f}C".format(lowest_average))
        print("Average Mean Humidity: {:.2f}%".format(average_mean_humidity))

    elif mode=='-c':
        display_bar_charts(weather_readings)

    else:
        raise Exception('Error in report generation!',mode,'is unknown mode.')

    print('-'*30,'\n')