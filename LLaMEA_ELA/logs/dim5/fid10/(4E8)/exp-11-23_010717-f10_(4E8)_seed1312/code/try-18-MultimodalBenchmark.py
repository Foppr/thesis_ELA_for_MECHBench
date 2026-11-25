import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of sinusoidal terms with different frequencies
        f1 = np.sum(np.sin(2 * np.pi * x_norm))
        
        # Quadratic term that penalizes distance from origin
        f2 = np.sum(x_norm**2)
        
        # Additional multimodal component with multiple local minima
        f3 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Cross-terms to increase interaction between dimensions
        f4 = np.sum(np.sin(4 * np.pi * x_norm[:-1]) * np.cos(2 * np.pi * x_norm[1:]))
        
        # Modified quadratic basin with higher conditioning
        f5 = 0.5 * np.sum(x_norm**4)
        
        # Combine terms with different weights to create challenging landscape
        return 0.1 * f1 + 0.3 * f2 + 0.3 * f3 + 0.1 * f4 + 0.2 * f5 + 1.0