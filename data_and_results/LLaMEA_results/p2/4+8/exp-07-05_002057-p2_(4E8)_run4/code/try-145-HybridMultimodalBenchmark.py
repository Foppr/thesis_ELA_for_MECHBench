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
        self.chaotic_params = np.random.uniform(0.1, 2.0, 10)
        # New enhanced conditioning and interaction terms
        self.conditioning_weights = np.random.uniform(0.1, 1.0, dim)
        self.cubic_weights = np.random.uniform(-0.3, 0.3, (dim, dim, dim))
    
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
        
        # Enhanced chaotic sinusoidal perturbation component with more complex modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add more chaotic terms with varying frequencies and amplitudes
            chaotic_sum += (self.chaotic_params[0] * np.sin(7 * xi) * np.cos(5 * xi) * np.sin(9 * xi) + 
                           self.chaotic_params[1] * np.sin(13 * xi) * np.cos(4 * xi) * np.sin(11 * xi) + 
                           self.chaotic_params[2] * np.sin(6 * xi) * np.cos(8 * xi) * np.sin(10 * xi) +
                           self.chaotic_params[3] * np.sin(15 * xi) * np.cos(3 * xi) * np.sin(12 * xi) +
                           self.chaotic_params[4] * np.sin(2 * xi) * np.cos(17 * xi) * np.sin(19 * xi) +
                           self.chaotic_params[5] * np.sin(23 * xi) * np.cos(14 * xi) * np.sin(21 * xi) +
                           self.chaotic_params[6] * np.sin(25 * xi) * np.cos(22 * xi) * np.sin(27 * xi) +
                           self.chaotic_params[7] * np.sin(31 * xi) * np.cos(29 * xi) * np.sin(33 * xi) +
                           self.chaotic_params[8] * np.sin(37 * xi) * np.cos(35 * xi) * np.sin(39 * xi) +
                           self.chaotic_params[9] * np.sin(41 * xi) * np.cos(43 * xi) * np.sin(47 * xi))
        
        # Logarithmic conditioning term with additional sine modulation
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += np.log(1 + np.abs(xi)) * (np.sin(xi) + 0.5 * np.sin(2 * xi) + 0.3 * np.sin(3 * xi))
        
        # Cross-dimensional cubic interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_term += self.cross_weights[i, j] * (x[i] ** 3) * x[j]
        
        # Enhanced cubic cross-dimensional interactions
        cubic_cross_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        cubic_cross_term += self.cubic_weights[i, j, k] * x[i] * x[j] * x[k]
        
        # Quadratic basin component with conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Add a novel hyperbolic tangent component for additional complexity
        tanh_component = 0.0
        for i in range(self.dim):
            tanh_component += np.tanh(x[i]) * np.sin(x[i])
        
        # Add a new conditioning component with varying weights
        conditioning_component = 0.0
        for i in range(self.dim):
            conditioning_component += self.conditioning_weights[i] * (x[i] ** 4)
        
        # Combine all components with different weights
        result = 0.25 * gaussian_sum + 0.2 * chaotic_sum + 0.15 * log_conditioning + 0.15 * cross_term + 0.1 * cubic_cross_term + 0.1 * quadratic_term + 0.05 * tanh_component + 0.05 * conditioning_component
        
        return result