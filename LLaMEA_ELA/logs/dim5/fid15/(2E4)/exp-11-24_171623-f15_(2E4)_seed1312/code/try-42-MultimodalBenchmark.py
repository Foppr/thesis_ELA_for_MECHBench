import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay interactions with varying rates
        exp_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_norm[i] - x_norm[j])
                exp_term += np.exp(-5 * distance) * np.sin(3 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Trigonometric wave interference patterns
        wave_term = 0
        for i in range(self.dim):
            wave_term += np.sin(2 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i])
            
        # Adaptive curvature terms based on dimensionality
        curvature_term = 0
        for i in range(self.dim):
            curvature_term += (x_norm[i] ** 4 - 2 * x_norm[i] ** 2) * np.cos(np.pi * x_norm[i])
            
        # Cross-dimensional coupling with polynomial interactions
        poly_coupling = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                poly_coupling += (x_norm[i] ** 3 + x_norm[i+1] ** 3) * np.sin(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Combined result with dynamic weighting
        weight1, weight2, weight3, weight4 = 0.3, 0.25, 0.25, 0.2
        result = weight1 * exp_term + weight2 * wave_term + weight3 * curvature_term + weight4 * poly_coupling
        
        # Add a global scaling and offset to ensure positive fitness values
        result += 0.1 * np.sum(x_norm ** 2)
        
        return result