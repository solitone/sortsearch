# Credits: Najam R Syed
# for explaining how to use matplotlib.animation to visualise data:
# https://nrsyed.com/2018/09/27/visualizing-sorting-algorithms-and-time-complexity-with-matplotlib/
# https://github.com/nrsyed/sorts

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sort import exchangesort, selectionsort, bubblesort, quicksort, mergesort, insertionsort
from util import merge


# Get user input to determine range of integers (1 to N) and desired
# sorting method (algorithm).
N = int(input("Enter number of integers: "))
method_msg = "Enter sorting method:\n(b)ubble\n(e)xchange\n(i)nsertion \
              \n(m)erge\n(q)uick\n(s)election:\n"
method = input(method_msg)

# Build and randomly shuffle list of integers.
l = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(l)

# Get appropriate generator to supply to matplotlib FuncAnimation method.
if method == "b":
    title = "Bubble sort"
    generator = bubblesort(l)
elif method == "e":
    title = "Exchange sort"
    generator = exchangesort(l)
elif method == "i":
    title = "Insertion sort"
    generator = insertionsort(l)
elif method == "m":
    title = "Merge sort"
    generator = mergesort(l, 0, N - 1)
elif method == "q":
    title = "Quick sort"
    generator = quicksort(l, 0, N - 1)
elif method == "s":
    title = "Selection sort"
    generator = selectionsort(l)
else:
    print("Invalid input.")
    exit()

## Visualise list while being sorted

# Initialize figure and axis.
fig, ax = plt.subplots() # returns a figure and an axes object
ax.set_title(title)

colormap = plt.cm.get_cmap('cool')
# Needed for 1st frame
color_nums = [x / max(l) for x in l]
colors = colormap(color_nums)
# Needed for later frames
orderd_color_nums = [(x + 1)/N for x in range(N)]
orderd_colors = colormap(orderd_color_nums)

# Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
# list of rectangles (with each bar in the bar plot corresponding
# to one rectangle), which we store in bar_rects.
bar_rects = ax.bar(range(len(l)), l, width=0.9, align="edge", color=colors)

# Set axis limits. Set y axis upper limit high enough that the tops of
# the bars won't overlap with the text label.
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.12 * N))

# Place two text labels in the upper-left corner of the plot to display
# number of comparisons and swaps performed by the sorting algorithm
labelCompars = ax.text(0.02, 0.95, "", transform=ax.transAxes)
labelSwaps = ax.text(0.02, 0.90, "", transform=ax.transAxes)

# Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
def update_fig(count_tuple, list, rects):
    maxval = max(list)
    for rect, val in zip(rects, list):
        rect.set_height(val)
        rect.set_color(orderd_colors[val-1])
        rect.set_edgecolor(None)
    labelCompars.set_text("# of comparisons: {}".format(count_tuple[0]))
    labelSwaps.set_text("# of swaps: {}".format(count_tuple[1]))

_ = animation.FuncAnimation(fig, func=update_fig,
    fargs=(l, bar_rects), frames=generator, interval=1,
    repeat=False)
plt.show()
