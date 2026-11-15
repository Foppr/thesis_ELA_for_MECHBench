import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multi-scale sinusoidal components with varying frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.3 * np.sin(5 * x[i])**3
        
        # Radial basis function components to create local optima
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                f_val += 0.2 * np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(6 * (x[i] + x[j]))
        
        # Polynomial chaos terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 0.1 * (x[i]**4) * np.cos(3 * x[i]) + 0.05 * (x[i]**6) * np.sin(2 * x[i])
        
        # Multi-modal exponential terms with shifted centers
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i, center in enumerate(centers):
            if i < self.dim:
                f_val += 0.15 * np.exp(-0.2 * (x[i] - center)**2) * np.cos(5 * (x[i] - center))
        
        # Add noise-like perturbations to increase complexity
        for i in range(self.dim):
            f_val += 0.03 * np.sin(15 * x[i]) * np.cos(12 * x[i])
        
        return f_val