import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic basin with varying coefficients
        quadratic_sum = np.sum((0.5 + 0.5 * np.sin(np.pi * x_normalized)) * x_normalized**2)
        
        # Highly oscillatory sinusoidal terms with exponentially increasing frequencies
        freq_multiplier = 2.0
        sinusoidal_sum = np.sum(np.sin(freq_multiplier ** (np.arange(self.dim) + 1) * np.pi * x_normalized))
        
        # Polynomial penalty with mixed degrees for increased complexity
        penalty = 0.2 * np.sum(x_normalized**6 + 0.3 * x_normalized**8)
        
        # Cross-dimensional interaction terms to increase search difficulty
        cross_term = np.sum((x_normalized[:-1] - x_normalized[1:])**4)
        
        # Combine all components to create a highly multimodal function
        return quadratic_sum + sinusoidal_sum + penalty + 0.5 * cross_term