import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.3, 3.0, 20)
        # Additional cross-dimensional interaction terms with higher order coupling
        self.cross_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Add higher-order polynomial terms for increased complexity
        self.poly_weights = np.random.uniform(-0.5, 0.5, (dim, 4))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with increased number of centers
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.25 ** 2))
        
        # Chaotic sinusoidal perturbation component with higher frequency and amplitude
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(11 * xi) * np.cos(9 * xi) * np.sin(13 * xi) + 
                           0.8 * np.sin(17 * xi) * np.cos(6 * xi) * np.sin(15 * xi) + 
                           0.6 * np.sin(8 * xi) * np.cos(12 * xi) * np.sin(14 * xi) +
                           0.4 * np.sin(19 * xi) * np.cos(5 * xi) * np.sin(16 * xi) +
                           0.2 * np.sin(21 * xi) * np.cos(4 * xi) * np.sin(18 * xi))
        
        # Logarithmic conditioning term with additional sine modulation and higher order terms
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.3 * np.sin(3 * xi))
        
        # Cross-dimensional cubic interaction terms with higher coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j]
        
        # Add quartic polynomial terms for increased complexity
        quartic_term = 0.0
        for i in range(self.dim):
            quartic_term += self.poly_weights[i, 0] * (x[i] ** 4) + \
                           self.poly_weights[i, 1] * (x[i] ** 3) + \
                           self.poly_weights[i, 2] * (x[i] ** 2) + \
                           self.poly_weights[i, 3] * x[i]
        
        # Quadratic basin component with conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.2 * cross_term + 0.1 * quartic_term + 0.05 * quadratic_term
        
        return result