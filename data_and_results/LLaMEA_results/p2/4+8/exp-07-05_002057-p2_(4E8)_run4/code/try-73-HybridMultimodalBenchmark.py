import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
        # Additional polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (5, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with increased complexity
        gaussian_sum = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbation component with higher frequency terms and modified amplitudes
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (0.8 * np.sin(7 * xi) * np.cos(5 * xi) * np.sin(9 * xi) + 
                           0.9 * np.sin(13 * xi) * np.cos(4 * xi) * np.sin(11 * xi) + 
                           0.5 * np.sin(6 * xi) * np.cos(8 * xi) * np.sin(10 * xi) + 
                           0.3 * np.sin(15 * xi) * np.cos(3 * xi) * np.sin(12 * xi) + 
                           0.6 * np.sin(17 * xi) * np.cos(2 * xi) * np.sin(14 * xi))
        
        # Logarithmic conditioning term with enhanced barrier
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + 0.5 * np.abs(xi)) * np.sin(2 * xi) + 0.1 * np.log(1 + np.abs(xi)) ** 2
        
        # Quadratic basin component with cross-dimensional interactions
        quadratic_term = np.sum(x**2) / self.dim
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * x[i] * x[j] * np.sin(3 * (x[i] + x[j]))
        
        # Polynomial interaction component
        poly_interaction = 0.0
        for i in range(5):
            poly_interaction += np.sum(self.poly_coeffs[i] * (x ** (i+2)))
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.25 * chaotic_sum + 0.2 * log_conditioning + 0.15 * quadratic_term + 0.1 * cross_term + 0.05 * poly_interaction
        
        return result