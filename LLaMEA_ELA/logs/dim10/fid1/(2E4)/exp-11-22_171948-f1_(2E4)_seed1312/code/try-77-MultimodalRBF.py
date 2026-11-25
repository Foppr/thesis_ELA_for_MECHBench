import numpy as np

class MultimodalRBF:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and weights for efficiency
        np.random.seed(42)  # For reproducibility
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Sinusoidal component with varying frequencies and amplitudes
        for i in range(self.dim):
            result += (np.sin(2 * np.pi * x[i]) + 
                      0.5 * np.sin(4 * np.pi * x[i]) + 
                      0.25 * np.sin(8 * np.pi * x[i]) +
                      0.125 * np.sin(16 * np.pi * x[i]))
        
        # Polynomial potential component
        for i in range(self.dim):
            result += 0.1 * x[i]**4 + 0.05 * x[i]**6
        
        # Radial basis function component
        for i in range(10):  # 10 RBFs
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center)**2)
            result += weight * np.exp(-0.5 * distance / (self.dim * 0.5**2))
        
        # Cross-dimensional coupling with modified interaction terms
        for i in range(self.dim - 1):
            result += 0.3 * np.sin(3 * x[i]) * np.cos(2 * x[i+1]) + \
                     0.2 * np.cos(4 * x[i]) * np.sin(5 * x[i+1])
        
        # Add noise-like perturbations with varying scales
        noise_scale = 0.05
        for i in range(self.dim):
            result += noise_scale * np.sin(50 * x[i] + i) * np.cos(25 * x[i] + i)
        
        # Dimensionality-dependent scaling
        result *= (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Final regularization with quartic term
        result += 0.02 * np.sum(x**4) / self.dim
        
        return result