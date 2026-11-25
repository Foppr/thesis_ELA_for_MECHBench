import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for increased sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequencies and nonlinear interactions
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(4 * scaled_x[i]) * np.sin(7 * scaled_x[i]) * np.cos(2 * scaled_x[i])
            
        # Add multiple nested polynomial valleys with varying exponents
        for i in range(self.dim):
            result += 0.3 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2) + 0.2 * (x[i]**4)
            
        # Introduce dynamic scaling based on dimensionality and input magnitude
        dynamic_scale = np.sum(np.abs(x)) / self.dim + 0.1 * np.sum(x**2) / self.dim
        
        # Add ultra-high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.6 * np.sin(23 * scaled_x[i]) * np.cos(11 * scaled_x[i]) * np.sin(5 * scaled_x[i])
            
        # Add a global minimum at the origin with strong penalty terms
        result += 0.25 * np.sum(x**2) + 0.15 * dynamic_scale**2 + 0.05 * np.sum(x**4)
        
        # Include strong cross-dimension interactions with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(8 * (scaled_x[i] - scaled_x[j])) * np.sin(3 * (x[i] + x[j]))
                
        # Add a significant shift to the global minimum to increase challenge
        result += 0.12 * np.sum(np.sin(1.2 * x) + np.cos(0.8 * x))
        
        # Strong mutation: Increase influence of higher-order terms and add quintic interaction
        for i in range(self.dim):
            result += 0.08 * (x[i]**5)
            
        # Add a new cross-dimensional quintic interaction term with multiple frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(3 * scaled_x[i]) * np.cos(5 * scaled_x[j]) * (x[i] * x[j])**3
                
        # Add a complex multi-scale component with varying amplitude
        for i in range(self.dim):
            result += 0.15 * np.sin(13 * scaled_x[i]) * np.cos(9 * scaled_x[i]) * np.sin(4 * scaled_x[i]) * (1 + 0.2 * np.sin(7 * x[i]))
            
        # Add a final chaotic component with exponential scaling
        result += 0.1 * np.exp(-0.5 * np.sum(np.abs(x))) * np.sin(19 * np.sum(x))
        
        return result