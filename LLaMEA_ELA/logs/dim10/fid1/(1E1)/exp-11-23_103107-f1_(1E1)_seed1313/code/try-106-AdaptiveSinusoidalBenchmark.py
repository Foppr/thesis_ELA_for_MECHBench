import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Predefined global optima locations
        self.optima = np.array([[0.0] * dim, [2.5] * dim, [-2.5] * dim])
        
    def f(self, x):
        x = np.array(x)
        
        # Periodic sinusoidal components with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x)) + \
                     np.sum(np.sin(5 * np.pi * x) * np.cos(4 * np.pi * x)) + \
                     np.sum(np.sin(7 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Saddle-point structure with hyperbolic tangent interactions
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle += np.tanh(x[i] * x[j]) * np.sin(0.5 * (x[i]**2 + x[j]**2))
        
        # Adaptive penalty based on proximity to optima
        penalty = 0
        for i, optimum in enumerate(self.optima):
            dist = np.linalg.norm(x - optimum)
            penalty += 10 * np.exp(-0.1 * dist**2) * np.sin(2 * np.pi * dist)**2
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.5 * (x[i] - x[j])**2) * \
                           np.sin(2 * np.pi * (x[i] + x[j])) * \
                           np.cos(3 * np.pi * (x[i] - x[j]))
        
        # Return combined function value with scaling
        return 0.8 * (sinusoidal + saddle + penalty + coupling)