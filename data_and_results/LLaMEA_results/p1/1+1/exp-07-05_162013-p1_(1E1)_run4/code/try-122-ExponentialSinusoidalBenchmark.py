import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.5
        self.beta = 2.0
        self.gamma = 1.5
        self.delta = 0.3
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component
        result = np.sum(self.alpha * np.exp(-self.beta * np.abs(x)))
        
        # Sinusoidal modulation with varying frequencies
        for i in range(self.dim):
            freq = 2 * np.pi * (1 + 0.5 * np.sin(i))
            result += np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.exp(-self.gamma * (x[i] - x[j])**2)
                result += self.delta * interaction * np.sin(x[i] + x[j])
                
        # Polynomial coupling with exponential scaling
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**3) * np.exp(-0.1 * np.abs(x[i]))
        result += 0.1 * poly_term
        
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        return result