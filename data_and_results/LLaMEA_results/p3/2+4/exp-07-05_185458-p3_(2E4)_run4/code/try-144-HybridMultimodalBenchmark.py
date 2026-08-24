import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for each dimension
        self.centers = np.random.uniform(-1, 1, (10, dim))
        self.weights = np.random.uniform(0.5, 2.0, 10)
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian mixture component
        gaussian = 0.0
        for i in range(10):
            dist = np.sum((x_norm - self.centers[i]) ** 2)
            gaussian += self.weights[i] * np.exp(-5 * dist)
        
        # Trigonometric wave interference
        wave = 0.0
        for i in range(self.dim):
            wave += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) * np.sin(3 * x_norm[i])
        
        # Adaptive polynomial penalty based on distance from origin
        poly_penalty = 0.0
        dist_from_origin = np.linalg.norm(x_norm)
        for i in range(self.dim):
            poly_penalty += (x_norm[i] ** 4 + 0.5 * x_norm[i] ** 6) * (1 + 0.1 * dist_from_origin)
        
        # Cross-dimensional coupling with dynamic interaction weights
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            weight = 0.5 + 0.5 * np.sin(0.5 * (x_norm[i] + x_norm[j]))
            cross_coupling += weight * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**2 + x_norm[j]**2)
        
        # Dynamic conditioning based on dimension
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (i + 1) * np.sin(x_norm[i] ** 3)
        
        # Combine all components with adaptive scaling
        return 1.5 * gaussian + 0.8 * wave + 0.6 * poly_penalty + 0.4 * cross_coupling + 0.2 * conditioning + 0.1 * np.sum(x_norm**2)