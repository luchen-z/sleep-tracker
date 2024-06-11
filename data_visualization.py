import json
import matplotlib.pyplot as plt
import pandas as pd

from data_storage import read_json_file


# filepath = 'data_store/sleep_data/Luchen.json'
#
# with open(filepath) as fp:
#     data_loaded = json.load(fp)
#     print(data_loaded)

data_loaded = read_json_file()

# Convert data to DataFrame
df = pd.DataFrame([
    [date, entry[0], entry[1], entry[2], entry[3]]
    for user in data_loaded.keys()
    for date, entries in data_loaded[user].items()
    for entry in entries
], columns=['date', 'start_time', 'end_time', 'duration', 'quality'])

# Convert date and time strings to datetime objects
df['date'] = pd.to_datetime(df['date'])
df['start_time'] = pd.to_datetime(df['start_time'], format='%H:%M').dt.time
df['end_time'] = pd.to_datetime(df['end_time'], format='%H:%M').dt.time

# Helper function to convert time to hours
def time_to_hours(t):
    return t.hour + t.minute / 60

df['start_hour'] = df['start_time'].apply(time_to_hours)
df['end_hour'] = df['end_time'].apply(time_to_hours)

# Define colors based on quality
quality_colors = {
    'rested': 'mediumseagreen',
    'okay': 'yellowgreen',
    'tired': 'honeydew'
}

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
for idx, row in df.iterrows():
    ax.bar(row['date'], row['end_hour'] - row['start_hour'], bottom=row['start_hour'],
           color=quality_colors[row['quality']], edgecolor='black')

# Formatting the plot
ax.set_ylim(24, 0)
ax.set_ylabel('Time (hour)')
ax.set_xlabel('Date')
ax.set_title('Sleep Records')

ax.set_yticks(range(25))
ax.set_yticklabels(range(25))

# Adding a legend
handles = [plt.Line2D([0], [0], color=color, lw=2) for color in quality_colors.values()]
labels = quality_colors.keys()
ax.legend(handles, labels, title='Quality')

plt.show()