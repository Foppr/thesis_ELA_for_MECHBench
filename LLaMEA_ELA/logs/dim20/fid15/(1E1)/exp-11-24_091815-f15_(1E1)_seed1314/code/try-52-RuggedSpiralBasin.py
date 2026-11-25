import numpy as np

class RuggedSpiralBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create a set of Gaussian peaks with random centers and varying heights
        peak_centers = np.random.uniform(-0.8, 0.8, (10, self.dim))
        peak_heights = np.random.uniform(0.5, 2.0, 10)
        
        gaussian_sum = 0.0
        for i in range(10):
            center = peak_centers[i]
            height = peak_heights[i]
            # Gaussian with varying width and height
            gauss = height * np.exp(-np.sum(((x_norm - center) / 0.3)**2) / 2)
            gaussian_sum += gauss
        
        # Add a global spiral-like gradient that increases complexity
        spiral_term = 0.0
        for i in range(self.dim):
            spiral_term += (x_norm[i] * np.sin(5 * np.pi * x_norm[i]) + 
                           x_norm[i]**2 * np.cos(3 * np.pi * x_norm[i]))
        
        # Add a small noise term to increase ruggedness
        noise = 0.1 * np.random.rand()
        
        # Combine all terms with different weights
        return -gaussian_sum + 2.0 * spiral_term + noise