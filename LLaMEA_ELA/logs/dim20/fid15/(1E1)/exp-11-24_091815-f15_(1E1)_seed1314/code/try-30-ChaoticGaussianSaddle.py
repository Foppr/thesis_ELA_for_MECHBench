import numpy as np

class ChaoticGaussianSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Precompute constants for chaotic behavior
        self.chaotic_const = 4.0
        self.gauss_centers = np.random.uniform(-3.0, 3.0, (5, dim))
        self.gauss_weights = np.random.rand(5)
        self.gauss_weights /= np.sum(self.gauss_weights)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic saddle term using logistic map-like dynamics
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += self.chaotic_const * x_norm[i] * (1 - x_norm[i]**2)
        
        # Gaussian mixture component with varying scales and positions
        gauss_term = 0.0
        for i in range(5):
            diff = x_norm - self.gauss_centers[i]
            scale = 0.5 + 0.5 * np.sin(i)  # Varying scales
            gauss_term += self.gauss_weights[i] * np.exp(-np.sum(diff**2) / (2 * scale**2))
        
        # Polynomial correlation terms to create complex interactions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimensionality
                poly_term += x_norm[i] * x_norm[j] * (i + j)
        
        # Add a sinusoidal modulation to increase nonlinearity
        sin_term = np.sum(np.sin(3 * x_norm) * np.cos(2 * x_norm))
        
        # Combine all terms with different weights
        return chaotic_term + gauss_term + poly_term + sin_term