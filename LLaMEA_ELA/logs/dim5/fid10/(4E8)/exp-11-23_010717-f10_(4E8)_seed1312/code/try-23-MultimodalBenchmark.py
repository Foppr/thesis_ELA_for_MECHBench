import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay component that creates flat regions far from origin
        exp_decay = np.sum(np.exp(-x_normalized**2 / 2.0))
        
        # Polynomial oscillation component with varying frequencies
        poly_oscillation = np.sum((x_normalized**3 - 0.5 * x_normalized**2 + 0.1 * x_normalized) * np.sin(10 * np.pi * x_normalized))
        
        # Quadratic basin term to guide convergence towards origin
        quadratic_basin = 0.5 * np.sum(x_normalized**2)
        
        # Cross-term interaction to increase complexity
        cross_term = 0.3 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Combine all components
        return exp_decay + poly_oscillation + quadratic_basin + cross_term