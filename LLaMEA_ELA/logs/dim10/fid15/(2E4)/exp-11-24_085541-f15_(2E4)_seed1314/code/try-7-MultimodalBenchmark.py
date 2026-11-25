import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Enhanced sinusoidal terms with varying frequencies and amplitudes
        term1 = np.sum(np.sin(3 * np.pi * x_norm) * np.exp(-0.15 * np.sum(x_norm**2)))
        term2 = np.sum(np.cos(5 * np.pi * x_norm) * np.exp(-0.08 * np.sum(x_norm**2)))
        
        # Adaptive quadratic penalty with dimension-dependent scaling
        term3 = 0.2 * np.sum(x_norm**2) * (1 + 0.1 * np.sin(np.sum(x_norm)))
        
        # Additional multimodal component with higher frequency oscillations
        term4 = np.sum(np.sin(8 * np.pi * x_norm) * np.exp(-0.03 * np.sum(x_norm**2)))
        
        # Combined function with global minimum at origin and enhanced complexity
        result = term1 + term2 - term3 + term4
        
        return result