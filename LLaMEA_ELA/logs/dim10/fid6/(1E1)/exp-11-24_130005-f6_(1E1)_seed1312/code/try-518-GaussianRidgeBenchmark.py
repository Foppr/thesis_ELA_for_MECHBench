import numpy as np

class GaussianRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for periodic boundary effects
        self.periods = np.linspace(1.0, 3.0, min(5, dim))
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Gaussian mixture components with varying covariances and weights
        gaussian_sum = 0.0
        centers = np.linspace(-0.8, 0.8, 9)
        weights = np.exp(-np.arange(9) * 0.3)
        weights = weights / np.sum(weights)
        
        for i, (center, weight) in enumerate(zip(centers, weights)):
            cov = np.diag(np.ones(self.dim) * (0.2 + 0.1 * i))
            # Add some correlation between dimensions
            if self.dim > 1:
                cov[0, 1] = 0.1 * np.sin(i)
                cov[1, 0] = 0.1 * np.sin(i)
            
            diff = x_scaled - center
            exponent = -0.5 * np.dot(np.dot(diff, np.linalg.inv(cov)), diff)
            gaussian_sum += weight * np.exp(exponent)
        
        # Polynomial interaction terms with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                poly_term += (x_scaled[i] * x_scaled[j])**3
                
        # Periodic boundary effects with multiple frequencies
        periodic = 0.0
        for i in range(min(5, self.dim)):
            freq = self.periods[i]
            periodic += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
            
        # Combined function with weighted components
        return 1.5 * gaussian_sum + 0.8 * poly_term + 0.6 * periodic