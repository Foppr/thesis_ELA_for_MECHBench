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
        # Introduce time-like chaotic parameter
        self.time_param = np.random.uniform(0.1, 2.0)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with more diverse centers
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.25 ** 2))
        
        # Chaotic sinusoidal perturbation component with more complex modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(9 * xi) * np.cos(7 * xi) * np.sin(11 * xi) * np.cos(5 * xi) + 
                           0.7 * np.sin(15 * xi) * np.cos(3 * xi) * np.sin(13 * xi) * np.cos(4 * xi) + 
                           0.5 * np.sin(8 * xi) * np.cos(6 * xi) * np.sin(10 * xi) * np.cos(2 * xi) +
                           0.3 * np.sin(17 * xi) * np.cos(1 * xi) * np.sin(14 * xi) * np.cos(8 * xi) +
                           0.1 * np.sin(20 * xi) * np.cos(9 * xi) * np.sin(16 * xi) * np.cos(7 * xi))
        
        # Logarithmic conditioning term with additional sine modulation and time dependency
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 
                                                        0.3 * np.sin(3 * xi) * self.time_param)
        
        # Cross-dimensional cubic interaction terms with additional coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j]
        
        # Add quartic polynomial terms for enhanced nonlinearity
        poly_term = 0.0
        for i in range(self.dim):
            for p in range(4):
                poly_term += self.poly_weights[i, p] * (x[i] ** (p + 2))
        
        # Quadratic basin component with conditioning and additional noise
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.2 * cross_term + 0.1 * poly_term + 0.05 * quadratic_term
        
        return result