import numpy as np
import matplotlib.pyplot as plt
from Aufgabe1 import Aufgabe1_Standart as a1
def predator_prey(t, Y):

    x, y = Y

    dx = x - x * y
    dy = x * y - y

    return np.array([dx, dy])


y_0 = np.array([0.5, 0.5])

T = 20

taus = [0.64, 0.32, 0.16, 0.08, 0.04]


methods = {
    "Euler": a1.explicit_euler,
    "Heun": a1.explicit_heun,
    "Runge-Kutta 3": a1.explicit_runge_kutta3
}

def aufgabe_2_a():
    x_values = np.linspace(0, 3, 20)
    y_values = np.linspace(0, 3, 20)

    X, Y = np.meshgrid(x_values, y_values)

    U = X - X * Y
    V = X * Y - Y



    for name, method in methods.items():
        plt.figure(figsize=(8, 6))

        plt.quiver(X, Y, U, V, alpha=0.4)

        for tau in taus:

            solution = method(predator_prey, y_0, T, tau)

            plt.plot(
                solution[0, :],
                solution[1, :],
                label=f"tau = {tau}"
            )

        plt.xlabel("Beutepopulation x(t)")
        plt.ylabel("Räuberpopulation y(t)")

        plt.title(f"Phasendiagramm – {name}")

        plt.xlim(0, 3)
        plt.ylim(0, 3)

        plt.grid()
        plt.legend()

        plt.show()
        
def aufgabe_2_b():
    for name, method in methods.items():

        fig, axes = plt.subplots(2, 1, figsize=(10, 8))

        for tau in taus:

            solution = method(predator_prey, y_0, T, tau)

            K = solution.shape[1]

            t = np.linspace(0, T, K)

            axes[0].plot(t, solution[0, :], label=f"tau = {tau}")

            axes[1].plot(t, solution[1, :], label=f"tau = {tau}")

    axes[0].set_title(f"Beutepopulation – {name}")
    axes[0].set_ylabel("Beutepopulation")
    axes[0].set_xlabel("Zeit")

    axes[1].set_title(f"Räuberpopulation – {name}")
    axes[1].set_ylabel("Räuberpopulation")
    axes[1].set_xlabel("Zeit")

    axes[0].legend()
    axes[1].legend()

    axes[0].grid()
    axes[1].grid()

    plt.tight_layout()
    plt.show()