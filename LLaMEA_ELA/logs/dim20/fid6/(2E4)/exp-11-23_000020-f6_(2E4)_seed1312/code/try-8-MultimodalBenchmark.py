import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        result = np.sum(x_norm**2)
        
        # Multiple nested sinusoidal components creating complex landscape
        for i in range(self.dim):
            # Primary oscillatory pattern
            result += 0.3 * np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[(i+1) % self.dim])
            
            # Secondary interaction terms
            if i > 0:
                result += 0.2 * np.sin(8 * x_norm[i-1]) * np.sin(6 * x_norm[i]) * np.cos(4 * x_norm[(i+2) % self.dim])
                
        # Add high-frequency oscillations for increased complexity
        for i in range(self.dim):
            result += 0.15 * np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[(i+3) % self.dim]) * np.sin(12 * x_norm[(i+1) % self.dim])
        
        # Add a global minimum with penalty terms for convergence testing
        result += 0.02 * np.sum(np.abs(x_norm)**4) + 0.01 * np.sum(np.abs(x_norm)**5)
        
        # Add a complex interaction term between all dimensions
        interaction_term = 0.25 * np.prod(np.sin(x_norm))
        result += interaction_term
        
        return result