import mne
import os

# REPLACE THIS with the exact name of the file you downloaded
file_name = "S001R01.edf" 

# 1. Load the data
# preload=True loads the data into your computer's memory (RAM)
raw = mne.io.read_raw_edf(file_name, preload=True)

# 2. Print basic info (Number of channels, sample rate, etc.)
print(raw)
print(raw.info)

# 3. Visualize the raw signals
# This opens an interactive window where you can scroll through the data
raw.plot()
