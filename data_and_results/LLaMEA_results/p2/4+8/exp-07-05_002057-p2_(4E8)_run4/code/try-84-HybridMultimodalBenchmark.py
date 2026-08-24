import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay centers and weights for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 3.0, 10)
        # Adaptive conditioning parameters
        self.conditioning = np.random.uniform(1.0, 10.0, dim)
        # Trigonometric coupling terms
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay radial basis function component
        exp_sum = 0.0
        for i in range(10):
            center = self.centers[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            exp_sum += weight * np.exp(-distance / (2 * 0.5 ** 2))
        
        # Trigonometric coupling terms
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_coupling += self.coupling_weights[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Adaptive conditioning term
        adaptive_conditioning = 0.0
        for i in range(self.dim):
            adaptive_conditioning += self.conditioning[i] * (x[i] ** 2)
        
        # Cross-dimensional quadratic interaction
        quadratic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quadratic_interaction += (x[i] * x[j]) ** 2
        
        # Sine-based periodic modulation
        periodic_modulation = 0.0
        for i in range(self.dim):
            periodic_modulation += np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Combine all components with different weights
        result = 0.4 * exp_sum + 0.3 * trig_coupling + 0.15 * adaptive_conditioning + 0.1 * quadratic_interaction + 0.05 * periodic_modulation
        
        return result