import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-4*pi, 4*pi] for even greater sinusoidal complexity
        scaled_x = x * (4.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequencies and interactions
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(5 * scaled_x[i]) * np.sin(9 * scaled_x[i]) * np.cos(3 * scaled_x[i])
            
        # Add multiple nested polynomial valleys with varying exponents
        for i in range(self.dim):
            result += 0.7 * (np.sin(4 * scaled_x[i]) + 1) * (x[i]**2) + 0.4 * (x[i]**4) + 0.2 * (x[i]**6)
            
        # Introduce dynamic scaling based on dimensionality and magnitude
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        magnitude_factor = np.sqrt(np.sum(x**2))
        
        # Add ultra-high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 1.0 * np.sin(31 * scaled_x[i]) * np.cos(17 * scaled_x[i]) * np.sin(19 * scaled_x[i])
            
        # Add a global minimum at the origin with strong penalty terms
        result += 0.4 * np.sum(x**2) + 0.2 * dynamic_scale**2 + 0.1 * magnitude_factor**2
        
        # Include strong cross-dimension interactions with higher-order coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(9 * (scaled_x[i] - scaled_x[j])) * np.sin(4 * (x[i] * x[j]))
                
        # Add a significant shift to the global minimum to increase challenge
        result += 0.2 * np.sum(np.sin(1.5 * x) + 0.6 * np.cos(2.8 * x))
        
        # Heavy mutation: Increase influence of higher-order terms and add quintic interaction
        for i in range(self.dim):
            result += 0.15 * (x[i]**5)
            
        # Add a new cross-dimensional quintic interaction term with chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[j]) * (x[i] * x[j])**3
                
        # Add a novel hyper-cubic interaction term
        cubic_sum = np.sum(x**3)
        result += 0.06 * cubic_sum**2
        
        # Add hyper-spectral oscillations for increased multimodality
        for i in range(self.dim):
            result += 0.12 * np.sin(5 * scaled_x[i]) * np.cos(7 * scaled_x[i]) * np.sin(13 * scaled_x[i]) * np.cos(11 * scaled_x[i])
            
        # Add a new sixth-order polynomial interaction
        for i in range(self.dim):
            result += 0.08 * (x[i]**6)
            
        # Add a new cross-dimensional seventh-order interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * (x[i] * x[j])**4
                
        return result