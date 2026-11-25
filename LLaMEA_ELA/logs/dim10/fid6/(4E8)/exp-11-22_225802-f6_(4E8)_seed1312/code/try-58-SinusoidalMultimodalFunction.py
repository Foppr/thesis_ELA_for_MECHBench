import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-2*pi, 2*pi] for enhanced sinusoidal complexity
        scaled_x = x * (2.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with altered frequencies and coupling
        result = 0.0
        for i in range(self.dim):
            result += np.sin(1.5 * scaled_x[i]) * np.cos(2.5 * scaled_x[i]) * np.sin(4.0 * scaled_x[i])
            
        # Add nested quadratic valleys to create multiple local minima
        for i in range(self.dim):
            result += 0.3 * (np.sin(1.8 * scaled_x[i]) + 1) * (x[i]**2)
            
        # Introduce dynamic scaling based on dimensionality with enhanced complexity
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        
        # Add high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.4 * np.sin(8 * scaled_x[i]) * np.cos(5 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms
        result += 0.15 * np.sum(x**2) + 0.08 * dynamic_scale**2
        
        # Include cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.04 * np.sin(1.2 * scaled_x[i] + 0.8 * scaled_x[j]) * np.cos(3.0 * (scaled_x[i] - scaled_x[j]))
                
        # Add a new chaotic component with modified frequencies and coupling
        for i in range(self.dim):
            result += 0.22 * np.sin(5.0 * scaled_x[i]) * np.cos(7.0 * scaled_x[i]) * np.sin(8.0 * scaled_x[i])
            
        # Introduce a hybrid polynomial-sinusoidal term to enhance multimodality
        hybrid_term = 0.0
        for i in range(self.dim):
            hybrid_term += (x[i]**3) * np.sin(4.0 * scaled_x[i])
        result += 0.32 * hybrid_term / self.dim
        
        # Add a non-separable component with increased complexity
        separable_sum = 0.0
        for i in range(self.dim):
            separable_sum += np.sin(scaled_x[i]) * np.cos(1.5 * scaled_x[i])
        result += 0.15 * (separable_sum**2)
        
        # Add a new dimensionally dependent sinusoidal penalty term
        for i in range(self.dim):
            result += 0.05 * np.sin(6.0 * scaled_x[i]) * np.cos(4.0 * scaled_x[i]) * np.sin(2.0 * scaled_x[i])
            
        return result