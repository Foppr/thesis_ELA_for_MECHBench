import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive radial basis functions with dynamic widths
        rbf_sum = 0.0
        for i in range(self.dim):
            width = 1.5 + 0.5 * np.cos(i * np.pi / self.dim)  # Adaptive widths
            rbf_sum += np.exp(-0.3 * (x[i] / width)**2)
        
        # Enhanced sinusoidal modulation with varying frequencies
        sine_mod = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i)  # Varying frequencies
            sine_mod += np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Modified quadratic basin with conditioning
        quadratic = 0.03 * np.sum(x**2)
        
        # Increased cross-terms with interaction coefficients
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = 0.03 * np.sin(1.5 * x[i]) * np.cos(1.5 * x[j])
                # Add dimensionality-dependent scaling
                scale = (i + 1) * (j + 1) / (self.dim**2)
                cross_terms += scale * interaction
        
        # Additional high-frequency oscillation for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(5.0 * x[i]) * np.cos(2.0 * x[i])
        
        return quadratic + rbf_sum + sine_mod + cross_terms + 0.5 * high_freq