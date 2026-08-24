import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (20, dim))
        self.weights = np.random.uniform(0.5, 3.0, 20)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with more centers
        gaussian_sum = 0.0
        for i in range(20):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.25 ** 2))
        
        # Enhanced chaotic sinusoidal perturbation with higher frequency terms and more complex combinations
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            chaotic_sum += (np.sin(9 * xi) * np.cos(7 * xi) * np.sin(11 * xi) * np.cos(5 * xi) + 
                           0.8 * np.sin(15 * xi) * np.cos(6 * xi) * np.sin(13 * xi) * np.cos(4 * xi) + 
                           0.6 * np.sin(8 * xi) * np.cos(9 * xi) * np.sin(10 * xi) * np.cos(3 * xi) + 
                           0.4 * np.sin(17 * xi) * np.cos(2 * xi) * np.sin(14 * xi) * np.cos(8 * xi) + 
                           0.3 * np.sin(12 * xi) * np.cos(10 * xi) * np.sin(16 * xi) * np.cos(6 * xi))
        
        # Enhanced logarithmic conditioning term with multiple barrier components
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += (np.log(1 + np.abs(xi)) * np.sin(xi) * np.cos(xi) + 
                               0.5 * np.log(1 + np.abs(xi)**2) * np.sin(xi**2) * np.cos(xi**2) + 
                               0.3 * np.log(1 + np.abs(xi)**3) * np.sin(xi**3) * np.cos(xi**3))
        
        # Increased cross-dimensional polynomial interactions with higher-order terms
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i] ** 4) * (x[j] ** 3) * np.sin(x[i] + x[j]) + \
                                   (x[i] ** 3) * (x[j] ** 4) * np.cos(x[i] - x[j]) + \
                                   0.5 * (x[i] ** 2) * (x[j] ** 5) * np.tan(x[i] * x[j])
        
        # Enhanced quadratic basin component with variable conditioning and additional terms
        quadratic_term = np.sum(x**2) / self.dim + 0.1 * np.sum(x**4) / (self.dim**2)
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.3 * chaotic_sum + 0.25 * log_conditioning + 0.15 * poly_interaction + 0.05 * quadratic_term
        
        return result