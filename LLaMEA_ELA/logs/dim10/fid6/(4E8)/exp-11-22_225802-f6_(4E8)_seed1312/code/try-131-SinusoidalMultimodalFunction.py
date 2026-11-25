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
        
        # Include stronger cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(6 * (scaled_x[i] - scaled_x[j]))
                
        # Add a small shift to the global minimum to increase challenge
        result += 0.09 * np.sum(np.sin(0.8 * x))
        
        # Enhanced polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.3 * (x[i]**4) * np.sin(2 * scaled_x[i])
            
        # Add a chaotic component with dynamic frequency modulation
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(scaled_x[i] * (1 + 0.5 * np.sin(x[i])))
        result += 0.25 * chaotic_component
        
        # Add a new term to increase the condition number and challenge
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.1 * x[i]**2) * np.cos(4 * scaled_x[i])
            
        # Add a hybrid component combining polynomial and sinusoidal elements
        hybrid_term = 0.0
        for i in range(self.dim):
            hybrid_term += (x[i]**3) * np.sin(3 * scaled_x[i]) + (x[i]**5) * np.cos(2 * scaled_x[i])
        result += 0.18 * hybrid_term
        
        return result