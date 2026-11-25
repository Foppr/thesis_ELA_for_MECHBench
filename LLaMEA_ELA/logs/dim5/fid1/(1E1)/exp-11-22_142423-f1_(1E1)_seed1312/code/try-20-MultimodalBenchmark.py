import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add multiple local minima using enhanced sinusoidal terms with higher frequencies
        for i in range(self.dim):
            f += 0.4 * np.sin(12 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            
        # Add additional interaction terms between non-adjacent dimensions with different coefficients
        for i in range(self.dim):
            f += 0.2 * np.sin(6 * x[i]) * np.sin(4 * x[(i + 2) % self.dim])
            
        # Add cubic and higher-order interactions for increased complexity
        for i in range(self.dim):
            f += 0.05 * x[i]**3 * np.cos(3 * x[(i + 1) % self.dim])
            
        # Add shifted local minima and modified penalty terms with stronger nonlinear effects
        f += 0.04 * np.sum(np.abs(x)) + 0.02 * np.sum(x**4) + 0.25 * np.sum(np.sin(0.7 * x))
        
        return f