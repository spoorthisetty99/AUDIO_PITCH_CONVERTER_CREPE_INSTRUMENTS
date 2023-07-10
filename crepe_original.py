import crepe
from scipy.io import wavfile
from os.path import expanduser
import numpy as np
import librosa
import matplotlib.pyplot as plt

# Load the audio file
sr, audio = wavfile.read(expanduser('Flute_song_R.wav'))

# Use Crepe to predict the pitch
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)

# Save the pitch values to a CSV file
data = np.column_stack((time, frequency, confidence))
np.savetxt(expanduser('~/violin-A-pluck.f0-python.csv'), data,
           ['%.3f', '%.3f', '%.6f'],
           header='time,frequency,confidence', delimiter=',')

# Convert frequency values to pitch values
pitches = librosa.hz_to_note(frequency, cents=False)
print(pitches)
# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(time, pitches, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Pitch')
plt.title('Pitch over Time')
plt.grid(True)

plt.show()

