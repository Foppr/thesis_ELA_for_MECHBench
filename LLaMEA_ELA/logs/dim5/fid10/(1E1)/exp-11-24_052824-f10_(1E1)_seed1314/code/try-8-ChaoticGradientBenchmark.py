import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quad = 0.5 * np.sum(x**2)
        
        # Chaotic sine wave component with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * x[i]) * np.cos(7 * x[i]) + np.sin(3 * x[i])**3
        
        # Saddle point structure with hyperbolic tangent interactions
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction
                saddle += np.tanh(x[i]) * np.tanh(x[j]) * (x[i]**2 - x[j]**2)
        
        # Mixed convexity component with exponential barriers
        mixed = 0
        for i in range(self.dim):
            mixed += np.exp(-x[i]**2) + np.exp(-(x[i] - 2)**2) + np.exp(-(x[i] + 2)**2)
        
        # Non-smooth component with absolute value and step functions
        smoothness = 0
        for i in range(self.dim):
            smoothness += np.abs(x[i])**1.5 + 0.1 * np.sin(50 * x[i])
        
        # Combine all components with different weights
        return quad + 0.7 * chaotic + 0.3 * saddle + 0.5 * mixed + 0.2 * smoothness + 10 * np.sum(np.sin(x)**2)