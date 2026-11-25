import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for increased sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequency interactions
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2 * scaled_x[i]) * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[i])
            
        # Add nested quartic valleys to create multiple local minima
        for i in range(self.dim):
            result += 0.6 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**4)
            
        # Introduce dynamic scaling based on dimensionality with exponential factor
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale = np.exp(dynamic_scale) - 1.0
        
        # Add ultra-high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.8 * np.sin(23 * scaled_x[i]) * np.cos(13 * scaled_x[i]) * np.sin(19 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms including hyperbolic functions
        result += 0.3 * np.sum(x**2) + 0.15 * dynamic_scale**3 + 0.05 * np.sum(np.tanh(x))
        
        # Include stronger cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.12 * np.sin(2 * (scaled_x[i] + scaled_x[j])) * np.cos(7 * (scaled_x[i] - scaled_x[j])) * np.sin(5 * (scaled_x[i] * scaled_x[j]))
                
        # Add a small shift to the global minimum with additional chaotic sinusoidal terms
        result += 0.15 * np.sum(np.sin(1.2 * x) * np.cos(0.9 * x))
        
        # Add a final chaotic correction term based on all dimensions
        result += 0.1 * np.sin(np.sum(scaled_x)**2) * np.cos(np.sum(x**3))
        
        return result