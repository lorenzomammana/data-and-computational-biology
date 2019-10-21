import numpy as np
import matplotlib.pyplot as plt
import sys


def compute_j():
    for i in range(0, len(a) + 1):
        if np.sum(a[0:i]) >= r2 * a0:
            return i - 1


if __name__ == '__main__':
    type = sys.argv[1]
    numsim = int(sys.argv[2])
    inittime = int(sys.argv[3])
    steps = int(sys.argv[4])

    if type == "bistable":
        k = [3 * 10e-7, 10e-4, 10e-3, 3.5]
        labels = ['A', 'B', 'X']
        X0 = np.array([10e5, 2 * 10e5, 250])

        beta = np.array([
            [-1, 0, 1],
            [1, 0, -1],
            [0, -1, 1],
            [0, 1, -1]
        ])
    else:
        k = [1.1, 0.1, 0.8]
        labels = ['S', 'E', 'C', 'P']
        X0 = np.array([100, 100, 1, 1])
        t = [0]

        beta = np.array([
            [-1, -1, 1, 0],
            [1, 1, -1, 0],
            [0, 1, -1, 1]])

    for sim in range(0, 100):
        print("Simulation: " + str(sim))
        t = [0]
        x = X0.copy()
        record_x = x.copy()
        for i in range(0, steps):

            if type == "bistable":
                a = [[(k[0] / 2) * x[0] * x[2] * (x[2] - 1)],
                     [(k[1] / 6) * x[2] * (x[2] - 1) * (x[2] - 2)],
                     [k[2] * x[1]],
                     [k[3] * x[2]]]
            else:
                a = [[k[0] * x[0] * x[1]],
                     [k[1] * x[2]],
                     [k[2] * x[2]]]

            a0 = np.sum(a)

            if a0 == 0:
                break

            r1 = np.random.uniform()
            r2 = np.random.uniform()

            tau = (1 / a0) * np.log(1 / r1)
            j = compute_j()

            x = x + beta[j]
            record_x = np.vstack((record_x, x))
            t.append(t[-1] + tau)

        colors = ['b', 'g', 'r', 'y']
        for i in range(0, len(X0)):
            plt.plot(t, record_x[:, i], colors[i])

    plt.ylabel('# of molecules')
    plt.xlabel('time')
    plt.legend(labels, loc='center right')
    plt.show()
