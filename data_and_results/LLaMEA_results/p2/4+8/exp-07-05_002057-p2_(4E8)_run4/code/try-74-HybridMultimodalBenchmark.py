import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.2, 3.0, 20)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.25 ** 2))
        
        # Chaotic sinusoidal perturbation component with higher frequency and amplitude terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(10 * xi) * np.cos(8 * xi) * np.sin(12 * xi) + 
                           0.9 * np.sin(16 * xi) * np.cos(6 * xi) * np.sin(14 * xi) + 
                           0.7 * np.sin(9 * xi) * np.cos(10 * xi) * np.sin(13 * xi) + 
                           0.5 * np.sin(18 * xi) * np.cos(5 * xi) * np.sin(15 * xi) + 
                           0.3 * np.sin(20 * xi) * np.cos(4 * xi) * np.sin(17 * xi))
        
        # Logarithmic conditioning term with additional cross-dimensional interaction
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + 0.6 * np.abs(xi)) * np.sin(2.0 * xi) * np.cos(2.0 * xi)
        
        # Additional cross-dimensional polynomial interactions (cubic terms)
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] ** 3) * (x[j] ** 3) * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Quadratic basin component with variable conditioning and additional noise
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.25 * chaotic_sum + 0.18 * log_conditioning + 0.22 * poly_interaction + 0.05 * quadratic_term
        
        return result