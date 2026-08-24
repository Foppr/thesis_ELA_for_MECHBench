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
        # Additional chaotic components with fractional frequencies
        self.frac_freqs = np.random.uniform(1.5, 15.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with increased complexity
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.25 ** 2))
        
        # Chaotic sinusoidal perturbation component with fractional frequencies and higher-order terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.frac_freqs[i]
            chaotic_sum += (np.sin(freq * xi) * np.cos(freq * xi) * np.sin(freq * xi) + 
                           0.7 * np.sin(2 * freq * xi) * np.cos(1.5 * freq * xi) * np.sin(0.5 * freq * xi) + 
                           0.5 * np.sin(3 * freq * xi) * np.cos(2 * freq * xi) * np.sin(freq * xi) +
                           0.3 * np.sin(4 * freq * xi) * np.cos(0.5 * freq * xi) * np.sin(2 * freq * xi))
        
        # Logarithmic conditioning term with additional sine modulation and higher-order polynomials
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.2 * np.sin(3 * xi))
        
        # Cross-dimensional cubic interaction terms with third-order coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        cross_term += self.cross_weights[i, j, k] * (x[i] ** 2) * x[j] * x[k]
        
        # Quadratic basin component with conditioning and additional noise
        quadratic_term = np.sum(x**2) / self.dim + 0.1 * np.random.random()
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.2 * chaotic_sum + 0.25 * log_conditioning + 0.15 * cross_term + 0.1 * quadratic_term
        
        return result