import numpy as np

class ChaoticRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Generate rotation matrix for chaotic interactions
        rotation_matrix = np.zeros((self.dim, self.dim))
        for i in range(self.dim):
            for j in range(self.dim):
                if i == j:
                    rotation_matrix[i, j] = 1.0
                else:
                    rotation_matrix[i, j] = np.sin((i + 1) * (j + 1) * np.pi / 4.0) * 0.3
        
        # Apply rotation to input
        x_rotated = np.dot(rotation_matrix, x_norm)
        
        # Exponentially decaying sinusoidal components with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        sin_component = np.sum(np.exp(-0.1 * freqs) * np.sin(freqs * x_rotated))
        cos_component = np.sum(np.exp(-0.1 * freqs) * np.cos(freqs * x_rotated))
        
        # Polynomial basin terms with increasing degree
        poly_terms = [0.0] * self.dim
        for i in range(self.dim):
            poly_terms[i] = (i + 1) * (x_rotated[i] ** (i + 2))
        
        polynomial_basin = np.sum(poly_terms)
        
        # Cross-dimensional interaction terms with exponential decay
        cross_terms = 0.0
        for i in range(self.dim - 1):
            cross_terms += np.exp(-0.05 * (i + 1)) * x_rotated[i] * x_rotated[i + 1]
            
        # Fractal-like self-similar structure using recursive sine components
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2 ** (i + 1) * x_rotated[i]) / (2 ** (i + 1))
        
        # Chaotic modulation with time-like parameter
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(x_rotated[i] * np.exp(x_rotated[i])) * np.cos(x_rotated[i] * np.exp(-x_rotated[i]))
        
        # Add a noise term with chaotic behavior
        noise = 0.05 * np.sum(np.sin(10 * x_rotated) + np.cos(10 * x_rotated))
        
        # Combine all components with different weights
        result = (sin_component + cos_component + polynomial_basin + cross_terms + 
                 fractal + chaotic_mod + noise)
        
        return result