import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    # Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Available Cities: ', [*CITY_DATA])

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        v_city = input('Enter one of the following city chicago, new york city and washington ')
        if v_city not in CITY_DATA:
            v_city = input('enter only three cities mentioned above ')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january','february','march','april','may','june','all'}
    while True:
        v_month = input('What month would you like to check? Enter All to view all data available ')
        if v_month not in MONTH_DATA:
            v_month = input('enter january to june or all ')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = {'monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'}
    while True:
        v_day = input('What day? Enter monday, tuesday etc ')
        if v_day not in DAY_DATA:
            v_day = input('enter valid day only or all')
            continue
        else:
            break

    print('-'*40)
    return v_city, v_month, v_day

#get_filters()

def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #lst= [city,month,day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['pop_month'] = df['Start Time'].dt.month
    common_month = df['pop_month'].mode()[0]
    print('Most Common Month:', common_month)

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['pop_day'] = df['Start Time'].dt.day
    common_day = df['pop_day'].mode()[0]
    print('Most Common Day:', common_day)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['pop_hour'] = df['Start Time'].dt.hour
    common_hour = df['pop_hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    df['pop_start_station'] = df['Start Station'].mode()[0]
    common_start_station = df['pop_start_station'].mode()[0]
    print('Most Start Station:', common_start_station)

    # display most commonly used end station
    df['pop_end_station'] = df['End Station'].mode()[0]
    common_end_station = df['pop_end_station'].mode()[0]
    print('Most End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    df['frequent_combination'] = df['Start Station'] + " " + df['End Station']
    print('Most frequent combination of start station and end station trip is:', df['frequent_combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['bike_duration'] = df['Trip Duration'].sum()
    total_bike_duration = df['bike_duration'].sum()
    print('Total Travel Time:', total_bike_duration)

    # display mean travel time
    df['bike_duration'] = df['Trip Duration'].mean()
    avrg_bike_duration = df['bike_duration'].mean()
    print('Average Travel Time:', avrg_bike_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df['user_type'] = df['User Type'].value_counts()
    user_type = df['User Type'].value_counts()
    print('User Type:',user_type)

    # Display counts of gender
    if city != 'washington':
            gender = df['Gender'].value_counts()
            print('Gender:', gender)
        # Display earliest, most recent, and most common year of birth
            df['birth_y'] = df['Birth Year'].mode()
            most_common_year = int(df['Birth Year'].mode()[0])
            print('Most Common Year:', most_common_year)
            most_recent_year = int(df['Birth Year'].max())
            print('Most Recent Year:', most_recent_year)
            earliest_year = int(df['Birth Year'].min())
            print('Earliest Year:', earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
        city,month,day = get_filters()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        raw_display = input('\nWould you like to see the raw data? Enter yes or no.\n')
        if raw_display.lower() == 'yes':
            print(df.head())


if __name__ == "__main__":
    main()