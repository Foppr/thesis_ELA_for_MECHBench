import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        logistic = 0.0
        r = 3.95
        for i in range(10):
            logistic += np.sum(np.sin(r * x * (1 - x)))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-4, 4, min(5, self.dim))
        rbfs = 0.0
        for c in centers:
            rbfs += np.exp(-np.sum((x - c)**2) / 2.0)
        
        # Cross-terms with asymmetric weights
        cross = 0.0
        for i in range(self.dim - 1):
            cross += (i + 1) * x[i] * x[i+1]**3
        
        # Polynomial and sinusoidal mix
        poly = np.sum(x**2) + 0.5 * np.sum(x**6)
        sin = np.sum(np.sin(3.0 * x)) + 0.3 * np.sum(np.cos(4.0 * x)**2)
        
        return logistic + rbfs + cross + poly + sin