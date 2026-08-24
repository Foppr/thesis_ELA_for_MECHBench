import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add radial basis function components with varying centers and widths
        for i in range(self.dim):
            center = 2.0 * np.sin(i)
            width = 0.5 + 0.5 * np.cos(i)
            f_val += 0.3 * np.exp(-width * (x[i] - center)**2) * np.sin(3 * (x[i] - center))
        
        # Add cross-dimensional polynomial interactions with sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] - x[j])) * np.sin(2 * (x[i] + x[j]))
        
        # Add high-frequency sinusoidal oscillations
        for i in range(self.dim):
            f_val += 0.25 * np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.1 * np.sin(15 * x[i])**3
        
        # Add a global landscape modulation based on the norm of x
        norm_x = np.linalg.norm(x)
        f_val += 0.05 * np.sin(0.3 * norm_x) * np.cos(0.4 * norm_x) * np.sum(x**4)
        
        # Add a shifted and scaled exponential term to increase local optima density
        for i in range(self.dim):
            f_val += 0.15 * np.exp(-0.2 * (x[i] - 1.0)**2) * np.cos(6 * (x[i] + 1.0))
        
        return f_val