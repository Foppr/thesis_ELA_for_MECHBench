import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic exponential decay with sine modulation
        f1 = np.sum(np.exp(-np.abs(x_scaled) ** 1.5) * np.sin(5 * np.pi * x_scaled ** 2))
        
        # Polynomial interaction with cross-dimensional coupling
        f2 = np.sum(x_scaled**6 + 0.5 * x_scaled[:-2]**2 * x_scaled[2:] + 0.3 * x_scaled[:-1] * x_scaled[1:])
        
        # Trigonometric coupling creating saddle points
        f3 = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) * 
                   np.exp(-0.5 * np.sum(x_scaled**2)))
        
        # High-frequency oscillations with varying amplitude
        f4 = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) * 
                   (1 + 0.1 * np.sin(8 * x_scaled)))
        
        # Additional chaotic component with non-smooth regions
        f5 = np.sum(np.abs(x_scaled) ** 1.3 * np.exp(-np.abs(x_scaled)) * 
                   np.cos(3 * np.pi * x_scaled**2))
        
        # Combined function with complex landscape characteristics
        return 1.5 * f1 + 0.8 * f2 + 0.6 * f3 + 0.4 * f4 + 0.2 * f5 + np.sum(np.exp(-x_scaled**3))