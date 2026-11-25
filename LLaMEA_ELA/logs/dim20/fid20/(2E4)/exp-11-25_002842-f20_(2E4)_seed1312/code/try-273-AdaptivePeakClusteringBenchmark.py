import numpy as np

class AdaptivePeakClusteringBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate cluster centers for peaks
        self.centers = np.random.uniform(-4.0, 4.0, (12, dim))
        # Peak heights and widths
        self.heights = np.random.uniform(1.0, 10.0, 12)
        self.widths = np.random.uniform(0.5, 2.0, 12)
        # Adaptive scaling factors per dimension
        self.scaling = np.random.uniform(0.5, 1.5, dim)
        # Exponential barrier parameters
        self.barrier_strength = np.random.uniform(0.5, 2.0, dim)
        self.barrier_width = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Sinusoidal oscillation component
        for i in range(self.dim):
            result += np.sin(x[i]) * np.cos(2 * x[i]) * self.scaling[i]
            
        # Adaptive peak clustering component
        peak_sum = 0.0
        for j in range(12):
            distance = np.sum((x - self.centers[j]) ** 2)
            peak_sum += self.heights[j] * np.exp(-distance / (2 * self.widths[j]**2))
            
        # Exponential barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_strength[i] * np.exp(-np.abs(x[i]) / self.barrier_width[i])
            
        # Combine components with dynamic weighting
        total = 0.3 * result + 0.5 * peak_sum - 0.2 * barrier_sum
        
        return total