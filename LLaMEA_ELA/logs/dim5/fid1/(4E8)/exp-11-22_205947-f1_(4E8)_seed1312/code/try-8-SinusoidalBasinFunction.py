import numpy as np

class SinusoidalBasinFunction:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for consistent scaling
        x_normalized = x / 5.0
        
        # Exponential attraction term towards center (stronger than original)
        attraction = -2 * np.exp(-np.sum(x_normalized**2) / (2 * 0.3**2))
        
        # High-frequency sinusoidal oscillations with multiple peaks
        oscillation = np.sum(np.sin(10 * np.pi * x_normalized) ** 2)
        
        # Additional saddle-point repulsion term to create complex landscape
        repulsion = 0.5 * np.sum(np.cos(3 * np.pi * x_normalized) ** 2)
        
        # Quadratic penalty for staying away from center (strengthened)
        penalty = 0.2 * np.sum(x_normalized**2)
        
        # Add cross-terms to increase dimensionality interaction
        cross_term = 0.1 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        return attraction + oscillation + repulsion + penalty + cross_term