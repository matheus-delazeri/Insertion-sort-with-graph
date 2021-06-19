import numpy as np
import matplotlib.pyplot as plt
import sys

ARRAY_SIZE = int(sys.argv[1])
graph_on = True
if len(sys.argv) >= 3:
    graph_on = False if sys.argv[2]=='graph-off' else True
np.set_printoptions(precision=3, suppress=True)
plt.rcParams['toolbar'] = 'None'

num_array = np.random.rand(ARRAY_SIZE)
len_array = np.arange(ARRAY_SIZE)

if(graph_on):
    plt.ion()
    fig = plt.figure()
    fig.canvas.manager.set_window_title('Insert Sort')
    ax = fig.add_subplot(111)
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
    if(graph_on):
        line.set_ydata(num_array)
        fig.canvas.draw()
        fig.canvas.flush_events()

print("\nSorted array:")
print(num_array,"\n")

while graph_on:
    fig.canvas.flush_events()
    fig.canvas.mpl_connect('close_event', sys.exit)
