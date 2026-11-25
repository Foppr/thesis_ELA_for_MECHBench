import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic sinusoidal components with non-linear frequency modulation
        for i in range(self.dim):
            freq = 5.0 + 3.0 * np.sin(0.5 * x[i])
            result += 0.2 * np.sin(freq * x[i]) * np.cos(3.0 * x[i] + 0.5 * np.cos(x[i]))
        
        # Complex cross-dimensional interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) + 0.3 * np.cos(x[i] + x[j])**2
                result += 0.1 * coupling * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Irregular penalty landscape with multiple local minima
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.03 * (np.abs(x[i] - 1.0) + np.abs(x[i] + 2.0)) * np.sin(5.0 * x[i])
        result += penalty
        
        # Add a small random perturbation to increase non-smoothness
        noise = 0.001 * np.sum(np.random.rand(self.dim) * (x**2))
        result += noise
        
        return result