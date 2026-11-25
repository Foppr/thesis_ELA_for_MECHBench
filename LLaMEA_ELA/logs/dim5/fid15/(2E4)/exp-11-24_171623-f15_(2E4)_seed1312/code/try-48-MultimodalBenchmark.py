import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis functions with adaptive centers
        rbf_term = 0
        num_centers = min(10, self.dim)
        centers = np.random.uniform(-1, 1, (num_centers, self.dim))
        
        for i in range(num_centers):
            distance = np.sum((x_norm - centers[i]) ** 2)
            rbf_term += np.exp(-distance * 10) * np.sin(np.pi * np.sum(x_norm * centers[i]))
        
        # Sinusoidal modulation with varying frequencies
        sin_mod = 0
        for i in range(self.dim):
            sin_mod += np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            
        # Cross-dimensional quadratic coupling with variable weights
        quad_coupling = 0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                quad_coupling += (x_norm[i] ** 2 + x_norm[i+1] ** 2) * np.cos(np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Adaptive curvature with dimension-dependent scaling
        curvature_term = 0
        for i in range(self.dim):
            curvature_term += (x_norm[i] ** 4 - 3 * x_norm[i] ** 2 + 2) * np.sin(2 * np.pi * x_norm[i])
            
        # Combined result with dynamic weighting
        weight1, weight2, weight3, weight4 = 0.25, 0.3, 0.25, 0.2
        result = weight1 * rbf_term + weight2 * sin_mod + weight3 * curvature_term + weight4 * quad_coupling
        
        # Add a global scaling and offset to ensure positive fitness values
        result += 0.05 * np.sum(x_norm ** 2)
        
        return result