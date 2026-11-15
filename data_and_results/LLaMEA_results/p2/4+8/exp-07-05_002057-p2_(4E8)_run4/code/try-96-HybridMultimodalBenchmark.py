import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute Gaussian centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.weights = np.random.uniform(0.3, 2.5, 15)
        self.conditioning_factors = np.random.uniform(0.05, 1.5, dim)
        self.frequency_factors = np.random.uniform(1.0, 10.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component with adaptive widths
        gauss_sum = 0.0
        for i in range(15):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            # Adaptive width based on dimension
            adaptive_width = 0.3 + 0.2 * np.sin(i)
            gauss_sum += weight * np.exp(-distance / (2 * adaptive_width ** 2))
        
        # Chaotic sinusoidal perturbations with varying frequencies
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequency_factors[i]
            chaotic_sum += (np.sin(freq * xi + np.sin(freq * xi)) * 
                           np.cos(freq * xi + np.cos(freq * xi)) * 
                           np.tan(freq * xi + np.tan(freq * xi)))
        
        # Logarithmic conditioning with cross-dimensional coupling
        log_conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            log_conditioning += self.conditioning_factors[i] * np.log(1 + np.abs(xi)) * np.sin(xi)
        
        # Cross-dimensional cubic interactions with variable coupling strengths
        cubic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin((i + j) * 0.5)
                cubic_interaction += coupling * (x[i] ** 3) * (x[j] ** 3)
        
        # Novel quartic basin component with chaotic modulation
        quartic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            quartic_term += (xi ** 4) * (1 + 0.3 * np.sin(7 * xi))
        
        # Combine all components with different weights
        result = 0.3 * gauss_sum + 0.25 * chaotic_sum + 0.2 * log_conditioning + 0.15 * cubic_interaction + 0.15 * quartic_term
        
        return result