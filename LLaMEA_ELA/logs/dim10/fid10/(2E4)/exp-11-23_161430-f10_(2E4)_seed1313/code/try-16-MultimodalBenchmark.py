import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple periodic components with different frequencies and amplitudes
        for i in range(1, 6):
            result += (1.0 / i) * np.sum(np.sin(i * x) * np.cos(i * x))
        
        # Replace exponential decay with logarithmic terms that create complex valleys
        for i in range(self.dim):
            result += 0.5 * np.log(1.0 + 0.1 * np.abs(x[i])) * np.sin(2 * np.pi * x[i])
        
        # Add cubic polynomial cross-dimensional interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * (x[i]**3 + x[j]**3) * np.sin(x[i] + x[j])
        
        result += cross_term
        
        # Add a global scaling factor with modified sine terms
        result *= (1.0 + 0.3 * np.sum(np.sin(0.3 * x)**3))
        
        # Shift the global minimum to a non-origin point
        shift = np.ones(self.dim) * 1.5
        result += 2.0 * np.sum((x - shift)**2)
        
        return result