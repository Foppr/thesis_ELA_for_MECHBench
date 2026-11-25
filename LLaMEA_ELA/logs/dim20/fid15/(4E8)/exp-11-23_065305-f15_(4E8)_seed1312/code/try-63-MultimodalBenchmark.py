import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        term1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with nested structure
        term2 = 0.4 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        
        # Exponential decay modulated sinusoids for enhanced multimodality
        term3 = 0.3 * np.sum(np.exp(-2.5 * x_norm**2) * np.sin(12 * np.pi * x_norm))
        
        # Higher-order polynomial with trigonometric modulation
        term4 = 0.2 * np.sum((x_norm**5) * np.cos(6 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms with non-linear coupling
        interaction = 0
        for i in range(self.dim - 1):
            interaction += (x_norm[i] ** 3) * x_norm[i + 1] * np.sin(2 * np.pi * x_norm[i])
        term5 = 0.15 * interaction
        
        # Nested trigonometric structure with multiple frequencies
        term6 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Shift global minimum to a non-zero point and add additional complexity
        shift = 0.2
        term7 = 0.15 * np.sum((x_norm - shift)**4)
        
        # Additional chaotic exponential decay with higher frequency
        term8 = 0.25 * np.sum(np.exp(-1.5 * x_norm**3) * np.sin(18 * np.pi * x_norm))
        
        # New cross-dimensional interference with cubic coupling and altered frequency
        cubic_interaction = 0
        for i in range(self.dim - 2):
            cubic_interaction += (x_norm[i] ** 2) * (x_norm[i + 1] ** 2) * x_norm[i + 2] * np.cos(1.5 * np.pi * x_norm[i])
        term9 = 0.12 * cubic_interaction
        
        # Add a new chaotic component with quartic exponential decay
        term10 = 0.18 * np.sum(np.exp(-x_norm**4) * np.sin(20 * np.pi * x_norm))
        
        # Combine all terms with different scaling factors
        result = term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8 + term9 + term10
        
        return result