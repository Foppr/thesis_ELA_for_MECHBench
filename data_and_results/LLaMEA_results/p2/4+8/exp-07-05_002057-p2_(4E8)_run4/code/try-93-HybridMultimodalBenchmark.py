import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
        self.conditioning_factors = np.random.uniform(0.05, 1.5, dim)
        self.chaotic_params = np.random.uniform(0.1, 0.9, (5, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with chaotic perturbations
        gaussian_sum = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            gaussian_sum += weight * np.exp(-distance / (2 * 0.3 ** 2))
        
        # Chaotic sinusoidal perturbations with logarithmic conditioning
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply chaotic modulation with different frequencies
            modulator = np.sin(self.chaotic_params[0, i] * xi) * np.cos(self.chaotic_params[1, i] * xi)
            modulator += np.sin(self.chaotic_params[2, i] * xi) * np.cos(self.chaotic_params[3, i] * xi)
            modulator += np.sin(self.chaotic_params[4, i] * xi) * np.cos(self.chaotic_params[0, i] * xi)
            chaotic_sum += modulator * np.log(np.abs(xi) + 1.0)
        
        # Logarithmic conditioning with cubic interactions
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += self.conditioning_factors[i] * (xi ** 3) * np.log(np.abs(xi) + 1.0)
        
        # Cross-dimensional cubic interactions
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cubic_interaction += (x[i] ** 3) * (x[j] ** 3) * np.sin(x[i] + x[j])
        
        # Quadratic basin component with variable conditioning
        quadratic_term = np.sum(x**2) / self.dim
        
        # Combine all components with different weights
        result = 0.3 * gaussian_sum + 0.25 * chaotic_sum + 0.2 * log_conditioning + 0.15 * cubic_interaction + 0.1 * quadratic_term
        
        return result