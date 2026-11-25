import numpy as np

class ChaoticMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical basin term
        sphere = 0.1 * np.sum(x**2)
        
        # Logistic map chaotic component
        logistic = 0.0
        r = 3.99
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            logistic += np.sin(r * x_prev * (1 - x_prev)) * np.cos(x[i])
        
        # Multi-scale sinusoidal modulation
        multiscale = 0.0
        for i in range(self.dim):
            multiscale += 0.5 * np.sin(2 * np.pi * x[i]) + \
                          0.3 * np.sin(4 * np.pi * x[i]) + \
                          0.2 * np.sin(8 * np.pi * x[i])
        
        # Cross-dimensional interaction with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            cross_interaction += np.exp(-0.1 * abs(x[i] - x[j])) * np.sin(3 * x[i]) * np.cos(2 * x[j])
        
        # Fractal-like structure with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += (x[i] ** 4) * np.sin(10 * x[i]) + \
                       (x[i] ** 3) * np.cos(5 * x[i]) + \
                       (x[i] ** 2) * np.sin(7 * x[i])
        
        # Final combined fitness
        return sphere + 0.8 * logistic + 1.2 * multiscale + 0.6 * cross_interaction + 0.4 * fractal