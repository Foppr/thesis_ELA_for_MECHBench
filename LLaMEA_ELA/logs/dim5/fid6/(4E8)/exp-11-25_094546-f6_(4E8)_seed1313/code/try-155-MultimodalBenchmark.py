import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for Gaussian mixture components
        self.gaussians = []
        self.weights = []
        num_gaussians = min(8, dim)
        for i in range(num_gaussians):
            center = np.random.uniform(-1, 1, dim)
            cov = np.eye(dim) * np.random.uniform(0.1, 0.5)
            weight = np.random.uniform(0.1, 1.0)
            self.gaussians.append((center, cov))
            self.weights.append(weight)
        self.total_weight = sum(self.weights)
        
    def f(self, x):
        x_norm = x / 5.0
        
        # Chaotic saddle-point component with dynamic scaling
        chaotic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map based chaotic dynamics
            chaotic += 4.0 * xi * (1.0 - xi) * np.sin(20.0 * xi)
        
        # Gaussian mixture component with dynamic weights and positions
        gaussian_sum = 0.0
        for i, (center, cov) in enumerate(self.gaussians):
            diff = x_norm - center
            exponent = -0.5 * np.dot(np.dot(diff, np.linalg.inv(cov)), diff)
            gaussian_sum += self.weights[i] * np.exp(exponent)
        
        # Dynamic curvature modulation based on dimensionality
        curvature_mod = 1.0 + 0.3 * np.sin(self.dim * 0.7) + 0.2 * np.cos(self.dim * 0.4)
        
        # Embedded saddle-point structure with enhanced complexity
        saddle = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale saddle potential
            saddle += (xi**4 - 2.0*xi**2) * np.cos(5.0 * xi)
        
        # Cross-dimensional interaction with varying coupling strength
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = 0.5 + 0.5 * np.sin(0.3 * (i + j))
                cross += coupling * np.exp(-dist**2) * np.sin(10.0 * dist)
        
        # Final combination with dynamic scaling
        return curvature_mod * (0.6 * chaotic + 
                               0.3 * gaussian_sum / self.total_weight + 
                               0.2 * saddle + 
                               0.1 * cross)