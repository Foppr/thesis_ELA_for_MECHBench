import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher degree
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**6)
        
        # Enhanced sinusoidal oscillations with different frequencies
        sinusoidal = np.sum(np.sin(7.0 * x)) * np.exp(-0.15 * np.sum(x**2))
        
        # Additional multimodal component with stronger interaction
        multimodal = 0.7 * np.sum(np.sin(4.0 * x) * np.cos(8.0 * x))
        
        # Radial symmetry term to create more pronounced basins
        radial = 0.3 * np.exp(-0.05 * np.sum((x - np.mean(x))**2))
        
        return polynomial + sinusoidal + multimodal + radial