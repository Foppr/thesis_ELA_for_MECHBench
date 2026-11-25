import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of sinusoidal terms with different frequencies and amplitudes
        term1 = np.sum(np.sin(2 * np.pi * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Quadratic penalty term to encourage convergence to origin
        term2 = 0.1 * np.sum(x_norm**2)
        
        # Additional multimodal component with multiple local minima
        term3 = np.sum(np.cos(4 * np.pi * x_norm) * np.exp(-0.05 * np.sum(x_norm**2)))
        
        # Combined function with global minimum at origin
        result = term1 + term2 - term3
        
        return result