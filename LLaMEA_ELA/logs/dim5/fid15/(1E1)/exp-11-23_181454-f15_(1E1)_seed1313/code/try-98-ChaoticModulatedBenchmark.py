import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for the chaotic modulation
        self.coefficients = np.random.uniform(0.5, 2.0, dim)
        self.frequencies = np.random.uniform(1.0, 5.0, dim)
        self.barrier_centers = np.random.uniform(-4.0, 4.0, (3, dim))
        self.barrier_heights = np.random.uniform(5.0, 15.0, 3)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Ensure domain bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic term with sinusoidal modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += self.coefficients[i] * np.sin(self.frequencies[i] * x[i]) * np.cos(self.frequencies[i] * x[i])
        
        # Exponential barrier terms to create fitness valleys
        barrier_term = 0.0
        for i in range(3):
            distance = np.sum((x - self.barrier_centers[i])**2)
            barrier_term += self.barrier_heights[i] * np.exp(-distance / 10.0)
        
        # Add a quadratic basin to create a deceptive landscape
        basin_term = 0.05 * np.sum(x**2)
        
        # Add noise for additional complexity
        noise = 0.02 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        return -chaotic_term + barrier_term + basin_term + noise