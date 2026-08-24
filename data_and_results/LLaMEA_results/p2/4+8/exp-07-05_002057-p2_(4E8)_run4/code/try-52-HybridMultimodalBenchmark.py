import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
    
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
        
        # Chaotic sinusoidal perturbation component with higher frequency terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(7 * xi) * np.cos(5 * xi) * np.sin(9 * xi) + 
                           0.7 * np.sin(13 * xi) * np.cos(4 * xi) * np.sin(11 * xi) + 
                           0.5 * np.sin(6 * xi) * np.cos(8 * xi) * np.sin(10 * xi) + 
                           0.3 * np.sin(15 * xi) * np.cos(3 * xi) * np.sin(12 * xi))
        
        # Logarithmic conditioning term with additional cross-dimensional interaction
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * np.sin(xi) * np.cos(xi)
        
        # Additional cross-dimensional polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] ** 3) * (x[j] ** 2) * np.sin(x[i] + x[j])
        
        # Quadratic basin component with variable conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.25 * chaotic_sum + 0.2 * log_conditioning + 0.15 * poly_interaction + 0.1 * quadratic_term
        
        return result