import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add trigonometric chaotic components with radial basis influence
        for i in range(self.dim):
            xi = x[i]
            # Chaotic trigonometric terms
            result += np.sin(7 * xi) * np.cos(5 * xi) * np.exp(-0.1 * xi**2) + \
                      np.cos(9 * xi) * np.sin(4 * xi) * np.exp(-0.05 * xi**2)
        
        # Add radial basis function interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Radial distance between dimensions
                r = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 0.3 * np.exp(-r**2) * np.sin(2 * np.pi * r) * np.cos(0.5 * (x[i] + x[j]))
        
        # Add nested multi-modal structure with dynamic scaling
        for i in range(self.dim):
            xi = x[i]
            # Nested sinusoidal modulations with varying frequencies
            result += 0.5 * np.sin(3 * xi) * np.sin(9 * xi) * np.sin(15 * xi) + \
                      0.4 * np.cos(2 * xi) * np.cos(6 * xi) * np.cos(12 * xi)
        
        # Add dynamic conditioning based on dimensionality
        conditioning = 1.0 + 0.3 * np.sin(0.7 * self.dim) * np.cos(0.4 * self.dim)
        result *= conditioning
        
        # Add cross-dimensional coupling with exponential barriers
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.exp(-0.3 * (x[i] - 3)**2) + np.exp(-0.3 * (x[i] + 3)**2) + \
                       np.exp(-0.2 * (x[i] - 1)**2) + np.exp(-0.2 * (x[i] + 1)**2)
        result += 0.6 * barrier
        
        # Add noise component with multi-scale sinusoidal interference
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(15 * x[i]) * np.cos(17 * x[i]) * np.exp(-0.08 * x[i]**2) + \
                     np.cos(23 * x[i]) * np.sin(29 * x[i]) * np.exp(-0.06 * x[i]**2)
        result += 0.03 * noise
        
        return result