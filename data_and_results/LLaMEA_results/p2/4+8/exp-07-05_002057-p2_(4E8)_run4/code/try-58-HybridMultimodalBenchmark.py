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
        
        # Enhanced Gaussian radial basis function component
        gaussian_sum = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Enhanced chaotic sinusoidal perturbation component
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(7 * xi) * np.cos(4 * xi) * np.sin(9 * xi) + 
                           0.6 * np.sin(13 * xi) * np.cos(3 * xi) * np.sin(11 * xi) + 
                           0.4 * np.sin(5 * xi) * np.cos(7 * xi) * np.sin(10 * xi) + 
                           0.2 * np.sin(8 * xi) * np.cos(5 * xi) * np.sin(6 * xi))
        
        # Improved logarithmic conditioning term
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += (np.log(1 + np.abs(xi)) * np.sin(xi) * 
                               np.cos(0.5 * xi) * np.tan(0.3 * xi))
        
        # Modified quadratic basin component with cross-terms
        quadratic_term = np.sum(x**2) / self.dim
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] / (self.dim * (self.dim - 1) / 2)
        
        # Combine all components with optimized weights
        result = 0.35 * gaussian_sum + 0.3 * chaotic_sum + 0.25 * log_conditioning + 0.1 * (quadratic_term + 0.05 * cross_term)
        
        return result