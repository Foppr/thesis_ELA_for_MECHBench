import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term to guide optimization towards origin
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced periodic terms with higher frequencies and additional harmonics
        periodic = np.sum(1.5 * np.sin(15 * np.pi * x_scaled) ** 2 + 
                         0.8 * np.sin(30 * np.pi * x_scaled) ** 2 +
                         0.3 * np.sin(45 * np.pi * x_scaled) ** 2)
        
        # Modified exponential interaction term with different curvature
        exponential = np.exp(-np.sum(x_scaled**2) / 1.5) * np.sum(np.cos(4 * x_scaled)**2)
        
        # Add a modified sigmoid-like penalty for large values
        penalty = 1.0 / (1.0 + np.exp(-np.sum(x_scaled**2) + 1.5))
        
        # Combine all terms with adjusted weights
        result = 0.3 * quadratic + 0.45 * periodic + 0.2 * exponential + 0.05 * penalty
        
        return result