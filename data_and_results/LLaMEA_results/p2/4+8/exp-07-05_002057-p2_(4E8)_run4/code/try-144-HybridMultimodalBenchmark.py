import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.3, 3.0, 20)
        # Additional cross-dimensional interaction terms with higher-order coupling
        self.cross_weights = np.random.uniform(-1.0, 1.0, (dim, dim, dim))
        # Additional chaotic components for increased complexity with time-varying coefficients
        self.chaotic_coeffs = np.random.uniform(0.05, 1.5, (7, dim))
        # Additional sine and cosine modulation for increased nonlinearity
        self.modulation_coeffs = np.random.uniform(0.1, 2.0, (3, dim))
    
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
        
        # Enhanced chaotic sinusoidal perturbation component with higher frequency and more complex terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(9 * xi) * np.cos(7 * xi) * np.sin(11 * xi) * np.cos(5 * xi) + 
                           0.7 * np.sin(15 * xi) * np.cos(8 * xi) * np.sin(13 * xi) * np.cos(6 * xi) + 
                           0.5 * np.sin(17 * xi) * np.cos(9 * xi) * np.sin(14 * xi) * np.cos(4 * xi) +
                           0.3 * np.sin(20 * xi) * np.cos(10 * xi) * np.sin(16 * xi) * np.cos(3 * xi) +
                           self.chaotic_coeffs[0, i] * np.sin(19 * xi) * np.cos(2 * xi) * np.sin(18 * xi) * np.cos(7 * xi) +
                           self.chaotic_coeffs[1, i] * np.sin(22 * xi) * np.cos(5 * xi) * np.sin(21 * xi) * np.cos(9 * xi) +
                           self.chaotic_coeffs[2, i] * np.sin(25 * xi) * np.cos(11 * xi) * np.sin(23 * xi) * np.cos(8 * xi) +
                           self.chaotic_coeffs[3, i] * np.sin(24 * xi) * np.cos(12 * xi) * np.sin(26 * xi) * np.cos(10 * xi))
        
        # Logarithmic conditioning term with additional sine modulation and multipliers
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.3 * np.sin(3 * xi))
        
        # Cross-dimensional cubic interaction terms with third-order coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        cross_term += self.cross_weights[i, j, k] * (x[i] ** 3) * x[j] * x[k]
        
        # Additional quintic polynomial terms for increased complexity
        quintic_term = 0.0
        for i in range(self.dim):
            quintic_term += 0.05 * (x[i] ** 5)
        
        # Quadratic basin component with conditioning and additional sine modulation
        quadratic_term = np.sum(x**2) / self.dim
        quadratic_term += 0.1 * np.sum(np.sin(x))
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.15 * cross_term + 0.1 * quintic_term + 0.1 * quadratic_term
        
        return result