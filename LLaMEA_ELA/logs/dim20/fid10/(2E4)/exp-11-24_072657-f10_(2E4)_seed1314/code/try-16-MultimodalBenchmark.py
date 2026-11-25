import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with random centers
        centers = np.random.uniform(-1, 1, self.dim)
        exp_term = np.sum(np.exp(-5 * (x_norm - centers)**2))
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(self.dim):
            rbf_sum += np.exp(-np.sum((x_norm - np.roll(centers, i))**2) / (2 * 0.5**2))
        
        # Cross-dimensional coupling through product of sinusoids
        coupling = np.prod(np.sin(np.pi * x_norm))
        
        # Polynomial interaction with quadratic and quartic terms
        poly_term = np.sum(x_norm**2 + 0.1 * x_norm**4)
        
        # Modified Schwefel function component for long-range dependencies
        schwefel = np.sum(np.abs(x_norm) * np.sin(np.sqrt(np.abs(x_norm))))
        
        # Additional harmonic structure with varying frequencies
        harmonic = np.sum(np.sin(10 * np.pi * x_norm**3))
        
        # Combine all terms with adaptive weights
        result = 0.3 * exp_term + 0.2 * rbf_sum + 0.4 * coupling + 0.1 * poly_term + 0.5 * schwefel + 0.3 * harmonic
        
        # Add small random perturbation for additional challenge
        noise = 0.001 * np.random.random()
        
        return result + noise