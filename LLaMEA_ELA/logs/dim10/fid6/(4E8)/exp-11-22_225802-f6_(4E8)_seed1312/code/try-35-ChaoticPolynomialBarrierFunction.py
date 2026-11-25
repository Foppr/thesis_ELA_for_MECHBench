import numpy as np

class ChaoticPolynomialBarrierFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable exponential behavior
        scaled_x = x / 5.0
        
        # Base exponential decay component with chaotic interaction
        result = 0.0
        for i in range(self.dim):
            result += np.exp(-np.abs(scaled_x[i])) * np.sin(2 * np.pi * scaled_x[i])
            
        # Add polynomial cross-terms to create complex valleys
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimensionality
                result += 0.1 * scaled_x[i]**3 * scaled_x[j]**2
                
        # Introduce logarithmic barrier terms to create disconnected regions
        barrier_penalty = 0.0
        for i in range(self.dim):
            if np.abs(scaled_x[i]) < 0.1:
                barrier_penalty += 10.0 * (1.0 / (np.abs(scaled_x[i]) + 1e-8) - 1.0)
            else:
                barrier_penalty += 0.0
                
        result += barrier_penalty
        
        # Add high-order polynomial terms for increased curvature
        for i in range(self.dim):
            result += 0.05 * scaled_x[i]**6
            
        # Include dynamic scaling based on neighbor distances
        if self.dim > 1:
            dist_sum = 0.0
            for i in range(self.dim-1):
                dist_sum += np.abs(scaled_x[i+1] - scaled_x[i])
            result += 0.2 * dist_sum
            
        # Add global minimum at origin with additional penalty
        result += 0.1 * np.sum(scaled_x**2)
        
        return result