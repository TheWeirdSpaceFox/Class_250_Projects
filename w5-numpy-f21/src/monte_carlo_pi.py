"""
Practice File input and plotting using Matplot lib
@author <your name here>
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import random

#https://docs.python.org/3/library/random.html
#random.seed(a=12, version=2) # Set seed to value to force same samples
                              # Normally use system clock as randomizer
x_rand = []
for i in range(10):
    x_rand.append(random.uniform(-1.0, 1.0))

print(x_rand)

#np.random.seed(12)
x_np = np.random.uniform(-1.0, 1.0, 25)
print(x_np)


def sample_xy(n=1e5):
    """
    Generate numpy array for x,y coordinates
    :param n: number of samples
    :return: x,y values
    """
    x = np.random.uniform(-1.0, 1.0, n)
    y = np.random.uniform(-1.0, 1.0, n)
    return x, y


def approx_pi(n):
    """
    Approximate pi using n samples in a square and inscribed unit circle.
    :param n:
    :return:
    """
    x, y = sample_xy(n)
    r = np.sqrt(x * x + y * y)
    rc = r <= 1.0
    number_circles = np.sum(rc)

    return 4.0 * number_circles / n


if __name__ == '__main__':

    fig = plt.figure()
    plt.plot([-1, 1, 1, -1, -1], [1, 1, -1, -1, 1], 'k')

    # How do we plot a circle
    print(" TO DO: Plot a circle")

    plt.axis([-1, 1, -1, 1])
    plt.axis('equal')
    plt.grid(True)
    plt.xticks([-1., -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0])
    plt.yticks([-1., -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0])
    fig.savefig(os.path.join("data", "circle_in_square.png"))


    x, y = sample_xy(10)

    r = np.sqrt(x*x + y*y)

    for i in range(len(x)):
        print("{: 7.4f}, {: 7.4f} r={:6.4f}".format(x[i], y[i], r[i]))

    rc = r < 1.0
    print("r <1.0 = ", r[rc])
    print("r>=1.0 = ", r[~rc])

    x, y = sample_xy(10)
    r = np.sqrt(x * x + y * y)
    rc = r < 1.0

    plt.plot(x[rc], y[rc], 'g.')
    plt.plot(x[~rc], y[~rc], 'r.')
    plt.title("Monte-Carlo Pi with N={}".format(len(x)))
    fig.savefig(os.path.join("data", "circle_monte_carlo_{}.png".format(len(x))))

    pi_a = approx_pi(10)
    print(" approximate pi = ", pi_a)

    n_range = np.logspace(4, 6, 100, dtype='int')
    pi_values = list(n_range)
    for i, n in enumerate(n_range):
        pi_values[i] = approx_pi(n)

    fig = plt.figure()
    plt.plot([0, max(n_range)], [np.pi, np.pi], 'g:')
    plt.plot(n_range, pi_values, 'r.')
    plt.grid(True)
    plt.title("Monte-Carlo Approximation of pi")
    fig.savefig(os.path.join("data", "pi_approx_{}_{}.png".format(min(n_range), max(n_range))))
