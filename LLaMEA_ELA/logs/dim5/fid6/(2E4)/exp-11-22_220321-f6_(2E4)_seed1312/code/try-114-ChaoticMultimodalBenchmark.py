import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.95
        self.spherical_harmonics_degree = 3
        self.modulation_freq = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component for chaotic behavior
        logistic_term = 0.0
        r = self.logistic_r
        for i in range(self.dim):
            # Initialize chaotic sequence
            x_prev = 0.5
            for _ in range(10):  # Let the system settle
                x_prev = r * x_prev * (1 - x_prev)
            # Use the chaotic value as a multiplier
            logistic_term += np.sin(x[i]) * x_prev
        
        # Sinusoidal modulation with dynamic frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.modulation_freq + 0.3 * np.sin(i * 0.5)
            sin_term += np.sin(freq * x[i] + np.cos(i * 0.4)) * np.cos(freq * x[i] + np.sin(i * 0.3))
        
        # Spherical harmonics component
        sph_harm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r_ij = np.sqrt(x[i]**2 + x[j]**2)
                theta_ij = np.arctan2(x[j], x[i])
                # Spherical harmonic Y_3^m (simplified version)
                sph_harm_term += np.sin(3 * theta_ij) * np.cos(3 * theta_ij) * np.exp(-0.1 * r_ij**2)
        
        # Cross-dimensional coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                cross_term += np.exp(-dist) * np.sin(x[i] * x[j])
        
        # Asymmetric exponential decay with phase shifts
        asym_term = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.7)
            asym_term += np.exp(-0.5 * (x[i] - phase_shift)**2) * np.cos(2 * x[i])
        
        # Global scaling factor based on sum of coordinates
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x) * 0.2)
        
        return global_scale * (0.3 * logistic_term + 0.25 * sin_term + 0.2 * sph_harm_term + 0.15 * cross_term + 0.1 * asym_term)