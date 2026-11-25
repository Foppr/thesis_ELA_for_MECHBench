import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-2*pi, 2*pi] for enhanced sinusoidal complexity
        scaled_x = x * (2.0 * np.pi / 5.0)
        
        # Base sinusoidal component with chaotic interaction terms
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(3 * scaled_x[i]) * np.sin(5 * scaled_x[i])
            
        # Add nested quadratic valleys to create multiple local minima
        for i in range(self.dim):
            result += 0.2 * (np.sin(2 * scaled_x[i]) + 1) * (x[i]**2)
            
        # Introduce dynamic scaling based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        
        # Add high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(10 * scaled_x[i]) * np.cos(7 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms
        result += 0.1 * np.sum(x**2) + 0.05 * dynamic_scale**2
        
        # Include cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(2 * (scaled_x[i] - scaled_x[j]))
                
        # Add a new chaotic component with modified frequencies and coupling
        for i in range(self.dim):
            result += 0.15 * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[i]) * np.sin(8 * scaled_x[i])
            
        # Introduce a hybrid polynomial-sinusoidal term to enhance multimodality
        hybrid_term = 0.0
        for i in range(self.dim):
            hybrid_term += (x[i]**4) * np.sin(3 * scaled_x[i])
        result += 0.25 * hybrid_term / self.dim
        
        # Add a non-separable component with increased complexity
        separable_sum = 0.0
        for i in range(self.dim):
            separable_sum += np.sin(scaled_x[i]) * np.cos(scaled_x[i])
        result += 0.1 * (separable_sum**2)
        
        return result