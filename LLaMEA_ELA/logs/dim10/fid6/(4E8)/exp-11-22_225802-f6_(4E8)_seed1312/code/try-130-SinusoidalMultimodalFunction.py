import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for increased sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base sinusoidal component with enhanced chaotic interaction terms
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(4 * scaled_x[i]) * np.sin(7 * scaled_x[i]) * np.cos(2 * scaled_x[i])
            
        # Add nested quadratic valleys with cubic terms to create multiple local minima
        for i in range(self.dim):
            result += 0.6 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2 + 0.5 * x[i]**3)
            
        # Introduce dynamic scaling based on dimensionality with exponential factor
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale = np.exp(dynamic_scale) - 1
        
        # Add high-frequency oscillations with varying amplitudes to increase complexity
        for i in range(self.dim):
            result += 0.8 * np.sin(23 * scaled_x[i]) * np.cos(11 * scaled_x[i]) * np.sin(5 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms including logarithmic scaling
        result += 0.3 * np.sum(x**2) + 0.15 * dynamic_scale**2 + 0.05 * np.log(1 + np.sum(x**4))
        
        # Include stronger cross-dimension interactions with sinusoidal coupling coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(8 * (scaled_x[i] - scaled_x[j])) * np.sin(3 * (x[i] + x[j]))
                
        # Add a small shift to the global minimum with higher-order polynomial terms
        result += 0.12 * np.sum(np.sin(1.2 * x) + 0.3 * np.sin(2.4 * x)**3)
        
        # Major mutation: add chaotic cubic coupling terms and hyperbolic sine components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sinh(3 * scaled_x[i]) * np.cos(5 * scaled_x[j]) * (x[i]**3 + x[j]**4)
                
        # Add a novel fractal-like component with recursive sinusoidal terms
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(scaled_x[i] * np.cos(scaled_x[i])) * np.cos(scaled_x[i] * np.sin(scaled_x[i]))
        result += 0.25 * fractal_term
        
        return result