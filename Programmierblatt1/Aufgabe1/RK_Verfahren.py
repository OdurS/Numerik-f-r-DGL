import numpy as np
# umgestellt ki so, dass y_k+1= y_k + tau * sum(( 1 bis s)b_i * k_i)
def RungeKuttaVerfahren(f, y_0, T, tau, A, b, c): 

    K = int(round(T / tau))
    s = len(b)
    
    Y = np.zeros((len(y_0), K + 1))
    Y[:, 0] = y_0
    
    for n in range(K):
        t = n * tau
        y = Y[:, n]
        
        k = np.zeros((s, len(y_0)))
    
        for i in range(s):
            yi = y.copy()
            for j in range(i):
                yi += tau * A[i, j] * k[j]
                
            k[i] = f(t + c[i] * tau, yi)
    
            Y[:, n + 1] = y + tau * np.sum(
                b[:, np.newaxis] * k, axis=0  #k bleibt vektor
            )

    return Y
