import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.5, 2.5, 15)
        # Modified cross-dimensional interaction terms with different coupling
        self.cross_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbation component with modified frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(8 * xi) * np.cos(6 * xi) * np.sin(10 * xi) + 
                           0.7 * np.sin(14 * xi) * np.cos(5 * xi) * np.sin(12 * xi) + 
                           0.5 * np.sin(7 * xi) * np.cos(9 * xi) * np.sin(11 * xi) +
                           0.3 * np.sin(16 * xi) * np.cos(4 * xi) * np.sin(13 * xi))
        
        # Logarithmic conditioning term with additional sine modulation
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi))
        
        # Cross-dimensional cubic interaction terms with modified weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 2) * x[j]
        
        # Quadratic basin component with conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with modified weights
        result = 0.3 * gaussian_sum + 0.3 * chaotic_sum + 0.15 * log_conditioning + 0.2 * cross_term + 0.05 * quadratic_term
        
        return result