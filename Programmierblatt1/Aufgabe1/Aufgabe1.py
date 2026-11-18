from . import RK_Verfahren as rk
import numpy as np
def explicit_euler(f, y_0, T, tau):
    Y= rk.RungeKuttaVerfahren(f, y_0, T, tau, 0, 1, 0)

    return Y



def explicit_heun(f, y_0, T, tau):
    A = np.array([
    [0, 0],
    [1, 0]
    ])

    b = np.array([1/2, 1/2])
    c = np.array([0, 1])

    Y= rk.RungeKuttaVerfahren(f, y_0, T, tau, A, b, c)
      
    return Y



def explicit_runge_kutta3(f, y_0, T, tau):
    A = np.array([
        [0,    0, 0],
        [1/2,  0, 0],
        [-1,   2, 0]
    ])
    b = np.array([1/6, 4/6, 1/6])
    c = np.array([0, 1/2, 1])
    
    Y= rk.RungeKuttaVerfahren(f, y_0, T, tau, A, b, c)
    
    return Y