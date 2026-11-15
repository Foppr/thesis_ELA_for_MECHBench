import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.3, 2.5, 10)
        self.conditioning_factors = np.random.uniform(0.2, 1.8, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gauss_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gauss_sum += weight * np.exp(-distance / (2 * 0.5 ** 2))
        
        # Chaotic sinusoidal perturbations with modified frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (0.7 * np.sin(7 * xi) * np.cos(5 * xi) * np.tan(3 * xi) + 
                           0.5 * np.sin(9 * xi) * np.cos(6 * xi) * np.tan(4 * xi) + 
                           0.3 * np.sin(4 * xi) * np.cos(7 * xi) * np.tan(5 * xi))
        
        # Logarithmic conditioning with dimension-specific scaling
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += self.conditioning_factors[i] * np.log(1 + xi**2) * np.sin(xi)
        
        # Cross-dimensional cubic interactions
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += (x[i] ** 3) * (x[j] ** 3) * np.sin(x[i] + x[j])
        
        # Quadratic basin component with variable conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.4 * gauss_sum + 0.3 * chaotic_sum + 0.2 * log_conditioning + 0.08 * cubic_interaction + 0.02 * quadratic_term
        
        return result