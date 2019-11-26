#Venz Pops

import pprint
import csv
import datetime
import os
from collections import defaultdict
import operator
import time

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = (input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')).lower()
    # TODO: handle raw input and complete function
    if ( city == "chicago") :
        with open('chicago.csv') as f:
            city_file = list(line for line in csv.reader (f, delimiter =','))
            return city_file
    elif (city == "new york") :
        with open('new_york_city.csv') as f:
            city_file = list(line for line in csv.reader (f, delimiter =','))
            return city_file
    elif (city == "washington") :
        with open('washington.csv') as f:
            city_file = list(line for line in csv.reader (f, delimiter =','))
            return city_file
    else :
        print ("Please select with in Chicago, New York, or Washington")
        city_file = get_city()
        return city_file


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) returns the time filter as per the user choice by month, day, none
    '''
    #time_period=""
    time_period = (input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')).lower()
    # TODO: handle raw input and complete function
    #if time_period == "month" or time_period == "day" or time_period = "none":
    if time_period == "none" or time_period == "month" or time_period == "day" :
        return time_period
        #print("")
    else :
        print ("Please select with in month, day, or none")
        time_period = get_time_period()
        return time_period
    #return time_period

def get_month():
    '''Asks the user for a month and returns the specified month number.

    Args:
        none.
    Returns:
        (str) returns the month number of the month which user choice
    '''
    month = (input('\nWhich month? January, February, March, April, May, or June?\n')).lower()
    # TODO: handle raw input and complete function
    if month == "january" or month == "february" or month == "march" or month == "april" or month == "may"  or month == "june":
        month_number=datetime.datetime.strptime(month,"%B").strftime('%m')
        #print(month, month_number)
        return month_number
    else :
        print ("Please select with in Jan to Jun month only")
        month_number = get_month()
        #month_number=datetime.datetime.strptime(month,"%B").strftime('%m')
        #print(month_number)
        return month_number

def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (str) returns the day number of user choice
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    try :
        day_number=datetime.datetime.strptime(day,'%d').strftime('%d')
        return day_number
    except (ValueError):
        #print("Counts of gender :Null")
        print ("Please select with in 1 to 31 days")
        day_number = get_day()
        return day_number
    #day_number=datetime.datetime.strptime(day,'%d').strftime('%d')
    #return day_number

def popular_month(filtered_csv_reader):
    '''Calculate and returns the popular month for start time if user choice is none filter
    Args:
        filtered csv input as per user filter choice
    Returns:
        (str) returns the popular month for start time

    Question: What is the most popular month for start time?
    '''
    # TODO: complete function

    month_count = {
    "January" : 0,
    "February" : 0,
    "March" : 0,
    "April" : 0,
    "May" : 0,
    "June" : 0,
    "July" : 0,
    "August" : 0,
    "September" : 0,
    "October" : 0,
    "November" : 0,
    "December" : 0
    }

    for i in filtered_csv_reader[0:]:
        month =datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").strftime('%m')
        if month == '01' :
            month_count['January'] +=1
        elif month == '02' :
            month_count['February'] +=1
        elif month == '03' :
            month_count['March'] +=1
        elif month == '04' :
            month_count['April'] +=1
        elif month == '05' :
            month_count['May'] +=1
        elif month == '06' :
            month_count['June'] +=1
        elif month == '07' :
            month_count['July'] +=1
        elif month == '08' :
            month_count['August'] +=1
        elif month == '09' :
            month_count['September'] +=1
        elif month == '10' :
            month_count['October'] +=1
        elif month == '11' :
            month_count['November'] +=1
        elif month == '12' :
            month_count['December'] +=1
        else :
            print("other month also in the list")

    s=max(zip(month_count.values(),month_count.keys()))
    print("Most popular Month for start time: ", s[1])

def popular_day(city_file):
    '''Calculate and returns the popular day for start time if user choice is none or month filter
    Args:
        filtered csv input as per user filter choice
    Returns:
        (str) returns the popular day for start time

    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    day_count = {
    "Sun" : 0,
    "Mon" : 0,
    "Tue" : 0,
    "Wed" : 0,
    "Thu" : 0,
    "Fri" : 0,
    "Sat" : 0,
    }
    for i in city_file [0:]:
        day =datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").strftime('%a')
        if day == 'Sun' :
            day_count['Sun'] +=1
        elif day == 'Mon' :
            day_count['Mon'] +=1
        elif day == 'Tue' :
            day_count['Tue'] +=1
        elif day == 'Wed' :
            day_count['Wed'] +=1
        elif day == 'Thu' :
            day_count['Thu'] +=1
        elif day == 'Fri' :
            day_count['Fri'] +=1
        elif day == 'Sat' :
            day_count['Sat'] +=1
        else :
            print("Day format wrong")

    s=max(zip(day_count.values(),day_count.keys()))
    print("Most popular day :", s[1])

