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
            result += 0.4 * (np.sin(2 * scaled_x[i]) + 1) * (x[i]**2)
            
        # Introduce dynamic scaling based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        
        # Add high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.5 * np.sin(17 * scaled_x[i]) * np.cos(9 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms
        result += 0.2 * np.sum(x**2) + 0.1 * dynamic_scale**2
        
        # Include cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.07 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(6 * (scaled_x[i] - scaled_x[j]))
                
        # Add a small shift to the global minimum to increase challenge
        result += 0.09 * np.sum(np.sin(0.8 * x))
        
        # Slight modification: increase the coupling strength and add a cubic term for more complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(2 * scaled_x[i]) * np.cos(4 * scaled_x[j]) * (x[i]**3 + x[j]**3)
        
        # Add a new component to improve fitness score: enhanced quartic terms with directional coupling
        for i in range(self.dim):
            result += 0.18 * (x[i]**4) * np.sin(2 * scaled_x[i])
            
        # Add a new cross-dimensional interaction with higher frequency coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.11 * np.sin(7 * scaled_x[i]) * np.cos(11 * scaled_x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a final penalty term to ensure global minimum is well-defined
        result += 0.05 * np.sum(np.abs(x)**3)
        
        return result