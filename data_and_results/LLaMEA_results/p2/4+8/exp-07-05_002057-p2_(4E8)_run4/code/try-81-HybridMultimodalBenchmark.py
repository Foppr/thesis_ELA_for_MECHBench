import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (12, dim))
        self.weights = np.random.uniform(0.3, 3.0, 12)
        # Trigonometric coupling terms
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay radial basis function component
        exp_sum = 0.0
        for i in range(12):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            exp_sum += weight * np.exp(-distance / (2 * 0.4 ** 2))
        
        # Trigonometric coupling terms
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_coupling += self.coupling_coeffs[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Adaptive conditioning term
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            adaptive_conditioning += self.conditioning_factors[i] * (x[i] ** 4) * np.sin(x[i])
        
        # Cross-dimensional quadratic interaction
        quadratic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quadratic_interaction += (x[i] ** 2) * (x[j] ** 2)
        
        # Sine-based harmonic component
        sine_harmonic = 0.0
        for i in range(self.dim):
            sine_harmonic += np.sin(3 * x[i]) + 0.5 * np.sin(7 * x[i]) + 0.3 * np.sin(11 * x[i])
        
        # Combine all components with different weights
        result = 0.3 * exp_sum + 0.25 * trig_coupling + 0.2 * adaptive_conditioning + 0.15 * quadratic_interaction + 0.15 * sine_harmonic
        
        return result