import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Add chaotic sinusoidal components with varying frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
        
        # Add exponential barriers around specific points
        barriers = 0.0
        barrier_centers = np.array([[-2.0, 2.0] * (self.dim // 2 + 1)])[:self.dim]
        for i in range(self.dim):
            barriers += 2.0 * np.exp(-0.5 * (x[i] - barrier_centers[0, i])**2)
        
        # Create periodic global minima clusters
        cluster_term = 0.0
        cluster_centers = np.array([0.0, 3.0, -3.0])
        for i in range(self.dim):
            min_dist = float('inf')
            for center in cluster_centers:
                dist = np.abs(x[i] - center)
                if dist < min_dist:
                    min_dist = dist
            cluster_term += np.exp(-min_dist / 2.0)
        
        # Combine all terms with different weights
        result = 0.5 * quadratic + 0.3 * sinusoidal + 0.2 * barriers + 0.1 * cluster_term
        
        return result