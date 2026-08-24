import numpy as np

class OscillatoryConditioningBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix for variable interactions
        self.correlation_matrix = np.random.rand(dim, dim) * 0.5 + 0.25
        self.correlation_matrix = (self.correlation_matrix + self.correlation_matrix.T) / 2
        np.fill_diagonal(self.correlation_matrix, 1.0)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        condition_number = 10.0 + 40.0 * np.random.rand()
        f1 = 0.5 * np.sum((x**2) / (1.0 + condition_number * np.abs(x)))
        
        # Add periodic oscillatory components with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(2.0 * np.pi * x[i] / 3.0) * np.cos(0.5 * np.pi * x[i])
        
        # Add correlated variable interactions
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    f3 += self.correlation_matrix[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Add multi-scale harmonic peaks
        f4 = 0.0
        for i in range(self.dim):
            f4 += 2.0 * np.sin(0.3 * x[i]) * np.cos(0.7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add asymmetric basins with exponential modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.5 * np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(0.5 * x[i])
        
        # Add cross-dimensional interactions with sine modulation
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f6 += np.sin(x[i] + x[j]) * np.cos(0.3 * x[i] * x[j])
        
        # Add dynamic noise component
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + noise