import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive radial basis function terms with dynamic widths
        rbf_sum = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.3 * np.cos(i * 0.5)  # Dynamic varying widths
            rbf_sum += np.exp(-0.5 * (x[i] / width)**2)
        
        # Enhanced sinusoidal modulation with varying frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            sin_mod += np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Quadratic basin term with adaptive scaling
        quadratic = 0.03 * np.sum(x**2)
        
        # Cross-terms with interactive coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.015 * np.sin(3.0 * x[i]) * np.cos(1.5 * x[j]) * (1 + 0.1 * np.abs(x[i] - x[j]))
        
        # Additional high-frequency oscillation for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.02 * np.sin(5.0 * x[i]) * np.cos(2.0 * x[i])
        
        return quadratic + rbf_sum + sin_mod + cross_terms + high_freq