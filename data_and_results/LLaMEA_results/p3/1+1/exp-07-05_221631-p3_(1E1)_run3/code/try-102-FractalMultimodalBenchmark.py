import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and widths for fractal structure
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (100, dim))
        self.widths = np.random.uniform(0.5, 2.0, 100)
        # Trigonometric penalty parameters
        self.penalty_freq = np.random.uniform(1.0, 5.0, dim)
        self.penalty_amp = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute sum of Gaussian functions
        f_val = 0.0
        for i in range(100):
            diff = x - self.centers[i]
            f_val -= np.exp(-0.5 * np.sum((diff / self.widths[i])**2))
        
        # Add trigonometric penalty to increase complexity
        for i in range(self.dim):
            f_val += self.penalty_amp[i] * np.sin(self.penalty_freq[i] * x[i])**2
        
        # Add a small constant to ensure positive fitness values
        f_val += 1.0
        
        return f_val