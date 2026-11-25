import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # High-frequency chaotic oscillation component
        term1 = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Quadratic penalty term with variable coefficients
        term2 = 0.2 * np.sum(x_norm**2 * (1 + 0.1 * np.sin(5 * np.pi * x_norm)))
        
        # Multiple overlapping global minima with different amplitudes
        term3 = np.sum(np.cos(6 * np.pi * x_norm) * np.exp(-0.02 * np.sum(x_norm**2)) * 
                      (1 + 0.3 * np.sin(3 * np.pi * x_norm)))
        
        # Additional complex multimodal component with saddle points
        term4 = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                      np.exp(-0.05 * np.sum(x_norm**2)) * (1 + 0.2 * np.cos(2 * np.pi * x_norm)))
        
        # Combined function with complex landscape
        result = term1 + term2 - term3 + term4
        
        return result