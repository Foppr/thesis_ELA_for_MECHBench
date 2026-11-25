import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Scale input to [-1, 1] for computation
        x_scaled = x / 5.0
        
        # Radial quadratic basin term
        radial_term = np.sum(x_scaled**2)
        
        # Sinusoidal oscillations in multiple directions
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += np.sin(5 * x_scaled[i]) * np.cos(3 * x_scaled[i])
        
        # Cross-terms creating non-separability
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x_scaled[i] * x_scaled[j] * np.sin(x_scaled[i] + x_scaled[j])
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x_scaled[i]) * np.cos(7 * x_scaled[i])
        
        # Combine all terms with different weights
        return 0.5 * radial_term + 0.3 * sin_sum + 0.2 * cross_term + 0.1 * chaotic