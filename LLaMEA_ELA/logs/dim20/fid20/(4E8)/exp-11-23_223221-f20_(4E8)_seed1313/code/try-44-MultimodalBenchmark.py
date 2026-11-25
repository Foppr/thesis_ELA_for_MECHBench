import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute cluster centers for radial basis functions
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying widths
        rbf_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            sigma = 0.5 + 0.5 * np.sin(i)
            rbf_sum += np.exp(-np.sum((x - center)**2) / (2 * sigma**2))
        
        # Adaptive gradient field component
        grad_field = 0.0
        for i in range(self.dim):
            grad_field += (x[i] - np.sin(x[i]))**2
        
        # Periodic boundary interaction
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(np.pi * x[i] / 5.0) * np.cos(np.pi * x[i] / 5.0)
        
        # Clustered minima with varying depths
        cluster_min = 0.0
        for i in range(10):
            center = self.centers[i]
            dist = np.sum((x - center)**2)
            cluster_min += 1.0 / (1.0 + dist * 0.1) * np.exp(-dist / 10.0)
        
        # Combine all components
        result = rbf_sum + 0.5 * grad_field + 0.3 * periodic + 0.2 * cluster_min
        
        return result