def popular_hour(city_file):
    '''Calculate and returns the popular hour for start time if user choice is any filter
    Args:
        filtered csv input as per user filter choice
    Returns:
        (str) returns the popular hour for start time

    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    hour_count = {
    "00" : 0,
    "01" : 0,
    "02" : 0,
    "03" : 0,
    "04" : 0,
    "05" : 0,
    "06" : 0,
    "07" : 0,
    "08" : 0,
    "09" : 0,
    "10" : 0,
    "11" : 0,
    "12" : 0,
    "13" : 0,
    "14" : 0,
    "15" : 0,
    "16" : 0,
    "17" : 0,
    "18" : 0,
    "19" : 0,
    "20" : 0,
    "21" : 0,
    "22" : 0,
    "23" : 0,
    }
    for i in city_file [0:]:
        hour =datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").strftime('%H')
        if hour == '00' :
            hour_count['00'] +=1
        elif hour == '01' :
            hour_count['01'] +=1
        elif hour == '02' :
            hour_count['02'] +=1
        elif hour == '03' :
            hour_count['03'] +=1
        elif hour == '04' :
            hour_count['04'] +=1
        elif hour == '05' :
            hour_count['05'] +=1
        elif hour == '06' :
            hour_count['06'] +=1
        elif hour == '07' :
            hour_count['07'] +=1
        elif hour == '08' :
            hour_count['08'] +=1
        elif hour == '09' :
            hour_count['09'] +=1
        elif hour == '10' :
            hour_count['10'] +=1
        elif hour == '11' :
            hour_count['11'] +=1
        elif hour == '12' :
            hour_count['12'] +=1
        elif hour == '13' :
            hour_count['13'] +=1
        elif hour == '14' :
            hour_count['14'] +=1
        elif hour == '15' :
            hour_count['15'] +=1
        elif hour == '16' :
            hour_count['16'] +=1
        elif hour == '17' :
            hour_count['17'] +=1
        elif hour == '18' :
            hour_count['18'] +=1
        elif hour == '19' :
            hour_count['19'] +=1
        elif hour == '20' :
            hour_count['20'] +=1
        elif hour == '21' :
            hour_count['21'] +=1
        elif hour == '22' :
            hour_count['22'] +=1
        elif hour == '23' :
            hour_count['23'] +=1
        else :
            print("Day format wrong")

    s=max(zip(hour_count.values(),hour_count.keys()))
    print("Most popular hour of day for start time : ", s[1])


def trip_duration(city_file):
    '''Calculate and returns the trip duration of particular city
    Args:
        filtered csv input as per user filter choice
    Returns:
        (str) returns the trip duration

    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    total_trip=0
    for i in city_file [0:]:
        #hour =datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").strftime('%H')
        total_trip=total_trip+(float(i[3]))

        #print(city_file[1,2])
    #print(total_trip)
    avg_trip=total_trip/(len(city_file)-1)
    print("Total trip duration : ", total_trip)
    print("Average trip duration : ",avg_trip)

def popular_stations(city_file):
    '''Calculate and returns the popular start and end station of particular city
    Args:
        filtered csv input as per user filter choice
    Returns:
        (str,int) returns the popular start and end station
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    pop_start=dict()
    pop_end=dict()
    '''Calculate popular Start station'''
    for i in city_file [0:]:
        if i[4] not in pop_start:
            pop_start.update({i[4]:0})
    for i in city_file [0:]:
        if i[4] in pop_start :
            pop_start[i[4]] +=1

    print ("Most Popular start station : " ,max(pop_start.items(), key= lambda x: x[1]))

    '''Calculate popular End station'''
    for i in city_file [0:]:
        if i[5] not in pop_end:
            pop_end.update({i[5]:0})

    for i in city_file [0:]:
        if i[5] in pop_end :
            pop_end[i[5]] +=1
    print ("Most Popular End station : " ,max(pop_end.items(), key= lambda x: x[1]))


def popular_trip(city_file):
    '''Calculate and returns the popular trip with combination of start and end station of particular city
    Args:
        filtered csv input as per user filter choice
    Returns:
        (str,int) returns the popular trip with station details
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    i=tuple()
    pop_trip=dict()
    for i in city_file [0:]:
        if (i[4]+" to "+i[5]) not in pop_trip:
            #z1.update = (i[4:5]:0)
            pop_trip.update({(i[4]+" to "+i[5]):0})

    for i in city_file [0:]:
        if (i[4]+" to "+i[5]) in pop_trip:
            pop_trip[i[4]+" to "+i[5]] +=1

    print ("Most Popular Trip : " ,max(pop_trip.items(), key= lambda x: x[1]))

