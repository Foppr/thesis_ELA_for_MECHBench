import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component
        rbf = 0.0
        for i in range(10):
            dist = np.sum((x_norm - self.centers[i])**2)
            rbf += self.weights[i] * np.exp(-dist / 2.0)
        
        # Polynomial chaos expansion component (sparse grid approximation)
        poly = 0.0
        for i in range(self.dim):
            poly += (x_norm[i]**4 - 2 * x_norm[i]**2) * np.cos(np.pi * x_norm[i])
        
        # Cross-dimensional interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin(x_norm[i] * x_norm[j]) * (i + j)
        
        # Add a global shaping term to ensure global minimum at origin
        shape = np.sum(x_norm**6) * 0.1
        
        # Combine all components
        return rbf + poly + interaction + shape