import numpy as np

class AsymmetricSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sine-cosine periodic interactions with varying frequencies
        periodic = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x)) + \
                   np.sum(np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Asymmetric saddle points with different curvature in each dimension
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 2 * x[i] + 1) * (x[i]**4 - 4 * x[i]**3 + 6 * x[i]**2 - 4 * x[i] + 1)
            
        # Dynamic conditioning based on dimensionality
        condition = 0
        for i in range(self.dim):
            condition += (i + 1) * np.exp(-0.1 * x[i]**2) * np.sin(0.5 * x[i])**2
            
        # Additional penalty terms for large values and global structure
        penalty = 0
        dist_from_origin = np.sqrt(np.sum(x**2))
        penalty += 10 * np.exp(-0.05 * (dist_from_origin - 2)**2) * \
                  np.sin(4 * np.pi * dist_from_origin)**2 + \
                  5 * np.exp(-0.1 * (dist_from_origin - 4)**2) * \
                  np.cos(2 * np.pi * dist_from_origin)**2
        
        # Combine all components with adaptive weights
        return 0.8 * (periodic + saddle + condition + penalty)