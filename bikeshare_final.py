#Asha code edit for python
"""Exploring bike share project using Python learnt skills from Udacity"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
city = ('chicago', 'new_york_city', 'washington')

month = ('all', 'january', 'febuary', 'march', 'april', 'may', 'june')

day = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

    #print('Hello! Let\'s explore some US bikeshare data!')

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

print('Which city would you like to select: chicago, new_york_city, or washington')

while True:

    try:

        city in CITY_DATA

        city = input('Please Enter name of a city: ').lower()

        print('Awesome! Stay put! we are checking data for', city)

        break

    except KeyError:

        print('Sorry, We store  data only on chicago, new york city and washington')

# get user input for month (all, january, february, ... , june)

print('\nPlease let us know which month would you like to explore')

month = input('Enter month of the year: ').lower()

while True:

    print('\nAwesome! Stay put! we are checking data for', month)

    break

else:

    print('Sorry, please enter months; january to june or all')



# get user input for day of week (all, monday, tuesday, ... sunday)

print('\nPlease let us know which day of the week would you like to select')

day = input('\nEnter day of the week: ').lower()

print('\nAwesome! Stay put ! we are checking the week of the day for', day)

print('-'*40)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #Creating a panda dataframe to filter by Month and Day

import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


    # load data file into a dataframe
df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.day

    # filter by month if applicable
if month != 'all':

        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

#return df
#

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
df['month'] = df['Start Time'].dt.month

common_month = df['month'].mode()[0]
print('most common month:', common_month)

    # display the most common day of week
df['day_of_week'] = df['Start Time'].dt.day

common_week = df['day_of_week'].mode()[0]
print('most common week:', common_week)

    # display the most common start hour

df['hour'] = df['Start Time'].dt.hour

popular_hour = df['hour'].mode()[0]
print('most popular hour:', popular_hour)
#print("\nThis took %s seconds." % (time.time() - start_time))
#print('-'*40)

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

print('\nCalculating The Most Popular Stations and Trip...\n')

start_time = time.time()

# display most commonly used start station

common_start_station = df['Start Station'].mode()[0]

print('Most Commonly used start station: ', common_start_station)

# display most commonly used end station

common_end_station = df['End Station'].mode()[0]

print('Most commonly used end station: ', common_end_station)

# display most frequent combination of start station and end station trip

df['comb'] = df['Start Station'] + ' to ' + df['End Station']

common_combined = df['comb'].mode()[0]

print('Most frequent combination of start and end station: ', common_combined)

print("\nThis took %s seconds." % (time.time() - start_time))

print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

print('\nCalculating Trip Duration...\n')

start_time = time.time()

# display total travel time

trip_duration_time = df['Trip Duration'].sum()

print('Total trip duration: ', trip_duration_time)

# display mean travel time

mean_travel_time = df['Trip Duration'].mean()

print('Mean Travel time: ', mean_travel_time)

print("\nThis took %s seconds." % (time.time() - start_time))

print('-'*40)


def user_stats(df):

    """Displays statistics on bikeshare users."""

print('\nCalculating User Stats...\n')

start_time = time.time()

# Display counts of user types

user_types = df['User Type'].value_counts()

print('Counts of User Type: ', user_types)

# Display counts of gender

if 'Gender' in df:

    gender_count = df['Gender'].value_counts()

    print('Sum of  Gender count: ', gender_count)

else:

    print('Gender information is not available for this city')

# Display earliest, most recent, and most common year of birth

if 'Birth Year' in df:

    recent_birth_year = df['Birth Year'].max()

    print('Most recent birth year: ', recent_birth_year)

else:

    print('Birth year information is not available for this city')
if 'Birth Year' in df:

    common_birth_year = df['Birth Year'].mode()[0]

    print('Most common birth year: ', common_birth_year)

else:

    print('Birth year information is not availabe for this city')

print("\nThis took %s seconds." % (time.time() - start_time))

print('-'*40)

def main():
    while True:
        #city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
