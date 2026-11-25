import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic exponential decay with sine modulation and enhanced nonlinearity
        f1 = np.sum(np.exp(-np.abs(x_scaled) ** 2.0) * np.sin(7 * np.pi * x_scaled ** 2))
        
        # Polynomial interaction with cross-dimensional coupling and increased conditioning
        f2 = np.sum(x_scaled**5 + 0.7 * x_scaled[:-2]**2 * x_scaled[2:] + 0.4 * x_scaled[:-1] * x_scaled[1:])
        
        # Trigonometric coupling creating saddle points with modified frequency
        f3 = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled) * 
                   np.exp(-0.3 * np.sum(x_scaled**2)))
        
        # High-frequency oscillations with varying amplitude and additional chaotic term
        f4 = np.sum(np.sin(18 * x_scaled) * np.cos(15 * x_scaled) * 
                   (1 + 0.15 * np.sin(9 * x_scaled)) + 0.05 * np.sin(25 * x_scaled))
        
        # Additional chaotic component with non-smooth regions and modified scaling
        f5 = np.sum(np.abs(x_scaled) ** 1.4 * np.exp(-np.abs(x_scaled)) * 
                   np.cos(4 * np.pi * x_scaled**2) + 0.1 * np.sin(6 * x_scaled))
        
        # Combined function with complex landscape characteristics
        return 1.7 * f1 + 0.9 * f2 + 0.7 * f3 + 0.5 * f4 + 0.3 * f5 + np.sum(np.exp(-x_scaled**4))