
import numpy as np
import matplotlib.pyplot as plt
import time
from Aufgabe1 import Aufgabe1_Standart as a1 

def Aufgabe3():

    alpha = 10
    beta = 0.1

    y_0 = np.array([1.0])
    T = 1




    def logistic(t, y):
        return alpha * y * (1 - beta * y)



    def exact_solution(t):
        return (
            y_0[0] * np.exp(alpha * t)
            / (1 + beta * y_0[0] * (np.exp(alpha * t) - 1))
        )




    taus = [1 / 2**(i + 3) for i in range(9)]



    methods = {
        "Euler": a1.explicit_euler,
        "Heun": a1.explicit_heun,
        "Runge-Kutta 3": a1.explicit_runge_kutta3
    }




    errors = {name: [] for name in methods}
    times = {name: [] for name in methods}

    for name, method in methods.items():

        for tau in taus:

            start = time.perf_counter()

            solution = method(logistic, y_0, T, tau)

            cpu_time = time.perf_counter() - start

            K = solution.shape[1]

            # Numerische Zeitpunkte
            t_values = np.linspace(0, T, K)

            # Exakte Lösung an den Zeitpunkten
            exact_values = exact_solution(t_values)

            # Maximaler Fehler
            error = np.max(
                np.abs(solution[0, :] - exact_values)
            )

            errors[name].append(error)
            times[name].append(cpu_time)


    print("---Aufgabe3 a---")

    for name in methods:

        print("\n", name)

        for tau, error, cpu_time in zip(
            taus, errors[name], times[name]
        ):

            print(
                f"tau = {tau:.6f}, "
                f"Fehler = {error:.8e}, "
                f"Zeit = {cpu_time:.8e} s"
            )


    print("---Aufgabe3 b---")

    plt.figure(figsize=(9, 6))

    for name in methods:

        plt.loglog(
            taus,
            errors[name],
            marker="o",
            label=name
        )

    plt.xlabel("Schrittweite tau")
    plt.ylabel("Maximaler Fehler")
    plt.title("Konvergenz der numerischen Verfahren")
    plt.grid(True, which="both")
    plt.legend()
    plt.show()


    print("---Aufgabe3 c---")

    plt.figure(figsize=(9, 6))

    for name in methods:

        plt.loglog(
            times[name],
            errors[name],
            marker="o",
            label=name
        )

    plt.xlabel("CPU-Laufzeit in Sekunden")
    plt.ylabel("Maximaler Fehler")
    plt.title("Fehler in Abhängigkeit von der Laufzeit")
    plt.grid(True, which="both")
    plt.legend()
    plt.show()
