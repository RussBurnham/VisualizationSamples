from pathlib import Path
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

path = Path(os.path.join(os.environ["Weather_Data"], "phoenix_az_temp.csv"))
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract average temperatures.
dates, average = [], []
current_date = None
for row in reader:
    try:
        current_date = datetime.strptime(row[0], "%Y%m")
        averages = float(int(row[1]))
    except ValueError:
        print(f"Missing data for {current_date}.")
    else:
        dates.append(current_date)
        average.append(averages)

# Plot high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, average, color="blue", alpha=0.5)

# Format plot.
title = "Average Temperature(F) in Phoenix, AZ"
ax.set_title(title, fontsize=24)
ax.set_xlabel("Year", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
