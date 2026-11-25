import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic exponential decay with sine modulation and enhanced nonlinearity
        f1 = np.sum(np.exp(-np.abs(x_scaled) ** 2.5) * np.sin(6 * np.pi * x_scaled ** 2))
        
        # Polynomial interaction with cross-dimensional coupling and increased conditioning
        f2 = np.sum(x_scaled**4 + 0.8 * x_scaled[:-2]**2 * x_scaled[2:] + 0.3 * x_scaled[:-1] * x_scaled[1:])
        
        # Trigonometric coupling creating saddle points with modified frequency
        f3 = np.sum(np.sin(2.5 * np.pi * x_scaled) * np.cos(4.5 * np.pi * x_scaled) * 
                   np.exp(-0.25 * np.sum(x_scaled**2)))
        
        # High-frequency oscillations with varying amplitude and additional chaotic term
        f4 = np.sum(np.sin(16 * x_scaled) * np.cos(13 * x_scaled) * 
                   (1 + 0.12 * np.sin(8 * x_scaled)) + 0.04 * np.sin(22 * x_scaled))
        
        # Additional chaotic component with non-smooth regions and modified scaling
        f5 = np.sum(np.abs(x_scaled) ** 1.6 * np.exp(-np.abs(x_scaled)) * 
                   np.cos(3.5 * np.pi * x_scaled**2) + 0.08 * np.sin(5 * x_scaled))
        
        # Combined function with complex landscape characteristics
        return 1.5 * f1 + 1.1 * f2 + 0.8 * f3 + 0.6 * f4 + 0.4 * f5 + np.sum(np.exp(-x_scaled**3))