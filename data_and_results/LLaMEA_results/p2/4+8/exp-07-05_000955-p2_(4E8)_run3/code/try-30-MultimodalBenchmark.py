import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        f2 = 0.2 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x))
        
        # Additional multimodal component with exponential modulation
        f3 = 0.15 * np.sum(np.sin(11.0 * x) * np.exp(-0.5 * x**2))
        
        # Cross-term interactions to increase landscape complexity
        f4 = 0.08 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.sin(6.0 * x))
        
        # Adaptive penalty term based on distance from origin
        f5 = 0.05 * np.sum((x**2) * np.exp(-0.1 * np.sum(x**2)))
        
        return f1 + f2 + f3 + f4 + f5