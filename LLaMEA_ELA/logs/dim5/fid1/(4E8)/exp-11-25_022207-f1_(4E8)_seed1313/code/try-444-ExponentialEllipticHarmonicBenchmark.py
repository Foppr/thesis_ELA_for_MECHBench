import numpy as np

class ExponentialEllipticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced periodic exponential pattern parameters
        self.n_patterns = max(4, dim // 2 + 2)
        self.exp_scales = np.random.uniform(0.3, 1.8, self.n_patterns) * 1.7
        self.periods = np.random.uniform(0.8, 3.5, self.n_patterns) * 1.9
        # Improved elliptic section parameters
        self.elliptic_radii = np.random.uniform(0.2, 1.8, dim) * 1.3
        self.elliptic_angles = np.random.uniform(0.0, np.pi/2, dim) * 2.0
        # Enhanced harmonic coupling between dimensions
        self.harmonic_couplings = np.random.uniform(0.4, 2.2, (dim, dim)) * 1.5
        # Refined stochastic conditioning factors
        self.conditioning_factors = np.random.uniform(0.6, 2.8, dim) * 1.6
        # Enhanced adaptive scaling parameters
        self.adaptive_scale = 1.0 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced periodic exponential pattern terms
        exp_term = 0.0
        for i in range(self.n_patterns):
            scale = self.exp_scales[i]
            period = self.periods[i]
            # Create enhanced periodic exponential with sinusoidal modulation
            exp_val = scale * np.exp(-0.3 * (x_norm / period) ** 2) * np.sin(period * x_norm)
            exp_term += np.sum(exp_val)
            
        # Improved elliptic section terms with adaptive radii and angles
        elliptic_term = 0.0
        for i in range(self.dim):
            radius = self.elliptic_radii[i]
            angle = self.elliptic_angles[i]
            # Enhanced elliptic quadratic form with directional scaling
            ellipse_val = radius * (x_norm[i] ** 2) * np.cos(angle) + (x_norm[i] ** 2) * np.sin(angle)
            elliptic_term += ellipse_val
            
        # Enhanced cross-dimensional harmonic coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling = self.harmonic_couplings[i, j]
                # Enhanced harmonic coupling with phase shift and exponential decay
                phase_shift = np.sin(0.3 * (i + j)) * np.pi / 3
                coupling_val = coupling * np.exp(-0.15 * (x_norm[i] ** 2 + x_norm[j] ** 2)) * \
                              np.sin(coupling * (x_norm[i] + x_norm[j]) + phase_shift)
                coupling_term += coupling_val
                
        # Refined stochastic conditioning with exponential modulation
        condition_term = 0.0
        for i in range(self.dim):
            cond_factor = self.conditioning_factors[i]
            # Refined exponential conditioning with sinusoidal perturbation
            condition_val = cond_factor * np.exp(0.6 * x_norm[i] ** 2) * (1.0 + 0.4 * np.sin(2.5 * x_norm[i]))
            condition_term += condition_val
            
        # Combined terms with enhanced weighting
        result = 2.0 * exp_term + 1.6 * elliptic_term + 1.3 * coupling_term + 1.1 * condition_term
        
        # Add refined stochastic noise with exponential characteristics
        noise_amplitude = 0.04 * (1.0 + 0.08 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        # Apply enhanced adaptive scaling
        result *= self.adaptive_scale
        
        return result + noise