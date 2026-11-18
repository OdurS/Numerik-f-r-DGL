import numpy as np

def explicit_euler(f, y_0, T, tau):

    K = int(round(T / tau))

    Y = np.zeros((len(y_0), K + 1))
    Y[:, 0] = y_0

    for k in range(K):

        t = k * tau
        y = Y[:, k]

        Y[:, k + 1] = y + tau * f(t, y)

    return Y



def explicit_heun(f, y_0, T, tau):

    K = int(round(T / tau))

    Y = np.zeros((len(y_0), K + 1))
    Y[:, 0] = y_0

    for k in range(K):

        t = k * tau
        y = Y[:, k]

        k1 = f(t, y)

        k2 = f(t + tau, y + tau * k1)

        Y[:, k + 1] = y + tau / 2 * (k1 + k2)

    return Y



def explicit_runge_kutta3(f, y_0, T, tau):

    K = int(round(T / tau))

    Y = np.zeros((len(y_0), K + 1))
    Y[:, 0] = y_0

    for k in range(K):

        t = k * tau
        y = Y[:, k]

        k1 = f(t, y)

        k2 = f(t + tau / 2, y + tau / 2 * k1)

        k3 = f(t + tau, y + tau * (-k1 + 2 * k2))

        Y[:, k + 1] = y + tau / 6 * (k1 + 4 * k2 + k3)

    return Y