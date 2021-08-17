import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'wdc': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!\n")
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Choose City (chicago, nyc, wdc, or all!): ').lower()
            if city in CITY_DATA:
                print("Viewing {}'s data...\n".format(city.title()))
                break
            elif city == 'all':
                print("Viewing all cities' data...\n")
                break
            else:
                print("Oh seems that there is no such city, Please try again :)")
        except:
                print("oops, something went wrong! Please try again :)")
                continue

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Specify Month (type all if you need all months; also you can use the first 3 initials if you want): ').lower()
            for month_find in months:
                if month[:3] == month_find[:3]:
                    month = month_find
                    break
                else:
                    continue
            if month in months:
                print("Viewing {}'s data...\n".format(month.title()))
                break
            elif month == 'all':
                print("Viewing all months' data...\n")
                break
            else:
                print("Oh seems that there is no such month, Please try again :)")
        except:
                print("oops, something went wrong! Please try again :)")
                continue
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Specify Day (type all if you need all days; also you can use the first 3 initials if you want): ').lower()
            for day_find in days:
                if day[:3] == day_find[:3]:
                    day = day_find
                    break
                else:
                    continue
            if day in days:
                print("Viewing {}'s data...\n".format(day.title()))
                break
            elif day == 'all':
                print("Viewing all week days' data...\n")
                break
            
            else:
                print("Oh seems that there is no such day, Please try again :)")
        except:
                print("oops, something went wrong! Please try again :)")
                continue

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month.lower())+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df