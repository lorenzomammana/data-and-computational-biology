import numpy as np
import matplotlib.pyplot as plt


def compute_j():
    for i in range(0, len(a) + 1):
        if np.sum(a[0:i]) >= r2 * a0:
            return i - 1


if __name__ == '__main__':

    k = [1.1, 0.1, 0.8]
    labels = ['S', 'E', 'C', 'P']
    X0 = np.array([100, 100, 1, 1])
    t = [0]

    beta = np.array([
        [-1, -1, 1, 0],
        [1, 1, -1, 0],
        [0, 1, -1, 1]])

    x = X0.copy()
    record_x = x.copy()

    for i in range(0, 2000):
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

    for i in range(0, len(X0)):
        plt.plot(t, record_x[:, i])

    plt.legend(labels, loc='center right')
    plt.show()
