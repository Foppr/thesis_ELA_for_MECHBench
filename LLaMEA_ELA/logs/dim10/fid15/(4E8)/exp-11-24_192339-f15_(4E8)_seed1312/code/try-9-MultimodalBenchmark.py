import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base term
        polynomial = np.sum(x_scaled**4)
        
        # Trigonometric oscillations with varying frequencies
        trigonometric = 0.0
        for i in range(1, min(8, self.dim + 1)):
            trigonometric += np.sin(i * np.pi * x_scaled) * np.cos(i * np.pi * x_scaled)
        
        # Exponential penalty terms to create ruggedness
        exponential = 0.0
        for i in range(self.dim):
            exponential += np.exp(-x_scaled[i]**2) * np.sin(5 * x_scaled[i])
            
        # Chaotic component using sine of squared coordinates
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(x_scaled[i]**2) * np.cos(x_scaled[(i+1) % self.dim]**2)
        
        # Combine all components with different weights
        result = 0.5 * polynomial + 0.3 * trigonometric + 0.2 * exponential + 0.1 * chaotic
        
        # Add a small penalty to ensure global minimum is at origin
        penalty = 0.001 * np.sum(x_scaled**6)
        
        return result + penalty