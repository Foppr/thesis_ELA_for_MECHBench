import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for increased sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequencies and amplitudes
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2 * scaled_x[i]) * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[i])
            
        # Add nested polynomial valleys with varying exponents to create multiple local minima
        for i in range(self.dim):
            result += 0.3 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2) + 0.1 * (x[i]**4)
            
        # Introduce dynamic scaling based on dimensionality and input magnitude
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale += 0.05 * np.std(x)
        
        # Add ultra-high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.6 * np.sin(23 * scaled_x[i]) * np.cos(11 * scaled_x[i]) * np.sin(19 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms and exponential scaling
        result += 0.25 * np.sum(x**2) + 0.15 * dynamic_scale**2 + 0.05 * np.exp(-0.1 * np.sum(x**2))
        
        # Include complex cross-dimension interactions with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(5 * (scaled_x[i] - scaled_x[j])) * np.sin(3 * (x[i] * x[j]))
                
        # Add a small shift to the global minimum using a multi-frequency sinusoidal term
        result += 0.12 * np.sum(np.sin(0.9 * x) + np.cos(0.7 * x))
        
        # Slight mutation: Increase influence of higher-order terms and add cubic interaction with exponential decay
        for i in range(self.dim):
            result += 0.08 * (x[i]**3) * np.exp(-0.05 * np.abs(x[i]))
            
        # Add a new cross-dimensional cubic interaction term with variable coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(3 * scaled_x[i]) * np.cos(5 * scaled_x[j]) * (x[i] * x[j])**2 * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add a fractal-like self-similar structure using recursive scaling
        for i in range(self.dim):
            result += 0.03 * np.sin(7 * scaled_x[i]) * np.cos(13 * scaled_x[i]) * np.sin(11 * scaled_x[i])
            
        return result