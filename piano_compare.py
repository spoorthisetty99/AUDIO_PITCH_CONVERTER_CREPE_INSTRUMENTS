import numpy as np
from os.path import expanduser
import librosa
import matplotlib.pyplot as plt
from art import *

a = np.loadtxt(open(expanduser('song.f0.csv'), 'rb'), delimiter=',', skiprows=1)
b = np.loadtxt(open(expanduser('Flue_song_R_f0.csv'), 'rb'), delimiter=',', skiprows=1)

# Crop the files to the size of the smaller file
min_length = min(len(a), len(b))
a = a[:min_length, :]
b = b[:min_length, :]

difference = a - b
np.savetxt(expanduser('recorded_wrong.f0.csv'), difference, ['%.3f', '%.3f', '%.6f'], header='time,frequency,confidence', delimiter=',')

a_pitch = librosa.hz_to_note(a[:, 1], cents=False)  # Convert 'a' pitches to notes without cents
b_pitch = librosa.hz_to_note(b[:, 1], cents=False)  # Convert 'b' pitches to notes without cents

# Get the time intervals and frequency changes
time_intervals = a[:, 0]
frequency_changes = difference[:, 1]

# Find the indices where the frequency change is greater than 50
significant_changes = np.abs(frequency_changes) > 75

# Check if all values in 'difference' are zero
if np.all(difference[:, 1] == 0):
    tprint("Correct", font='bulbhead')
else:
    for i, is_significant in enumerate(significant_changes):
        if is_significant:
            time = time_intervals[i]
            change = frequency_changes[i]
            reference = a[i, 1]
            if change > 0:
                print("At time", time, "reduce freq by", change)
            else:
                print("At time", time, "increase freq by", abs(change))

# Plotting the graphs
fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True, gridspec_kw={'hspace': 0.5})

# Plot for 'a' pitch data
axs[0].plot(a[:, 0], a_pitch, color='blue')  # Plot 'a' pitches without cents
axs[0].set_title("Crepe Original")
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Pitch")

# Plot for 'b' pitch data
axs[1].plot(b[:, 0], b_pitch, color='red')  # Plot 'b' pitches without cents
axs[1].set_title("Pitch 'b'")
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Pitch")

# Plot for the difference between 'a' and 'b'
axs[2].plot(a[:, 0], difference[:, 1], color='green')
axs[2].set_title("Difference (a - b)")
axs[2].set_xlabel("Time (s)")
axs[2].set_ylabel("Frequency Difference (Hz)")

plt.tight_layout()
plt.show()

