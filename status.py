import time

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Overall Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    if month == 'all':
        print('Most Popular Month: ', df['month'].mode()[0])

    # display the most common day of week
    if day == 'all':
        print('Most Popular Week Day: ', df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most Popular Start Hour: ', df['hour'].mode()[0])


    print("\nThis Operation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most Popular Start Station:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('Most Popular End Station:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station'])
    combination = combination.size().sort_values(ascending = False).head(1)
    print("Most Popular Combination: \n", combination)
    
    print("\nThis Operation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total Travel Time: ", total_time)
    

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print("Average Travel Time: ", avg_time)

    print("\nThis Operation took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types[:2])

    # Display counts of gender
    if city != 'wdc':
        gender = df['Gender'].value_counts()
        print(gender[:2])
    
    # Display earliest, most recent, and most common year of birth
    if city != 'wdc':
        print("Earliest Year of Birth: ", df['Birth Year'].min())
        print("Most Recent Year of Birth: ", df['Birth Year'].max())
        print("Most Common Year of Birth: ", df['Birth Year'].mode()[0])


    print("\nThis Operation took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays Five Rows from the Filtered Datasheet Continually if the User Wishes to..."""
    start_loc = 0
    print("\nFull Schedule Length: ", len(df))
    while True:
        try:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
            if (view_data[0] == 'y') or (view_data[0] == 'n'):
                break
            else:
                print("oops, type error! Please try again :)")
        except:
            print("oops, something went wrong! Please try again :)")
            
            
    while (view_data[0] == 'y' and (start_loc+5) <= len(df)):
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        if start_loc+5 <= len(df):
            while True:
                try:
                    view_data = input("Do you wish to continue?:").lower()
                    if (view_data[0] == 'y') or (view_data[0] == 'n'):
                        break
                    else:
                        print("oops, type error! Please try again :)")
                except:
                    print("oops, something went wrong! Please try again :)")
            
    print("Nothing more left to show!\n")
    
def summary(df, city, month, day):
    """Generates all the Functions of this Module"""
    time_stats(df, month, day)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df, city)
    display_data(df)