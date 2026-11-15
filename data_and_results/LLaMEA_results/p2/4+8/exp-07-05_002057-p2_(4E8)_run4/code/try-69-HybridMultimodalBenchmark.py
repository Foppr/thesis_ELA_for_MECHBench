import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (8, dim))
        self.weights = np.random.uniform(0.5, 2.0, 8)
        self.amplitudes = np.random.uniform(0.5, 1.5, 8)
        self.frequencies = np.random.uniform(1.0, 3.0, 8)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial landscape component
        poly_sum = 0.0
        for i in range(8):
            center = self.centers[i]
            weight = self.weights[i]
            amplitude = self.amplitudes[i]
            frequency = self.frequencies[i]
            distance = np.sum((x - center) ** 2)
            poly_sum += weight * (amplitude * distance + frequency * np.sin(distance))
        
        # Trigonometric wave interaction component
        wave_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            wave_sum += np.sin(2 * xi) * np.cos(3 * xi) * np.sin(5 * xi) + \
                       0.7 * np.cos(4 * xi) * np.sin(6 * xi) * np.cos(2 * xi) + \
                       0.3 * np.sin(7 * xi) * np.cos(8 * xi) * np.sin(9 * xi)
        
        # Adaptive conditioning term
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            adaptive_conditioning += (1 + 0.1 * np.sin(xi)) * xi**4 + (1 + 0.2 * np.cos(xi)) * xi**2
        
        # Cross-dimensional interaction term
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Combine all components with different weights
        result = 0.35 * poly_sum + 0.3 * wave_sum + 0.2 * adaptive_conditioning + 0.15 * cross_interaction
        
        return result