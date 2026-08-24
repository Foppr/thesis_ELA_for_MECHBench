import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.3, 2.5, 10)
        self.conditioning_factors = np.random.uniform(0.1, 3.0, dim)
        self.chaotic_params = np.random.uniform(0.5, 2.0, (5, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gauss_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gauss_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbations with dimension-specific frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply multiple chaotic sinusoidal terms
            chaotic_sum += (np.sin(self.chaotic_params[0, i] * xi) * 
                           np.cos(self.chaotic_params[1, i] * xi) * 
                           np.tan(self.chaotic_params[2, i] * xi) +
                           0.7 * np.sin(self.chaotic_params[3, i] * xi) * 
                           np.cos(self.chaotic_params[4, i] * xi) * 
                           np.tan(self.chaotic_params[0, i] * xi))
        
        # Logarithmic conditioning with adaptive scaling
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += self.conditioning_factors[i] * np.log(1 + abs(xi)) * np.sin(xi)
        
        # Cross-dimensional cubic interactions
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += (x[i] ** 3) * (x[j] ** 3) * np.sin(x[i] + x[j])
        
        # Novel polynomial coupling terms
        poly_coupling = 0.0
        for i in range(self.dim):
            xi = x[i]
            poly_coupling += (xi ** 5) * np.cos(2 * xi) + (xi ** 4) * np.sin(3 * xi)
        
        # Quadratic basin component with variable conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gauss_sum + 0.25 * chaotic_sum + 0.2 * log_conditioning + 0.15 * cubic_interaction + 0.08 * poly_coupling + 0.02 * quadratic_term
        
        return result