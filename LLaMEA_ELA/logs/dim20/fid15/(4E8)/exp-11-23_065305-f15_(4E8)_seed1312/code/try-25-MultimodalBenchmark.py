import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        term1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        term2 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Higher-order polynomial with trigonometric modulation
        term3 = 0.2 * np.sum((x_norm**8) * np.sin(6 * np.pi * x_norm))
        
        # Add a complex multimodal component with multiple peaks and exponential decay
        term4 = 0.25 * np.sum(np.sin(12 * np.pi * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Cross-dimensional interaction terms for increased complexity
        term5 = 0.15 * np.sum(np.sin(8 * np.pi * (x_norm[:-1] + x_norm[1:])) * np.cos(4 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Nested trigonometric modulation with varying frequencies
        term6 = 0.1 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Combine all terms
        result = term1 + term2 + term3 + term4 + term5 + term6
        
        return result