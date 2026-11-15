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
            chaotic_sum += (np.sin(9 * xi) * np.cos(7 * xi) * np.sin(11 * xi) + 
                           0.8 * np.sin(15 * xi) * np.cos(5 * xi) * np.sin(13 * xi) + 
                           0.6 * np.sin(8 * xi) * np.cos(9 * xi) * np.sin(12 * xi) + 
                           0.4 * np.sin(17 * xi) * np.cos(4 * xi) * np.sin(14 * xi) + 
                           0.2 * np.sin(19 * xi) * np.cos(3 * xi) * np.sin(16 * xi))
        
        # Logarithmic conditioning term with additional cross-dimensional interaction
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + 0.5 * np.abs(xi)) * np.sin(1.5 * xi) * np.cos(1.5 * xi)
        
        # Additional cross-dimensional polynomial interactions (cubic terms)
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] ** 3) * (x[j] ** 3) * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Quadratic basin component with variable conditioning and additional noise
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.3 * chaotic_sum + 0.15 * log_conditioning + 0.2 * poly_interaction + 0.1 * quadratic_term
        
        return result