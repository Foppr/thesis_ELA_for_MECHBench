import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Higher-order polynomial terms for increased curvature and complexity
        poly_term = np.sum(0.8 * x_normalized**6 + 0.5 * x_normalized**4 + 0.3 * x_normalized**3 + 0.1 * x_normalized**2)
        
        # Enhanced sinusoidal modulation with multiple frequencies and amplitudes
        sin_term = np.sum(1.5 * np.sin(15 * np.pi * x_normalized) * np.cos(8 * np.pi * x_normalized) + 
                          0.8 * np.sin(7 * np.pi * x_normalized) * np.cos(3 * np.pi * x_normalized))
        
        # Exponential decay with adjustable parameters for varied landscape smoothness
        exp_term = np.sum(np.exp(-x_normalized**2 / 1.5) - 1.0)
        
        # Adaptive coupling term that scales with dimensionality and introduces non-separability
        coupling_term = 0.4 * np.sum(x_normalized[:-1] * x_normalized[1:] * (1 + 0.2 * np.abs(x_normalized[:-1]) * np.abs(x_normalized[1:])))
        
        # Additional interaction term between all dimensions to increase problem difficulty
        interaction_term = 0.2 * np.sum((x_normalized ** 2) * np.exp(-np.sum(x_normalized**2) / (2 * self.dim)))
        
        # Combine all terms with adjusted weights for balanced contribution
        return poly_term + sin_term + exp_term + coupling_term + interaction_term