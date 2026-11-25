import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time_phase = 0.0
        self.amplitude_scale = 1.5
        self.frequency_mod = 2.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying phase for dynamic behavior
        self.time_phase = (self.time_phase + 0.01) % (2 * np.pi)
        
        # Radial Basis Function component with chaotic modulation
        rbf_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic radial basis with time-varying parameters
            sigma = 0.3 + 0.4 * np.sin(self.time_phase + i * 0.8)
            mu = 1.5 * np.cos(self.time_phase + i * 0.6)
            rbf_term += np.exp(-0.5 * ((xi - mu) / sigma)**2) * (1.0 + 0.4 * np.sin(xi * self.frequency_mod))
        
        # Multi-frequency sinusoidal modulation with dynamic coupling
        sin_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sinusoidal components with varying frequencies and amplitudes
            sin_term += (np.sin(xi * 2.5 + self.time_phase) * np.cos(xi * 1.7 + self.time_phase * 0.8) * 
                        np.exp(-0.15 * xi**2) +
                        np.sin(xi * 5.2 + self.time_phase * 1.4) * np.cos(xi * 3.8 + self.time_phase * 1.0) * 
                        np.exp(-0.08 * xi**2) +
                        np.sin(xi * 7.1 + self.time_phase * 1.9) * np.cos(xi * 6.3 + self.time_phase * 1.3) * 
                        np.exp(-0.04 * xi**2))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction with time-varying coupling strength
                coupling_strength = 0.9 + 0.3 * np.sin(self.time_phase + i * 0.5 + j * 0.3)
                cross_term += coupling_strength * np.sin(x[i] * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Asymmetric polynomial with chaotic perturbations
        poly_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric polynomial with time-varying coefficients
            a = 1.2 + 0.15 * np.sin(self.time_phase + i * 0.7)
            b = 0.9 + 0.25 * np.cos(self.time_phase + i * 0.4)
            poly_term += (a * xi**4 + b * xi**3 - 0.6 * xi**2) * np.exp(-0.12 * xi**2)
        
        # Additional chaotic harmonic component
        harmonic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            harmonic_term += (0.5 * np.sin(xi * 3.0 + self.time_phase * 1.2) * 
                             np.cos(xi * 2.0 + self.time_phase * 0.9) * 
                             np.exp(-0.06 * xi**2))
        
        # Combine all terms with time-varying weights
        weight_rbf = 0.6 + 0.4 * np.sin(self.time_phase * 1.3)
        weight_sin = 0.7 + 0.3 * np.cos(self.time_phase * 0.8)
        weight_cross = 0.5 + 0.5 * np.sin(self.time_phase * 1.7)
        weight_poly = 0.8 + 0.2 * np.cos(self.time_phase * 0.6)
        weight_harmonic = 0.4 + 0.3 * np.sin(self.time_phase * 1.1)
        
        return (weight_rbf * rbf_term + 
                weight_sin * sin_term + 
                weight_cross * cross_term + 
                weight_poly * poly_term +
                weight_harmonic * harmonic_term)