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
        
        # Enhanced radial basis function with adaptive width and position
        rbf_term = 0.0
        for i in range(self.dim):
            # Adaptive width based on dimension and input value
            sigma = 1.0 + 0.3 * np.sin(i * np.pi / self.dim) + 0.1 * np.abs(x[i])
            # Position centers vary dynamically with sinusoidal modulation
            center = 2.0 * np.cos(i * np.pi / (self.dim + 1)) + 0.5 * np.sin(x[i])
            rbf_term += np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        rbf_term /= self.dim
        
        # Temporal coupling with dynamic phase shifts and frequency modulation
        temporal_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            phase = self.tau[i] * np.sin(freq * x[i])
            temporal_term += np.cos(phase) * np.sin(2.0 * phase) + 0.2 * np.cos(3.0 * phase)
        temporal_term /= self.dim
        
        # Cross-dimensional interaction with enhanced hyperbolic tangent coupling and quadratic terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add quadratic interaction term for increased complexity
                cross_term += (np.tanh(x[i] * x[j]) + 0.3 * x[i]**2 * x[j]**2) * np.sin(np.pi * (x[i] + x[j]))
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-scale sinusoidal modulation with varying frequencies and phase shifts
        mod_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * np.pi / self.dim) + 0.2 * np.cos(x[i])
            phase_shift = 0.5 * np.sin(i * np.pi / (self.dim + 1))
            mod_term += np.sin(freq * x[i] + phase_shift) * np.cos(2.0 * freq * x[i] + phase_shift)
        mod_term /= self.dim
        
        # Asymmetric polynomial distortion with higher-order terms
        asym_term = np.sum(np.abs(x)**3 - 2.0 * x**2 + 1.5 * np.abs(x) + 0.5 * x**4) / self.dim
        
        # Dynamic conditioning with exponential scaling and dimension-dependent factor
        cond_factor = 1.0 + 0.3 * np.exp(-0.1 * np.mean(np.abs(x))) + 0.1 * np.sin(self.dim * np.pi / 4.0)
        
        # Combine all terms with dynamic weights
        total = (0.25 * poly_term + 
                0.20 * rbf_term + 
                0.15 * temporal_term + 
                0.15 * cross_term + 
                0.15 * mod_term + 
                0.10 * asym_term) * cond_factor
        
        return total