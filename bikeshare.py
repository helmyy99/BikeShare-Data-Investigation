"""
Student: Mostafa Mohamed Helmy
E-Mail Adress: mostafahelmy129@hotmail.com
Project: Explore US BikeShare Data
Date: 21/7/2021

.............................................

Program Description:
    A Bike Share System Data Analyser, provided by Motivate
    Start by choosing any city file (or all if you wish)
    
    There are two built modules:
        filter_data ---> filter the data according to user needs
        status_data ---> show the descriptive statistics of the data
    
"""




"""Importing The Program Modules"""
import filters as fs #module for data filtration
import status as stats #module for data description

def main():
    while True:
        city, month, day = fs.get_filters()
        if city != 'all':
            print("Showing The Data in {}:".format(city))
            df = fs.load_data(city, month, day)
            stats.summary(df, city, month, day)
        else:
            for CITY in fs.CITY_DATA:
                city = CITY
                print("Showing The Data in {}:".format(city))
                df = fs.load_data(city, month, day)
                stats.summary(df, city, month, day)    
        
        restart = input('\nWould you like to restart? Enter yes or y to continue.\n')
        if restart.lower()[0] != 'y':
            break

if __name__ == "__main__":
	main()