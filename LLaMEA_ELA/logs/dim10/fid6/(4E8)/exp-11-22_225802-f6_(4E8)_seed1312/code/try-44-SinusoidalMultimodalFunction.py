import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stable exponential behavior
        scaled_x = x / 5.0
        
        # Base chaotic sinusoidal component with multiple frequencies
        result = 0.0
        for i in range(self.dim):
            result += np.sin(2 * np.pi * scaled_x[i]) * np.cos(3 * np.pi * scaled_x[i])
            
        # Add nested multimodal terms with varying scales
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * np.pi * scaled_x[i]) * np.exp(-0.5 * scaled_x[i]**2)
            
        # Introduce polynomial cross-terms to create complex valleys and ridges
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased cross-dimensionality
                result += 0.2 * scaled_x[i]**2 * scaled_x[j]**3
                
        # Add logarithmic barrier terms to create disconnected regions and sharp gradients
        barrier_penalty = 0.0
        for i in range(self.dim):
            if np.abs(scaled_x[i]) < 0.05:
                barrier_penalty += 20.0 * (1.0 / (np.abs(scaled_x[i]) + 1e-8) - 1.0)
            else:
                barrier_penalty += 0.0
                
        result += barrier_penalty
        
        # Add high-order polynomial terms for increased curvature and complexity
        for i in range(self.dim):
            result += 0.1 * scaled_x[i]**7
            
        # Include dynamic scaling based on neighbor distances with chaotic factor
        if self.dim > 1:
            dist_sum = 0.0
            for i in range(self.dim-1):
                dist_sum += np.abs(scaled_x[i+1] - scaled_x[i])
            result += 0.3 * dist_sum * (1.0 + 0.5 * np.sin(5 * np.pi * np.sum(scaled_x)))
            
        # Add global minimum at origin with additional penalty and chaotic scaling
        result += 0.2 * np.sum(scaled_x**2) * (1.0 + 0.3 * np.sin(7 * np.pi * np.sum(scaled_x)))
        
        return result