import numpy as np

class ChaoticPolynomialBarrierFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable exponential behavior
        scaled_x = x / 5.0
        
        # Base chaotic sinusoidal component with multiple frequencies
        result = 0.0
        for i in range(self.dim):
            result += np.sin(2 * np.pi * scaled_x[i]) * np.cos(5 * np.pi * scaled_x[i]) * np.exp(-0.5 * scaled_x[i]**2)
            
        # Add polynomial cross-terms to create complex valleys and ridges
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased cross-dimensionality
                result += 0.2 * scaled_x[i]**2 * scaled_x[j]**3 * np.sin(np.pi * (scaled_x[i] + scaled_x[j]))
                
        # Introduce logarithmic barrier terms with multiple barriers to create disconnected regions
        barrier_penalty = 0.0
        for i in range(self.dim):
            if np.abs(scaled_x[i]) < 0.05:
                barrier_penalty += 15.0 * (1.0 / (np.abs(scaled_x[i]) + 1e-8) - 1.0)
            elif np.abs(scaled_x[i]) < 0.2:
                barrier_penalty += 5.0 * (1.0 / (np.abs(scaled_x[i]) + 1e-8) - 1.0)
            else:
                barrier_penalty += 0.0
                
        result += barrier_penalty
        
        # Add high-order polynomial terms for increased curvature and sharp gradients
        for i in range(self.dim):
            result += 0.1 * scaled_x[i]**7 + 0.05 * scaled_x[i]**5
            
        # Include dynamic scaling based on neighbor distances with chaotic weighting
        if self.dim > 1:
            dist_sum = 0.0
            weights = np.sin(np.linspace(0, np.pi, self.dim-1)) + 1.0
            for i in range(self.dim-1):
                dist_sum += weights[i] * np.abs(scaled_x[i+1] - scaled_x[i])
            result += 0.3 * dist_sum
            
        # Add global minimum at origin with additional penalty and chaotic scaling
        result += 0.15 * np.sum(scaled_x**2) + 0.05 * np.sum(np.sin(10 * scaled_x)**2)
        
        return result