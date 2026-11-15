import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with varying degrees
        f1 = np.sum(x**4) / 4.0
        
        # Trigonometric components with varying frequencies
        f2 = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-3.0, 3.0, 5)
        f3 = 0.0
        for i in range(5):
            for j in range(self.dim):
                f3 += np.exp(-0.5 * ((x[j] - centers[i % 5])**2) / 1.0)
        
        # Cross-term interactions with exponential decay
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Adaptive scaling based on dimensionality
        f5 = 0.1 * np.sum(x**2 * np.sin(4.0 * x))
        
        # Cubic and quartic nonlinearities
        f6 = 0.05 * np.sum(x**3 * np.cos(2.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6