def users(city_file):
    '''Calculate and returns the count of each user types of particular city
    Args:
        filtered csv input as per user filter choice
    Returns:
        (dict) returns the count of each user types
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    user_dict=dict()
    for i in city_file [0:]:
        if i[6] not in user_dict:
            user_dict.update({i[6]:0})

    for i in city_file [0:]:
        if i[6] in user_dict :
            user_dict[i[6]] +=1
    print ("Counts of each user type : ",user_dict)


def gender(city_file):
    '''Calculate and returns the count of gender types for particular city
    Args:
        filtered csv input as per user filter choice
    Returns:
        (dict) returns the count of each gender types
        Null if there is no data for gender
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    gen_dict=dict()
    #z1=dict()
    try :
        if (len(city_file[0][7])) > 1:
            lambda x: x
    except (IndexError):
        print("Counts of gender :Null")
        return
    for i in city_file [0:]:
        if i[7] not in gen_dict:
            gen_dict.update({i[7]:0})
    for i in city_file [0:]:
        if i[7] in gen_dict :
            gen_dict[i[7]] +=1
    print ("Counts of each gender : ",gen_dict)

def birth_years(city_file):
    '''Calculate and returns the count of earliest, most recent, and most popular birth years for particular city
    Args:
        filtered csv input as per user filter choice
    Returns:
        (dict) returns the count of earliest, most recent, and most popular birth years users
        Null if there is no data for birth years
    Question: What are the earliest, most recent, and most popular birth years?
    '''
    # TODO: complete function
    birth_dict=dict()
    i=dict()
    try :

        if (len(city_file[0][8])) > 1:
            lambda x: x
    except (IndexError):
        print("Counts of BirthYears :Null")
        return
    for i in city_file [0:]:
        if i[8] not in birth_dict and i[8] != '':
            a,b=i[8].split(".")
            birth_dict.update({a:0})
    for i in city_file [0:]:
        if i[8] != '' :
            a,b=i[8].split(".")
            if a in birth_dict :
                birth_dict[a] +=1
    print ("Most earliest birth year : " ,min(birth_dict.items(), key= lambda x: x[0]))
    print ("Most recent birth year : " ,max(birth_dict.items(), key= lambda x: x[0]))
    print ("Most Popular birth year : " ,max(birth_dict.items(), key= lambda x: x[1]))

def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        (list) returns five lines and keep adding five more data if user specifies yes
    '''
    display = input('Would you like to view individual trip data?'
                    'Type \'yes\' or \'no\'. ')
    # TODO: handle raw input and complete function
    start_line=0
    end_line=5
    while display == "yes" :
        print(city_file[start_line:end_line])
        pprint.isreadable(city_file[start_line:end_line])
        if (input('Would you like to view individual trip data?'
                        'Type \'yes\' or \'no\'. ') =='yes'):
            start_line+=5
            end_line+=5
            continue
        return
    else :
        return

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city_file = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    #print (time_period)
    filtered_csv_reader = []
    if time_period == 'month':
        filter_month_number = get_month()
        for i in city_file [1:]:
            if datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").strftime('%m') == filter_month_number:
                filtered_csv_reader.append(i)
    elif time_period == 'day':
        filter_day = get_day()
        #print (filter_day)
        for i in city_file [1:]:
            if datetime.datetime.strptime(i[1],"%Y-%m-%d %H:%M:%S").strftime('%d') == filter_day:
                filtered_csv_reader.append(i)
    else :
        for i in city_file [1:]:
            filtered_csv_reader.append(i)


    print('Calculating the first statistic...')
    start_time = time.time()

    # What is the most popular month for start time?
    if time_period == 'none':
        # TODO: call popular_month function and print the results
        popular_month(filtered_csv_reader)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        # TODO: call popular_day function and print the results
        popular_day(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_day function and print the results
    popular_hour(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest, most recent, and most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(filtered_csv_reader)
    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(filtered_csv_reader)

    # Restart?
    restart = input('Would you like to restart? Type \'yes\' or \'no\'.')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
