import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
#%% Load the CSV file
file_path = 'D:/GitHub/CFD_test/CFD_data/test_original_v2.csv'
try:
    data = pd.read_csv(file_path)
except UnicodeDecodeError:
    data = pd.read_csv(file_path, encoding='latin1')

#%% Extract and convert 'Time' column to datetime
data['Time'] = pd.to_datetime(data['Time'], format='%I:%M:%S %p', errors='coerce')

#%% Add a day shift when the time resets (detecting time going backward)
day_shift = np.zeros(len(data), dtype=int)
for i in range(1, len(data)):
    if data['Time'].iloc[i] < data['Time'].iloc[i - 1]:
        day_shift[i:] += 1

#%% Set the base date for the timestamps
base_date = pd.Timestamp('2024-04-11')

#%% Adjust the datetime by adding the base date and the computed day shifts
data['Adjusted Time'] = data['Time'].apply(lambda x: pd.Timestamp.combine(base_date, x.time())) + pd.to_timedelta(day_shift, unit='d')







#%% Plotting temps for each tree
for tree_number in range(1, 6):
    plt.figure(figsize=(12, 6))
    for i in range(1, 6):
        plt.plot(data['Adjusted Time'], data[f'T_{tree_number}_{i}'], label=f'T_{tree_number}_{i}')
    
    # Add a vertical line and annotations for day change
    day_change = data['Adjusted Time'].dt.date.shift(1, fill_value=data['Adjusted Time'].dt.date.iloc[0]) != data['Adjusted Time'].dt.date
    day_change_idx = day_change[day_change].index.min()
    if not pd.isna(day_change_idx):
        transition_time = data['Adjusted Time'].iloc[day_change_idx]
        plt.axvline(x=transition_time, color='r', linestyle='--', linewidth=2)
        plt.annotate(f'April 11', (transition_time, plt.ylim()[1]), textcoords="offset points", xytext=(-40,-16), ha='right', fontsize=20)
        plt.annotate(f'April 12', (transition_time, plt.ylim()[1]), textcoords="offset points", xytext=(40,-16), ha='left', fontsize=20)
    
    # Format the x-axis
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    
    plt.xlabel('Time')
    plt.ylabel('Temperature [C]')
    plt.title(f'Tree {tree_number} Temperatures')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the figure
    file_path = f'D:/GitHub/CFD_test/CFD_data/Tree{tree_number}_temp.png'
    plt.savefig(file_path, dpi=300)
#%% Plot temp for all the walls
# Names and labels for wall and floor/ceiling temperatures
temperature_columns = ['T_N', 'T_S', 'T_E', 'T_W', 'T_bot', 'T_top']
labels = ['North Wall', 'South Wall', 'East Wall', 'West Wall', 'Floor', 'Ceiling']

plt.figure(figsize=(12, 6))
for column, label in zip(temperature_columns, labels):
    plt.plot(data['Adjusted Time'], data[column], label=label)

# Add a vertical line and annotations for day change
day_change = data['Adjusted Time'].dt.date.shift(1, fill_value=data['Adjusted Time'].dt.date.iloc[0]) != data['Adjusted Time'].dt.date
day_change_idx = day_change[day_change].index.min()
if not pd.isna(day_change_idx):
    transition_time = data['Adjusted Time'].iloc[day_change_idx]
    plt.axvline(x=transition_time, color='r', linestyle='--', linewidth=2)
    plt.annotate('April 11', (transition_time, plt.ylim()[1]), textcoords="offset points", xytext=(-40,-16), ha='right', fontsize=20)
    plt.annotate('April 12', (transition_time, plt.ylim()[1]), textcoords="offset points", xytext=(40,-16), ha='left', fontsize=20)

# Format the x-axis
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.xlabel('Time')
plt.ylabel('Temperature [C]')
plt.title('Wall, Floor, and Ceiling Temperatures')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
file_path = 'D:/GitHub/CFD_test/CFD_data/Walls_temp.png'
plt.savefig(file_path, dpi=300)

#%% Plot temperatures at each level for each tree
for level in range(1, 6):
    plt.figure(figsize=(12, 6))
    for tree_number in range(1, 6):
        column_name = f'T_{tree_number}_{level}'
        plt.plot(data['Adjusted Time'], data[column_name], label=f'Tree {tree_number}')

    # Add a vertical line and annotations for day change
    day_change = data['Adjusted Time'].dt.date.shift(1, fill_value=data['Adjusted Time'].dt.date.iloc[0]) != data['Adjusted Time'].dt.date
    day_change_idx = day_change[day_change].index.min()
    if not pd.isna(day_change_idx):
        transition_time = data['Adjusted Time'].iloc[day_change_idx]
        plt.axvline(x=transition_time, color='r', linestyle='--', linewidth=2)
        plt.annotate('April 11', (transition_time, plt.ylim()[1]), textcoords="offset points", xytext=(-40,-16), ha='right', fontsize=20)
        plt.annotate('April 12', (transition_time, plt.ylim()[1]), textcoords="offset points", xytext=(40,-16), ha='left', fontsize=20)

    # Format the x-axis
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(12))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.xlabel('Time')
    plt.ylabel('Temperature [C]')
    plt.title(f'Temperatures at Level {level} across Trees')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the figure
    file_path = f'D:/GitHub/CFD_test/CFD_data/Temperatures_Level_{level}_Trees.png'
    plt.savefig(file_path, dpi=300)

#%% Contour plot for temp at chest level
# Select the specific rows from 485 to 540 with a step of 5
rows_of_interest = np.arange(485, 541, 5)
selected_data = data.iloc[rows_of_interest]

# Prepare the x, y, and temperature data for contour plotting
x = np.array([0, 1, 2])
y = np.array([0, 1, 2])
X, Y = np.meshgrid(x, y)

# Create a figure with multiple subplots
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))  # Adjust the size as needed
fig.suptitle('Temperature Contour at Chest Level', fontsize=16)

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Temperature extraction and plotting
for i, ax in enumerate(axes):
    if i < len(rows_of_interest):
        # Each matrix cell corresponds to a specific temperature source at level 3
        # Define the 3x3 matrix layout based on the provided structure
        temperature_matrix = np.array([
            [selected_data['T_2_3'].iloc[i], selected_data['T_N'].iloc[i], selected_data['T_1_3'].iloc[i]],
            [selected_data['T_W'].iloc[i], selected_data['T_5_3'].iloc[i], selected_data['T_E'].iloc[i]],
            [selected_data['T_4_3'].iloc[i], selected_data['T_S'].iloc[i], selected_data['T_3_3'].iloc[i]]
        ])

        # Plot contour
        contour = ax.contourf(X, Y, temperature_matrix, cmap='viridis', levels=100)
        # Use the adjusted time for titles
        ax.set_title(f'Time: {selected_data["Adjusted Time"].iloc[i].strftime("%Y-%m-%d %H:%M:%S")}', fontsize=10)
        ax.set_xticks(x)
        ax.set_yticks(y)
        ax.set_xticklabels(['', 'South', ''])
        ax.set_yticklabels(['', 'West', ''])
        ax.grid(True)
    else:
        ax.axis('off')  # Turn off axis for any unused subplot

# Add a color bar
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust the layout to make room for the title

cbar = fig.colorbar(contour,
                    ax=axes.ravel().tolist(),
                    orientation='horizontal', 
                    fraction=0.015,
                    pad=0.1, 
                    aspect=50)
cbar.set_label('Temperature [C]', fontsize=14)
# save figure
file_path = 'D:/GitHub/CFD_test/CFD_data/Tempe_contour_chest Level.png'
plt.savefig(file_path)