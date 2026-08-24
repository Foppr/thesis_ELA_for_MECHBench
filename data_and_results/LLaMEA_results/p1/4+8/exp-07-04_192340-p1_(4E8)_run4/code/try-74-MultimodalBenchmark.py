import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic coefficients and radial centers
        self.freqs = np.random.rand(dim) * 10 + 1
        self.centers = np.random.rand(dim) * 10 - 5
        self.conditioning = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial periodic terms with adaptive conditioning
        result = 0.0
        for i in range(self.dim):
            # Radial sinusoidal component with varying frequency and center
            radial_dist = np.sqrt(np.sum((x - self.centers)**2))
            result += np.sin(self.freqs[i] * radial_dist) * self.conditioning[i]
            # Additional periodic term in each dimension
            result += 0.5 * np.sin(2 * self.freqs[i] * x[i]) * np.cos(x[i])
            # Adaptive conditioning term
            result += 0.1 * (x[i] - self.centers[i])**2 * self.conditioning[i]
            
        # Add coupling terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling based on distance and conditioning
                dist = np.abs(x[i] - x[j])
                result += 0.02 * np.sin(dist) * self.conditioning[i] * self.conditioning[j]
                
        # Add global minimum at origin with penalty
        result += 0.0001 * np.sum(x**8)
        
        return result