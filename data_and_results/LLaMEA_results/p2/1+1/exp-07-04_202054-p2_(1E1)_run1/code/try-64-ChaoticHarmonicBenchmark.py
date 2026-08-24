import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map values for chaotic behavior
        self.logistic_r = 3.99
        self.logistic_x = np.random.rand(dim) * 0.1 + 0.01
        self.harmonic_coeffs = np.random.rand(dim) * 2 + 1
        self.fbm_exponent = 0.3
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical harmonic component
        f_value = 0.0
        for i in range(self.dim):
            f_value += self.harmonic_coeffs[i] * np.sin(x[i] * (i + 1)) * np.cos(x[i] * (i + 2))
        
        # Logistic map chaotic dynamics
        for i in range(self.dim):
            self.logistic_x[i] = self.logistic_r * self.logistic_x[i] * (1 - self.logistic_x[i])
            f_value += 0.5 * self.logistic_x[i] * np.sin(x[i])
        
        # Fractional Brownian motion-like scaling
        for i in range(self.dim):
            f_value += 0.3 * np.sin(x[i] ** 2) * np.cos(x[i] ** 3) * np.sin(self.fbm_exponent * x[i])
        
        # Multi-scale sinusoidal modulation
        for i in range(self.dim):
            f_value += 0.2 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i]) * np.cos(25 * x[i])
        
        # Cross-variable chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.15 * np.sin(5 * x[i] + 3 * x[j]) * np.cos(7 * x[i] - 2 * x[j]) * np.sin(4 * x[i] + x[j])
        
        # Fractional polynomial with chaotic modulation
        for i in range(self.dim):
            f_value += 0.25 * (x[i] ** 1.7) * np.sin(3 * x[i] * self.logistic_x[i])
        
        # Memory-dependent term with previous x values
        if hasattr(self, 'prev_x'):
            for i in range(self.dim):
                f_value += 0.1 * (x[i] - self.prev_x[i]) ** 2
        self.prev_x = x.copy()
        
        # Add a global scaling factor based on dimensionality
        f_value *= (1.0 + 0.1 * self.dim)
        
        return f_value