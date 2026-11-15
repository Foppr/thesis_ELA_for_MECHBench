import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.5, 2.5, 15)
        # Additional cross-dimensional interaction terms
        self.cross_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Additional chaotic modulation parameters
        self.chaotic_params = np.random.uniform(0.1, 2.0, (4, dim))
    
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
        
        # Enhanced chaotic sinusoidal perturbation component with dynamic parameters
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Dynamic chaotic terms with varying frequencies and amplitudes
            chaotic_sum += (self.chaotic_params[0, i] * np.sin(7 * xi) * np.cos(5 * xi) * np.sin(9 * xi) + 
                           self.chaotic_params[1, i] * np.sin(13 * xi) * np.cos(4 * xi) * np.sin(11 * xi) + 
                           self.chaotic_params[2, i] * np.sin(6 * xi) * np.cos(8 * xi) * np.sin(10 * xi) +
                           self.chaotic_params[3, i] * np.sin(15 * xi) * np.cos(3 * xi) * np.sin(12 * xi))
        
        # Logarithmic conditioning term with additional sine modulation
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi))
        
        # Cross-dimensional cubic interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j]
        
        # Additional quartic basin component for increased conditioning
        quartic_term = 0.0
        for i in range(self.dim):
            quartic_term += x[i] ** 4
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.25 * chaotic_sum + 0.15 * log_conditioning + 0.2 * cross_term + 0.1 * quartic_term
        
        return result