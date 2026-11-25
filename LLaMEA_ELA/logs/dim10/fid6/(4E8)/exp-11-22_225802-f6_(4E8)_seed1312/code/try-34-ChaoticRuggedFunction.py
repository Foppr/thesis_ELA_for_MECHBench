import numpy as np

class ChaoticRuggedFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for trigonometric stability
        scaled_x = x * (np.pi / 5.0)
        
        # Exponential decay base with chaotic modulation
        result = 0.0
        for i in range(self.dim):
            result += np.exp(-0.5 * x[i]**2) * np.sin(scaled_x[i])**2
            
        # Add power-law interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                result += 0.3 * (distance**(-1.5)) * np.cos(3 * scaled_x[i]) * np.sin(2 * scaled_x[j])
                
        # Introduce chaotic sinusoidal coupling
        for i in range(self.dim):
            result += 0.2 * np.sin(4 * scaled_x[i]) * np.cos(5 * scaled_x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Add polynomial basin terms with varying exponents
        for i in range(self.dim):
            result += 0.1 * (x[i]**6) + 0.05 * (x[i]**3)
            
        # Include cross-dimensional quadratic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j])**2
                
        result += 0.15 * cross_term
        
        # Add a global scaling factor based on norm
        norm = np.linalg.norm(x)
        result *= (1.0 + 0.2 * norm**2)
        
        # Introduce asymmetric ruggedness with step functions
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.08 * np.exp(-x[i]**2) * np.sin(10 * scaled_x[i])
            else:
                result += 0.08 * np.exp(x[i]**2) * np.cos(8 * scaled_x[i])
                
        # Add small constant offset
        result += 1.0
        
        return result