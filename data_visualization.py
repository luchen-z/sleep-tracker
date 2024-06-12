import matplotlib.pyplot as plt
import pandas as pd
import os

from data_storage import read_json_file

data_loaded = read_json_file()

# Convert data to DataFrame
for user in data_loaded.keys():
    df = pd.DataFrame([
        [date, entry[0], entry[1], entry[2], entry[3]]
        for date, entries in data_loaded[user].items()
        for entry in entries
    ], columns=['date', 'start_time', 'end_time', 'duration', 'quality'])

    # Convert date and time strings to datetime objects
    df['date'] = pd.to_datetime(df['date'])
    df['start_time'] = pd.to_datetime(df['start_time'], format='%H:%M').dt.time
    df['end_time'] = pd.to_datetime(df['end_time'], format='%H:%M').dt.time

    # Extract month and day for separate columns
    df['month'] = df['date'].dt.strftime('%Y-%m')
    df['day'] = df['date'].dt.day

    # Group data by month
    grouped = df.groupby('month')

    # Helper function to convert time to hours
    def time_to_hours(t):
        return t.hour + t.minute / 60


    df['start_hour'] = df['start_time'].apply(time_to_hours)
    df['end_hour'] = df['end_time'].apply(time_to_hours)

    # Define colors based on quality
    quality_colors = {
        'rested': '#398564',
        'okay': '#47B649',
        'tired': '#A6DBBC'
    }

    # Plotting
    for month, month_df in grouped:
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot bars
        for idx, row in df.iterrows():
            ax.bar(row['day'], row['end_hour'] - row['start_hour'], bottom=row['start_hour'],
                   color=quality_colors[row['quality']], edgecolor='black')

        # Formatting the plot
        ax.set_ylim(24, 0)
        ax.set_xlim(1, month_df['day'].max() + 1)  # Set x-axis limits to the number of days in the month
        ax.set_ylabel('Time (hour)')
        ax.set_xlabel('Day')
        ax.set_title(f'Sleep Records for {user} in {month}')

        ax.set_yticks(range(25))
        ax.set_yticklabels(range(25))
        ax.set_xticks(range(month_df['day'].max() + 1))
        ax.set_xticklabels(range(month_df['day'].max() + 1))

        # Adding a legend
        handles = [plt.Line2D([0], [0], color=color, lw=3) for color in quality_colors.values()]
        labels = quality_colors.keys()
        ax.legend(handles, labels, title='Quality')

        plt.show()

        # Save the figure
        SLEEP_DATA_DIRECTORY = 'data_store/sleep_data'
        filename = f'sleep_patterns_{user}_{month}.png'
        plt.savefig(os.path.join(SLEEP_DATA_DIRECTORY, filename))
        plt.close()
