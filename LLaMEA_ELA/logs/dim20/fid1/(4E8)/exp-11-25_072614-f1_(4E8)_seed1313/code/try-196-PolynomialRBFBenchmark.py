import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for temporal dynamics
        self.tau = np.linspace(0.1, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed terms
        poly_term = np.sum(0.3 * x**6 + 0.7 * x**4 - 1.2 * x**2 + 0.5) / self.dim
        
        # Radial basis function with adaptive width and position
        rbf_term = 0.0
        for i in range(self.dim):
            # Adaptive width based on dimension
            sigma = 1.0 + 0.2 * np.sin(i * np.pi / self.dim)
            # Position centers vary dynamically
            center = 2.0 * np.cos(i * np.pi / (self.dim + 1))
            rbf_term += np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        rbf_term /= self.dim
        
        # Temporal coupling with dynamic phase shifts
        temporal_term = 0.0
        for i in range(self.dim):
            phase = self.tau[i] * np.sin(x[i])
            temporal_term += np.cos(phase) * np.sin(2.0 * phase)
        temporal_term /= self.dim
        
        # Cross-dimensional interaction with hyperbolic tangent coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.tanh(x[i] * x[j]) * np.sin(np.pi * (x[i] + x[j]))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        mod_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            mod_term += np.sin(freq * x[i]) * np.cos(2.0 * freq * x[i])
        mod_term /= self.dim
        
        # Asymmetric polynomial distortion
        asym_term = np.sum(np.abs(x)**3 - 2.0 * x**2 + 1.5 * np.abs(x)) / self.dim
        
        # Dynamic conditioning with exponential scaling
        cond_factor = 1.0 + 0.3 * np.exp(-0.1 * np.mean(np.abs(x)))
        
        # Combine all terms with dynamic weights
        total = (0.25 * poly_term + 
                0.20 * rbf_term + 
                0.15 * temporal_term + 
                0.15 * cross_term + 
                0.15 * mod_term + 
                0.10 * asym_term) * cond_factor
        
        return total