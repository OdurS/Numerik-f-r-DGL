import matplotlib.pyplot as plt
import numpy as np
from . import Aufgabe1_Standart as a1  #Mit stadart verfahren
def Aufgabe1_Beispiel():
    print("\n========== TEST 1: EXPONENTIELLES WACHSTUM ==========")

    def f1(t, y):
        return y

    y_0 = np.array([1.0])
    T = 2
    tau = 0.1

    Y_euler = a1.explicit_euler(f1, y_0, T, tau)
    Y_heun = a1.explicit_heun(f1, y_0, T, tau)
    Y_rk3 = a1.explicit_runge_kutta3(f1, y_0, T, tau)

    exakt = np.exp(T)

    print("Exakte Lösung:", exakt)
    print("Euler:", Y_euler[0, -1])
    print("Heun:", Y_heun[0, -1])
    print("Runge-Kutta 3:", Y_rk3[0, -1])

    print("Fehler Euler:", abs(exakt - Y_euler[0, -1]))
    print("Fehler Heun:", abs(exakt - Y_heun[0, -1]))
    print("Fehler RK3:", abs(exakt - Y_rk3[0, -1]))


    print("\n========== TEST 2: HARMONISCHER OSZILLATOR ==========")

    def f2(t, y):
        return np.array([y[1], -y[0]])

    y_0 = np.array([1.0, 0.0])
    T = 20
    tau = 0.1

    Y_euler = a1.explicit_euler(f2, y_0, T, tau)
    Y_heun = a1.explicit_heun(f2, y_0, T, tau)
    Y_rk3 = a1.explicit_runge_kutta3(f2, y_0, T, tau)

    t = np.linspace(0, T, Y_euler.shape[1])

    plt.figure(figsize=(10, 6))

    plt.plot(Y_euler[0], Y_euler[1], label="Euler")
    plt.plot(Y_heun[0], Y_heun[1], label="Heun")
    plt.plot(Y_rk3[0], Y_rk3[1], label="Runge-Kutta 3")

    plt.xlabel("Position")
    plt.ylabel("Geschwindigkeit")
    plt.title("Harmonischer Oszillator")
    plt.legend()
    plt.grid()
    plt.axis("equal")
    plt.show()




    print("\n========== TEST 3: RÄUBER-BEUTE-MODELL ==========")

    def f3(t, y):
        x, z = y

        return np.array([
            x * (1 - z),
            z * (x - 1)
        ])

    y_0 = np.array([2.0, 1.0])
    T = 20
    tau = 0.05

    Y_euler = a1.explicit_euler(f3, y_0, T, tau)
    Y_heun = a1.explicit_heun(f3, y_0, T, tau)
    Y_rk3 = a1.explicit_runge_kutta3(f3, y_0, T, tau)

    plt.figure(figsize=(10, 6))

    plt.plot(Y_euler[0], Y_euler[1], label="Euler")
    plt.plot(Y_heun[0], Y_heun[1], label="Heun")
    plt.plot(Y_rk3[0], Y_rk3[1], label="Runge-Kutta 3")

    plt.xlabel("Beutepopulation x")
    plt.ylabel("Räuberpopulation y")
    plt.title("Räuber-Beute-Modell")
    plt.legend()
    plt.grid()
    plt.show()




    print("\n========== TEST 4: FEHLERVERGLEICH ==========")

    def f4(t, y):
        return y

    y_0 = np.array([1.0])
    T = 1

    for tau in [0.2, 0.1, 0.05, 0.025]:

        exakt = np.exp(T)

        E = a1.explicit_euler(f4, y_0, T, tau)
        H = a1.explicit_heun(f4, y_0, T, tau)
        R = a1.explicit_runge_kutta3(f4, y_0, T, tau)

        fehler_E = abs(exakt - E[0, -1])
        fehler_H = abs(exakt - H[0, -1])
        fehler_R = abs(exakt - R[0, -1])

        print("\nSchrittweite:", tau)
        print("Euler-Fehler:", fehler_E)
        print("Heun-Fehler:", fehler_H)
        print("RK3-Fehler:", fehler_R)
