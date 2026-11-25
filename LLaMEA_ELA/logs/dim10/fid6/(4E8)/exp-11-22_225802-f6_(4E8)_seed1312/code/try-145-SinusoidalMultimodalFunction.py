import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-4*pi, 4*pi] for increased sinusoidal complexity
        scaled_x = x * (4.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequencies and amplitudes
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2 * scaled_x[i]) * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[i]) * np.sin(8 * scaled_x[i])
            
        # Add nested polynomial valleys with varying exponents to create multiple local minima
        for i in range(self.dim):
            result += 0.4 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2) + 0.15 * (x[i]**4) + 0.05 * (x[i]**6)
            
        # Introduce dynamic scaling based on dimensionality and input magnitude
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        dynamic_scale += 0.08 * np.std(x)
        
        # Add ultra-high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 0.7 * np.sin(31 * scaled_x[i]) * np.cos(17 * scaled_x[i]) * np.sin(29 * scaled_x[i]) * np.cos(23 * scaled_x[i])
            
        # Add a global minimum at the origin with additional penalty terms and exponential scaling
        result += 0.3 * np.sum(x**2) + 0.2 * dynamic_scale**2 + 0.08 * np.exp(-0.15 * np.sum(x**2))
        
        # Include complex cross-dimension interactions with trigonometric coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(scaled_x[i] + scaled_x[j]) * np.cos(7 * (scaled_x[i] - scaled_x[j])) * np.sin(4 * (x[i] * x[j]))
                
        # Add a small shift to the global minimum using a multi-frequency sinusoidal term
        result += 0.15 * np.sum(np.sin(1.1 * x) + np.cos(0.9 * x))
        
        # Slight mutation: Increase influence of higher-order terms and add cubic interaction with exponential decay
        for i in range(self.dim):
            result += 0.12 * (x[i]**3) * np.exp(-0.08 * np.abs(x[i]))
            
        # Add a new cross-dimensional cubic interaction term with variable coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[j]) * (x[i] * x[j])**2 * np.exp(-0.15 * (x[i]**2 + x[j]**2))
                
        # Add a fractal-like self-similar structure using recursive scaling
        for i in range(self.dim):
            result += 0.05 * np.sin(9 * scaled_x[i]) * np.cos(15 * scaled_x[i]) * np.sin(13 * scaled_x[i]) * np.cos(17 * scaled_x[i])
            
        # Add a new high-frequency chaotic component with variable amplitude
        for i in range(self.dim):
            result += 0.06 * np.sin(37 * scaled_x[i]) * np.cos(33 * scaled_x[i]) * np.sin(41 * scaled_x[i]) * np.cos(39 * scaled_x[i])
            
        # Add a multi-modal polynomial component with exponentially decaying coefficients
        for i in range(self.dim):
            result += 0.2 * (np.sin(5 * scaled_x[i]) + 1) * (x[i]**8) * np.exp(-0.03 * np.abs(x[i]))
            
        # Add a dimensionality-dependent penalty term with complex trigonometric interactions
        penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                penalty += 0.03 * np.sin(2 * scaled_x[i]) * np.cos(3 * scaled_x[j]) * np.sin(5 * (x[i] + x[j]))
        result += penalty
        
        return result