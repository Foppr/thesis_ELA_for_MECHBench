import numpy as np

class SinusoidalCrossCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Predefined global optima locations
        self.optima = np.array([[2.5, -1.5], [-2.0, 2.0], [0.0, 0.0]]) if dim >= 2 else np.array([[0.0]])
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal periodic components with varying frequencies
        sinusoidal = np.sum(np.sin(5 * x)**2 + np.cos(3 * x)**2)
        
        # Cross-dimensional coupling with interaction terms
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] - x[j])**2 * np.sin(x[i] * x[j])
                
        # Distance-based penalty with multiple local minima
        penalty = 0
        for i in range(len(self.optima)):
            if self.dim >= 2:
                dist = np.sqrt((x[0] - self.optima[i][0])**2 + (x[1] - self.optima[i][1])**2)
            else:
                dist = abs(x[0] - self.optima[i][0])
            penalty += 10 * (1 - np.exp(-0.1 * (dist - 1)**2)) * np.sin(2 * np.pi * dist)**2
        
        # Additional quadratic term to increase conditioning
        quadratic = 0.5 * np.sum(x**2)
        
        return sinusoidal + coupling + penalty + quadratic