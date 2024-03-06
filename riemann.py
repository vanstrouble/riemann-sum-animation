import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim


# Function to calculate the integral of x^2
def f(x):
    return x**2


# Parameters
a = 0
b = 10
n_frames = 100

# Create figure and axes
fig, ax = plt.subplots(figsize=[10, 6], dpi=200)
plt.style.use("dark_background")

# Setting axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 120)


def animate(i):
    ax.clear()

    x = np.linspace(a, b, 100)
    y = f(x)
    ax.plot(x, y, color="crimson", linewidth=4)

    n_rectangles = 5 * (i + 1)
    delta_x = (b - a) / n_rectangles

    for j in range(n_rectangles):
        left = a + j * delta_x
        right = left + delta_x
        bottom = 0
        top = f(left)
        rect = plt.Rectangle((left, bottom), delta_x, top, color="deeppink", alpha=0.5)
        ax.add_patch(rect)

    ax.set_title(f"Riemann sums: {n_rectangles} rectangles", fontsize=25)


ani = anim.FuncAnimation(fig, animate, frames=n_frames, interval=100, repeat=False)
ani.save("riemann_sum.gif", writer="pillow")
plt.show()
