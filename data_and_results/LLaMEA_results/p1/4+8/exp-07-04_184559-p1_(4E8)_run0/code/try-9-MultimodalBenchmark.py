import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Highly oscillatory component with exponential growth in frequency
        oscillatory = np.sum(np.exp(10 * np.abs(x_norm)) * np.sin(20 * np.pi * x_norm**3))
        
        # Nested multimodal structure with multiple local minima
        nested = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Additional penalty for large values with non-linear scaling
        penalty = 0.5 * np.sum(np.abs(x_norm)**4)
        
        # Combine all components to create a complex, challenging landscape
        return quadratic + 15 * oscillatory + 5 * nested + penalty