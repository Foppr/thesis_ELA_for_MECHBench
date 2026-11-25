import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for even greater sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequencies and nonlinear interactions
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(4 * scaled_x[i]) * np.sin(7 * scaled_x[i]) * np.cos(2 * scaled_x[i])
            
        # Add nested polynomial valleys with varying exponents to create diverse local minima
        for i in range(self.dim):
            result += 0.6 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**4) + 0.3 * (x[i]**6)
            
        # Introduce dynamic scaling with exponential weighting based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale = np.exp(dynamic_scale) - 1.0
        
        # Add ultra-high-frequency oscillations to increase complexity and reduce algorithmic performance
        for i in range(self.dim):
            result += 0.8 * np.sin(23 * scaled_x[i]) * np.cos(15 * scaled_x[i]) * np.sin(11 * scaled_x[i])
            
        # Add a global minimum at the origin with strong penalty terms and nonlinearity
        result += 0.3 * np.sum(x**2) + 0.2 * dynamic_scale**3
        
        # Include strong cross-dimension interactions with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(8 * (scaled_x[i] - scaled_x[j])) * np.sin(3 * (x[i] * x[j]))
                
        # Add a significant shift to the global minimum with a complex distortion term
        result += 0.15 * np.sum(np.sin(1.2 * x) + 0.5 * np.cos(2.4 * x))
        
        # Introduce higher-order coupling with cubic and quintic terms for more complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(3 * scaled_x[i]) * np.cos(5 * scaled_x[j]) * (x[i]**4 + x[j]**5)
                
        # Add a final chaotic component with exponentially varying frequencies
        for i in range(self.dim):
            result += 0.1 * np.sin(np.exp(scaled_x[i])) * np.cos(np.exp(2 * scaled_x[i]))
        
        return result