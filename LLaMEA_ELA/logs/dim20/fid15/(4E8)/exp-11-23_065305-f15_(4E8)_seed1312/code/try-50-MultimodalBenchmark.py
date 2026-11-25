import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        term1 = np.sum(x_norm**2)
        
        # High-frequency nested sinusoidal components with chaotic coupling
        term2 = 0.4 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Adaptive exponential decay modulated sinusoids for enhanced multimodality
        term3 = 0.25 * np.sum(np.exp(-2 * x_norm**2) * np.sin(12 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Higher-order polynomial with trigonometric modulation and dynamic scaling
        term4 = 0.18 * np.sum((x_norm**5) * np.cos(5 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms with non-linear coupling and dynamic weights
        interaction = 0
        for i in range(self.dim - 1):
            interaction += (x_norm[i] ** 3) * x_norm[i + 1] * np.sin(np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i + 1])
        term5 = 0.15 * interaction
        
        # Multi-scale nested trigonometric structure with varying frequencies
        term6 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Shift global minimum with non-uniform transformation and additional complexity
        shift = 0.2
        term7 = 0.12 * np.sum((x_norm - shift)**4 + 0.5 * (x_norm - shift)**6)
        
        # Combine all terms with different scaling factors
        result = term1 + term2 + term3 + term4 + term5 + term6 + term7
        
        return result