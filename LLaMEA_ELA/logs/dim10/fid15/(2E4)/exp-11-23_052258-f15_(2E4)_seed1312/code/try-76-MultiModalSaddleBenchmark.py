import numpy as np

class MultiModalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x**4) + 0.5 * np.sum(x**3) + 0.1 * np.sum(x**2)
        
        # Multi-modal component with multiple local minima
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += (x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 10)
            
        # Saddle point structure with alternating signs
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += x[i] * np.sin(x[i]) * (-1)**i
            
        # Logarithmic barrier near boundaries to encourage exploration
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += 1.0 / (1.0 + np.exp(-10 * (x[i] - 5))) + 1.0 / (1.0 + np.exp(10 * (x[i] + 5)))
            
        # Cross-dimensional interaction with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(0.5 * (x[i] + x[j]))
                
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.01 * self.dim + 0.001 * np.sum(np.abs(x))
        
        return scale_factor * (poly_term + modal_term + saddle_term + barrier_term + 0.5 * cross_term)