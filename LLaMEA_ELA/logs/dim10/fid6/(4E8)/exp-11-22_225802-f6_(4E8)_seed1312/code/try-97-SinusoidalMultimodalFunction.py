import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for increased sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with modified frequency ratios
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2.5 * scaled_x[i]) * np.sin(4 * scaled_x[i])
            
        # Add nested quadratic valleys with varying coefficients
        for i in range(self.dim):
            result += 0.4 * (np.sin(1.5 * scaled_x[i]) + 1) * (x[i]**2)
            
        # Introduce dynamic scaling based on dimensionality with enhanced complexity
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        
        # Add high-frequency oscillations with modified coupling
        for i in range(self.dim):
            result += 0.5 * np.sin(15 * scaled_x[i]) * np.cos(11 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms
        result += 0.2 * np.sum(x**2) + 0.1 * dynamic_scale**2
        
        # Include stronger cross-dimension interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.sin(2.5 * scaled_x[i] + 1.8 * scaled_x[j]) * np.cos(4 * (scaled_x[i] - scaled_x[j]))
                
        # Add a small shift to the global minimum with modified parameters
        result += 0.1 * np.sum(np.sin(0.7 * x))
        
        # Introduce enhanced polynomial exponents and coupling coefficients for increased difficulty
        for i in range(self.dim):
            result += 0.28 * (x[i]**3.5) * np.cos(5 * scaled_x[i])
            
        # Add a new chaotic component with modified interaction terms
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * scaled_x[i]) * np.cos(3 * scaled_x[i]) * np.sin(9 * scaled_x[i])
            
        return result