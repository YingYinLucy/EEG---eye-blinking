#import matplotlib
# Force Python to use the standard "Tcl/Tk" window system
#atplotlib.use('TkAgg')

#import mne
#import matplotlib.pyplot as plt


#aw = mne.io.read_raw_edf("S001R01 (1).edf", preload=True)

#data, times= raw.get_data(return_times=True)

#plt.plot(times[:5000], data[0][:5000])
#plt.show()


import matplotlib
import mne
import matplotlib.pyplot as plt
raw = mne.io.read_raw_edf("S001R01 (1).edf", preload=True)

# Try one of these:
matplotlib.use('TkAgg')  # or 'Qt5Agg', 'WebAgg', etc.
# matplotlib.use('Agg')  # This is non-interactive - won't show plots!

raw = mne.io.read_raw_edf("S001R01 (1).edf", preload=True)
data, times = raw.get_data(return_times=True)

plt.plot(times[:5000], data[0][:5000])
plt.show()

# 1. Create the plot
#raw.plot(block=True)

# 2. Force the window to show (sometimes needed)
#plt.show()

# 3. Keep the script alive

#input("Press Enter to close the plot...")