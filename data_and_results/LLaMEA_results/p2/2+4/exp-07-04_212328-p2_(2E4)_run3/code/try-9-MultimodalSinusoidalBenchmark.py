import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = np.sum(x**2) * 0.5
        
        # Add chaotic sinusoidal grid pattern with varying frequencies
        for i in range(self.dim):
            f += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
            
        # Add nested multi-scale interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                f += 0.1 * np.sin(3 * x[i] + 2 * x[j]) * np.cos(5 * x[i] - x[j])
                
        # Add fractal-like self-similar structure
        for i in range(self.dim):
            f += 0.05 * np.sin(10 * np.sin(3 * x[i])) * np.cos(7 * np.cos(2 * x[i]))
            
        # Add higher-order polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, min(j+3, self.dim)):
                    f += 0.02 * x[i]**2 * np.sin(x[j] + x[k])
                    
        # Add multiple global minima at non-origin locations
        global_minima = np.array([[-2.5, 2.5], [2.5, -2.5], [-2.5, -2.5], [2.5, 2.5]])
        if self.dim >= 2:
            minima_term = 0
            for min_point in global_minima:
                if self.dim >= len(min_point):
                    diff = x[:len(min_point)] - min_point
                    minima_term += np.exp(-0.5 * np.sum(diff**2))
            f += 0.3 * minima_term
            
        # Add noise component for additional challenge
        f += 0.01 * np.sum(np.sin(10 * x)**2)
        
        return f