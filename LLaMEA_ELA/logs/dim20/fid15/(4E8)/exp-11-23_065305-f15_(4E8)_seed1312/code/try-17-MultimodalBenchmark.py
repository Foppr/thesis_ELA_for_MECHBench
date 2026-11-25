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
        term2 = 0.2 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Higher-order polynomial with trigonometric modulation
        term3 = 0.15 * np.sum((x_norm**6) * np.sin(4 * np.pi * x_norm))
        
        # Add a complex multimodal component with multiple peaks
        term4 = 0.1 * np.sum(np.sin(10 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Combine all terms
        result = term1 + term2 + term3 + term4
        
        return result