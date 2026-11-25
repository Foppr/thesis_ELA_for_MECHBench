import numpy as np

class ExponentialEllipticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Periodic exponential pattern parameters
        self.n_patterns = max(3, dim // 3 + 1)
        self.exp_scales = np.random.uniform(0.5, 2.0, self.n_patterns) * 1.5
        self.periods = np.random.uniform(1.0, 4.0, self.n_patterns) * 2.0
        # Elliptic section parameters
        self.elliptic_radii = np.random.uniform(0.3, 1.5, dim) * 1.2
        self.elliptic_angles = np.random.uniform(0.0, np.pi/2, dim) * 1.8
        # Harmonic coupling between dimensions
        self.harmonic_couplings = np.random.uniform(0.5, 2.5, (dim, dim)) * 1.3
        # Stochastic conditioning factors
        self.conditioning_factors = np.random.uniform(0.8, 3.0, dim) * 1.4
        # Adaptive scaling parameters
        self.adaptive_scale = 1.0 + 0.15 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Periodic exponential pattern terms
        exp_term = 0.0
        for i in range(self.n_patterns):
            scale = self.exp_scales[i]
            period = self.periods[i]
            # Create periodic exponential with sinusoidal modulation
            exp_val = scale * np.exp(-0.5 * (x_norm / period) ** 2) * np.sin(period * x_norm)
            exp_term += np.sum(exp_val)
            
        # Elliptic section terms with adaptive radii and angles
        elliptic_term = 0.0
        for i in range(self.dim):
            radius = self.elliptic_radii[i]
            angle = self.elliptic_angles[i]
            # Elliptic quadratic form with directional scaling
            ellipse_val = radius * (x_norm[i] ** 2) * np.cos(angle) + (x_norm[i] ** 2) * np.sin(angle)
            elliptic_term += ellipse_val
            
        # Cross-dimensional harmonic coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = self.harmonic_couplings[i, j]
                # Harmonic coupling with phase shift and exponential decay
                phase_shift = np.sin(0.5 * (i + j)) * np.pi / 4
                coupling_val = coupling * np.exp(-0.2 * (x_norm[i] ** 2 + x_norm[j] ** 2)) * \
                              np.sin(coupling * (x_norm[i] + x_norm[j]) + phase_shift)
                coupling_term += coupling_val
                
        # Stochastic conditioning with exponential modulation
        condition_term = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i]
            # Exponential conditioning with sinusoidal perturbation
            condition_val = cond_factor * np.exp(0.5 * x_norm[i] ** 2) * (1.0 + 0.3 * np.sin(3.0 * x_norm[i]))
            condition_term += condition_val
            
        # Combined terms with adaptive weighting
        result = 1.8 * exp_term + 1.4 * elliptic_term + 1.2 * coupling_term + 1.0 * condition_term
        
        # Add stochastic noise with exponential characteristics
        noise_amplitude = 0.03 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        # Apply adaptive scaling
        result *= self.adaptive_scale
        
        return result + noise