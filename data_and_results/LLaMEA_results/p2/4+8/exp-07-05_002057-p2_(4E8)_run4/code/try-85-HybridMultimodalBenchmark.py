import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (30, dim))
        self.weights = np.random.uniform(0.1, 4.0, 30)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(30):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbation component with higher frequency and amplitude terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(13 * xi) * np.cos(11 * xi) * np.sin(17 * xi) + 
                           0.9 * np.sin(21 * xi) * np.cos(9 * xi) * np.sin(19 * xi) + 
                           0.7 * np.sin(14 * xi) * np.cos(13 * xi) * np.sin(16 * xi) + 
                           0.5 * np.sin(23 * xi) * np.cos(8 * xi) * np.sin(20 * xi) + 
                           0.3 * np.sin(25 * xi) * np.cos(7 * xi) * np.sin(22 * xi))
        
        # Logarithmic conditioning term with additional cross-dimensional interaction
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + 0.7 * np.abs(xi)) * np.sin(2.0 * xi) * np.cos(2.0 * xi)
        
        # Additional cross-dimensional polynomial interactions (cubic terms)
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] ** 4) * (x[j] ** 4) * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Quadratic basin component with variable conditioning and additional noise
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.35 * chaotic_sum + 0.18 * log_conditioning + 0.22 * poly_interaction + 0.15 * quadratic_term
        
        return result