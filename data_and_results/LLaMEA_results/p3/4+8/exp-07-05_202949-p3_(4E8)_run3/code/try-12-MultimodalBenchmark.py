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
        
        # Additional sinusoidal terms with different phases
        for i in range(self.dim):
            f_val += 0.15 * np.cos(6 * x[i]) * np.sin(3 * x[i])
        
        # Adaptive penalty term that increases with distance from origin
        penalty = 0.02 * np.sum(x**4) + 0.01 * np.sum(np.abs(x))
        f_val += penalty
        
        # Add a small Gaussian-like perturbation to increase complexity
        f_val += 0.05 * np.exp(-0.5 * np.sum((x / 2.0)**2))
        
        return f_val