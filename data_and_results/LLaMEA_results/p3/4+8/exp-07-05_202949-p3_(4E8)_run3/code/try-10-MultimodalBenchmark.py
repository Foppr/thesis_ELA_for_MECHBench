import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Enhanced multimodal components with varying frequencies
        for i in range(self.dim):
            f_val += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
            
        # Additional penalty terms with adaptive scaling
        f_val += 0.05 * np.sum(np.abs(x)**1.5)
        
        # Add a more complex attraction term to guide convergence
        f_val += 0.1 * np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        
        return f_val