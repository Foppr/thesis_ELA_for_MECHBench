import numpy as np

class TemporalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        # Saddle point gradients
        self.saddle_gradients = np.random.randn(10, dim)
        # Temporal correlation parameters
        self.time_factor = np.random.rand(dim) * 0.1 + 0.05
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf += np.exp(-np.sum(diff**2) / (2 * self.widths[i]**2))
        
        # Saddle point gradient structure
        saddle = 0.0
        for i in range(10):
            grad = self.saddle_gradients[i]
            saddle += np.dot(x, grad)**2
        
        # Temporal correlation effect
        temporal = 0.0
        for i in range(self.dim):
            temporal += self.time_factor[i] * x[i] * np.sin(x[i] * (1 + 0.1 * i))
        
        # Cross-dimensional interaction with sinusoidal coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * (i + j)
        
        # Noise injection with time-varying amplitude
        noise = np.random.normal(0, 0.1) * np.sum(np.sin(x))
        
        # Combine components with dynamic weights
        total = 1.5 * rbf - 0.8 * saddle + 0.7 * temporal + 0.3 * cross + 0.2 * noise
        
        return total