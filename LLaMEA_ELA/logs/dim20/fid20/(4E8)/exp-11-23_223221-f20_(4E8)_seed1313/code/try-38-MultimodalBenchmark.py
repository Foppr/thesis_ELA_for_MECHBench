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
            width = 1.0 + 0.4 * np.cos(i * 0.6)  # Slightly increased variation
            rbf_sum += np.exp(-0.5 * (x[i] / width)**2)
        
        # Enhanced sinusoidal modulation with varying frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.5 + 0.6 * np.sin(i * 0.8)
            sin_mod += np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Modified quadratic basin term with stronger scaling
        quadratic = 0.05 * np.sum(x**2)
        
        # Cross-terms with interactive coupling and additional interaction strength
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.02 * np.sin(3.5 * x[i]) * np.cos(2.0 * x[j]) * (1 + 0.15 * np.abs(x[i] - x[j]))
        
        # Additional high-frequency oscillation for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.03 * np.sin(6.0 * x[i]) * np.cos(2.5 * x[i])
        
        # Add a periodic modulation term to further increase landscape complexity
        periodic_mod = 0.0
        for i in range(self.dim):
            periodic_mod += 0.01 * np.sin(4.0 * x[i] + 0.5 * i) * np.cos(3.0 * x[i])
        
        return quadratic + rbf_sum + sin_mod + cross_terms + high_freq + periodic_mod