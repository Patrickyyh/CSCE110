import  numpy as np
import matplotlib.pyplot as plt

# Unique identifiers for each figure
FIGURE1 = 1
FIGURE2 = 2

#Wave parameter
FREQUENCY  =  3
SAMPLE_RATE = 100
TIME_STEM =1.0 / SAMPLE_RATE

# Like range() for floating point
t1 = np.arange(0.0,5.0 ,TIME_STEM)
print(t1)

# Compute a sine wave
wave = np.sin(FREQUENCY * 2 * np.pi * t1)

#Compute Fast Fourier Transform
fft_result = np.fft.fft(wave)

#Compute x-axis values for frequency domain
t2 = np.fft.fftfreq(len(t1), TIME_STEM)




##   The plt.axis() function is used to set the range of the x and y axes.
plt.figure(FIGURE1)
plt.plot(t1, wave)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

## 对某一个部分进行缩放?
plt.axis([-1,6,-1.2,1.2])


plt.figure(FIGURE2)
plt.plot(t2 , np.abs(fft_result))
plt.xlabel("Frequencey (HZ)")
plt.ylabel("Magnitude")
plt.axis([-5,5, 0 ,260])
## set plot axis ranges (set some space buffer)

plt.show()




