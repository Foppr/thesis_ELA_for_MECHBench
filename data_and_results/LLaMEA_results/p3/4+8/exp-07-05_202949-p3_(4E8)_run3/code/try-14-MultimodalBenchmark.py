import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global attraction
        f1 = np.sum(x**2)
        
        # Multiple sinusoidal terms with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * x**2))
        
        # Additional multimodal component with higher frequency oscillations
        f3 = 0.3 * np.sum(np.sin(10.0 * x) * np.exp(-0.05 * x**2))
        
        # Cross-terms to increase conditioning difficulty
        f4 = 0.1 * np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.exp(-0.2 * x**2))
        
        # Add a global minimum with controlled curvature
        f5 = 0.05 * np.sum(np.cos(15.0 * x) * np.exp(-0.02 * x**2))
        
        # Combine all terms with optimized weights
        return f1 + f2 + f3 + f4 + f5