import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term with slight modification
        term1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with nested structure and adaptive scaling
        term2 = 0.4 * np.sum(np.sin(12 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Exponential decay modulated sinusoids with variable decay rates for enhanced multimodality
        term3 = 0.25 * np.sum(np.exp(-2 * x_norm**2) * np.sin(10 * np.pi * x_norm))
        
        # Higher-order polynomial with trigonometric modulation and adaptive coefficients
        term4 = 0.18 * np.sum((x_norm**5) * np.cos(5 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms with non-linear coupling and dynamic weights
        interaction = 0
        for i in range(self.dim - 1):
            interaction += (x_norm[i] ** 2) * x_norm[i + 1] * np.sin(np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i + 1])
        term5 = 0.12 * interaction
        
        # Nested trigonometric structure with multiple frequencies and phase shifts
        term6 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Shift global minimum to a non-zero point with additional complexity
        shift = 0.2
        term7 = 0.15 * np.sum((x_norm - shift)**4)
        
        # Additional chaotic component with random-like behavior
        chaotic = 0.08 * np.sum(np.sin(15 * x_norm) * np.cos(13 * x_norm) * np.exp(-x_norm**2))
        
        # Combine all terms with different scaling factors
        result = term1 + term2 + term3 + term4 + term5 + term6 + term7 + chaotic
        
        return result