import numpy as np
import matplotlib.pyplot as plt
import sys

ARRAY_SIZE = int(sys.argv[1])
np.set_printoptions(precision=3, suppress=True)
plt.rcParams['toolbar'] = 'None'

plt.ion()
fig = plt.figure()
fig.canvas.manager.set_window_title('Insert Sort')
ax = fig.add_subplot(111)

num_array = np.random.rand(ARRAY_SIZE)
len_array = np.arange(ARRAY_SIZE)
line, = ax.plot(len_array, num_array, '-r')

print("Initial array:")
print(num_array)

for i in range(len(num_array)):
    j = i
    while j >= 0:
        if num_array[i] < num_array[j]:
            temp = num_array[i]
            num_array[i] = num_array[j]
            num_array[j] = temp
            i -= 1
        j -= 1
    line.set_ydata(num_array)
    fig.canvas.draw()
    fig.canvas.flush_events()

print("\nSorted array:")
print(num_array,"\n")

while True:
    fig.canvas.flush_events()
    fig.canvas.mpl_connect('close_event', sys.exit)
