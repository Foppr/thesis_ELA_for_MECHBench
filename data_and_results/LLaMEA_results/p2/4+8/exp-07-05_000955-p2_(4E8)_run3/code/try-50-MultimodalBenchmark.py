import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        f1 = np.sum(np.sin(3.0 * x) * np.cos(5.0 * x) * np.sin(7.0 * x))
        
        # Radial component with multiple peaks and valleys
        f2 = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.0 * np.pi * x))
        
        # Polynomial penalty terms with mixed degrees
        f3 = np.sum(x**6 + 0.5 * x**4 - 2.0 * x**2)
        
        # Cross-term interactions with trigonometric coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Multi-modal radial basis with varying scales
        centers = np.linspace(-4.0, 4.0, 7)
        f5 = 0.0
        for i in range(7):
            dist = np.sum((x - centers[i % 7])**2)
            f5 += np.exp(-0.2 * dist) * np.sin(2.0 * dist)
        
        # Adaptive scaling based on dimensionality
        f6 = 0.01 * np.sum(x**3 * np.sin(3.0 * x))
        
        # Hybrid exponential and polynomial interactions
        f7 = 0.05 * np.sum(np.exp(-x**2) * x**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7