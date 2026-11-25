import numpy as np

class ChaoticLogarithmicEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic logarithmic pattern parameters
        self.n_patterns = max(4, dim // 2 + 2)
        self.log_scales = np.random.uniform(0.3, 1.8, self.n_patterns) * 2.0
        self.log_bases = np.random.uniform(1.1, 3.0, self.n_patterns) * 1.5
        # Elliptic section parameters
        self.elliptic_radii = np.random.uniform(0.2, 1.8, dim) * 1.3
        self.elliptic_angles = np.random.uniform(0.0, np.pi/3, dim) * 2.0
        # Harmonic coupling between dimensions
        self.harmonic_couplings = np.random.uniform(0.4, 3.0, (dim, dim)) * 1.5
        # Stochastic conditioning factors
        self.conditioning_factors = np.random.uniform(0.6, 2.8, dim) * 1.6
        # Chaotic scaling parameters
        self.chaotic_scale = 1.0 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Chaotic logarithmic pattern terms
        log_term = 0.0
        for i in range(self.n_patterns):
            scale = self.log_scales[i]
            base = self.log_bases[i]
            # Create chaotic logarithmic with sinusoidal modulation
            log_val = scale * np.log(base + np.abs(x_norm)) * np.cos(base * x_norm)
            log_term += np.sum(log_val)
            
        # Elliptic section terms with adaptive radii and angles
        elliptic_term = 0.0
        for i in range(self.dim):
            radius = self.elliptic_radii[i]
            angle = self.elliptic_angles[i]
            # Elliptic quadratic form with directional scaling
            ellipse_val = radius * (x_norm[i] ** 2) * np.sin(angle) + (x_norm[i] ** 2) * np.cos(angle)
            elliptic_term += ellipse_val
            
        # Cross-dimensional harmonic coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = self.harmonic_couplings[i, j]
                # Harmonic coupling with phase shift and logarithmic decay
                phase_shift = np.cos(0.3 * (i - j)) * np.pi / 3
                coupling_val = coupling * np.log(1.0 + 0.1 * (x_norm[i] ** 2 + x_norm[j] ** 2)) * \
                              np.cos(coupling * (x_norm[i] - x_norm[j]) + phase_shift)
                coupling_term += coupling_val
                
        # Stochastic conditioning with logarithmic modulation
        condition_term = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i]
            # Logarithmic conditioning with sinusoidal perturbation
            condition_val = cond_factor * np.log(1.0 + 0.5 * x_norm[i] ** 2) * (1.0 + 0.4 * np.cos(2.0 * x_norm[i]))
            condition_term += condition_val
            
        # Combined terms with chaotic weighting
        result = 2.0 * log_term + 1.5 * elliptic_term + 1.3 * coupling_term + 1.1 * condition_term
        
        # Add chaotic noise with logarithmic characteristics
        noise_amplitude = 0.04 * (1.0 + 0.08 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        # Apply chaotic scaling
        result *= self.chaotic_scale
        
        return result + noise