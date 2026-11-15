import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 2.0 * np.sin(3 * x[i]) * np.cos(5 * x[i]) * np.sin(7 * x[i])
            
        # Add polynomial interactions with mixed degrees
        for i in range(self.dim):
            f += 0.5 * x[i]**3 + 0.3 * x[i]**4 + 0.1 * x[i]**5
            
        # Add exponential coupling between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.3 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2 * x[i] * x[j])
                
        # Add chaotic sine modulation with non-linear coupling
        chaotic_sum = 0
        for i in range(self.dim):
            chaotic_sum += np.sin(11 * x[i] + np.sin(7 * x[i]))
        f += 0.4 * np.sin(chaotic_sum)
        
        # Add multi-scale sinusoidal pattern with nested structure
        for i in range(self.dim):
            f += 0.2 * np.sin(13 * x[i]) * np.cos(17 * x[i]) * np.sin(19 * x[i]) * np.cos(23 * x[i])
            
        # Add cross-dimensional coupling with higher-order terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f += 0.1 * x[i] * x[j]**2 * x[k]**3
                    
        # Add global minima locations with exponential decay
        minima_locations = [[-2.5, 2.5], [2.5, -2.5], [-4.0, 4.0], [4.0, -4.0]]
        minima_penalty = 0
        for loc in minima_locations:
            if self.dim >= len(loc):
                diff = x[:len(loc)] - np.array(loc)
                minima_penalty += np.exp(-0.3 * np.sum(diff**2))
        f += 1.0 * minima_penalty
        
        # Add noise term with chaotic behavior
        noise = 0
        for i in range(self.dim):
            noise += np.sin(19 * x[i] + np.cos(13 * x[i])) * np.cos(17 * x[i] + np.sin(11 * x[i]))
        f += 0.05 * noise
        
        # Add dimensional coupling with trigonometric polynomial
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(3 * x[i] + 2 * x[j]) * np.cos(4 * x[i] - x[j])
        f += 0.25 * coupling_term
        
        return f