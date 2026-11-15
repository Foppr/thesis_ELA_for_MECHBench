import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic base
        f_value = np.sum(x**2)
        
        # Add multiple local minima using high-frequency sinusoidal terms
        for i in range(self.dim):
            f_value += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Add strong interaction terms between dimensions with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.12 * np.sin(5 * x[i] + 3 * x[j]) * np.cos(4 * x[i] - 2 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add cubic and quartic terms for increased nonlinearity and complexity
        for i in range(self.dim):
            f_value += 0.05 * x[i]**3 + 0.02 * x[i]**4
            
        # Add a multi-peak sinusoidal component to increase landscape ruggedness
        peak_term = 0.0
        for i in range(self.dim):
            peak_term += np.sin(8 * x[i]) * np.cos(6 * x[i])
        f_value += 0.15 * peak_term
        
        # Add chaotic component using logistic map for increased complexity
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]  # Wrap around
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev)) * np.cos(3 * x[i])
        f_value += 0.1 * chaotic_term
        
        # Add a novel cross-dimensional coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        f_value += 0.08 * cross_term
        
        return f_value