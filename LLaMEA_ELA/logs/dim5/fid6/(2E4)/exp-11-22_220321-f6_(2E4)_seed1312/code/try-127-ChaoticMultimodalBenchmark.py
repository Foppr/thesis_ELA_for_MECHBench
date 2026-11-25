import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.99
        self.spherical_harmonics_degree = 4
        self.modulation_freq = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map component for chaotic behavior
        logistic_term = 0.0
        r = self.logistic_r
        for i in range(self.dim):
            # Initialize chaotic sequence
            x_prev = 0.5
            for _ in range(15):  # Let the system settle longer
                x_prev = r * x_prev * (1 - x_prev)
            # Use the chaotic value as a multiplier
            logistic_term += np.sin(x[i]) * x_prev
        
        # Sinusoidal modulation with dynamic frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.modulation_freq + 0.5 * np.sin(i * 0.6)
            sin_term += np.sin(freq * x[i] + np.cos(i * 0.5)) * np.cos(freq * x[i] + np.sin(i * 0.4))
        
        # Spherical harmonics component with higher degree
        sph_harm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r_ij = np.sqrt(x[i]**2 + x[j]**2)
                theta_ij = np.arctan2(x[j], x[i])
                # Spherical harmonic Y_4^m (higher degree)
                sph_harm_term += np.sin(4 * theta_ij) * np.cos(4 * theta_ij) * np.exp(-0.15 * r_ij**2)
        
        # Cross-dimensional coupling with stronger exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                cross_term += np.exp(-1.5 * dist) * np.sin(x[i] * x[j])
        
        # Asymmetric exponential decay with phase shifts
        asym_term = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.8)
            asym_term += np.exp(-0.3 * (x[i] - phase_shift)**2) * np.cos(2.5 * x[i])
        
        # Global scaling factor based on sum of coordinates
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x) * 0.25)
        
        return global_scale * (0.35 * logistic_term + 0.2 * sin_term + 0.18 * sph_harm_term + 0.17 * cross_term + 0.08 * asym_term)