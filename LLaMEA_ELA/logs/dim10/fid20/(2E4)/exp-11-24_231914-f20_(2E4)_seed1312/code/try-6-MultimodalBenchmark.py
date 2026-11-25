import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using exponentially decaying sinusoidal terms
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Add more complex interaction terms between dimensions with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimension interactions
                f_val += 0.3 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a periodic global structure with multiple valleys
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
        f_val += 0.8 * periodic_term**2
        
        # Add noise-like perturbations to increase complexity
        for i in range(self.dim):
            f_val += 0.05 * np.sin(15 * x[i]) * np.cos(12 * x[i])
            
        return f_val