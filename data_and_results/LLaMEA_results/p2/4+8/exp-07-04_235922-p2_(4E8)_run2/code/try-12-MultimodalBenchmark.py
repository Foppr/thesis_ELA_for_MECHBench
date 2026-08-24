import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2)
        
        # High-frequency sinusoidal perturbations to create many local minima
        f2 = 0.5 * np.sum(np.sin(10.0 * x) * np.exp(-0.2 * x**2))
        
        # Medium-frequency cosine terms with varying amplitudes
        f3 = 0.3 * np.sum(np.cos(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Low-frequency modulated term to create broader landscape features
        f4 = 0.2 * np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.exp(-0.05 * x**2))
        
        # Add a global scaling factor to increase difficulty
        f5 = 0.05 * np.sum(np.exp(-0.1 * x**2) * np.sin(8.0 * x))
        
        # Combine all components
        result = f1 + f2 + f3 + f4 + f5
        
        return result