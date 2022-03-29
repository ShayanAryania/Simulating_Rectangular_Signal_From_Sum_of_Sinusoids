#Simulating Rectangular Signal From Sum of Sinusoids
#ShayanAryania

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

#Time Domain
Time = np.arange(-1 * np.pi , 1 * np.pi, 0.01)
S = 0 

#Sinusoids From 0Hz To N Hz
for i in range (0,100) : 
    Frequency = (2 * i) + 1
    S += np.sin( Frequency * np.pi * Time ) / Frequency

#Plotting
f, ax = plt.subplots(figsize=(10,5))
ax.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))

ax.xaxis.set_major_locator(tck.MultipleLocator(base=1.0))
ax.plot(Time, 0.78 * signal.square(np.pi * Time), "Red")
ax.plot(Time ,S)

plt.show()