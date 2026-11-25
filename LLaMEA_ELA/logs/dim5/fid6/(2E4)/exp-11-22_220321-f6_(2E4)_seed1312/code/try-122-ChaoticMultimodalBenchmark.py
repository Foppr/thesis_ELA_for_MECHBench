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
        
        # Enhanced logistic map component with chaotic behavior
        logistic_term = 0.0
        r = self.logistic_r
        for i in range(self.dim):
            # Initialize chaotic sequence with multiple iterations
            x_prev = 0.5 + 0.1 * np.sin(i)
            for _ in range(15):  # More iterations for stronger chaos
                x_prev = r * x_prev * (1 - x_prev)
            # Use the chaotic value as a multiplier with phase modulation
            logistic_term += np.sin(x[i] + x_prev) * np.cos(x[i] * x_prev)
        
        # Modified sinusoidal modulation with frequency coupling
        sin_term = 0.0
        for i in range(self.dim):
            freq = self.modulation_freq + 0.5 * np.sin(i * 0.7) * np.cos(i * 0.3)
            phase = np.sin(i * 0.9) + 0.2 * np.cos(i * 0.4)
            sin_term += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase) * np.exp(-0.1 * x[i]**2)
        
        # Augmented spherical harmonics component with higher degree
        sph_harm_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r_ij = np.sqrt(x[i]**2 + x[j]**2)
                theta_ij = np.arctan2(x[j], x[i])
                # Spherical harmonic Y_4^m (higher degree)
                sph_harm_term += np.sin(4 * theta_ij) * np.cos(4 * theta_ij) * np.exp(-0.15 * r_ij**2)
        
        # Enhanced cross-dimensional coupling with cubic interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j]) + 0.1 * np.abs(x[i] + x[j])
                cross_term += np.exp(-dist**2) * (x[i]**3 * x[j] + x[i] * x[j]**3)
        
        # Modified asymmetric exponential decay with dynamic phase shifts
        asym_term = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.8) + 0.3 * np.cos(i * 0.5)
            asym_term += np.exp(-0.3 * (x[i] - phase_shift)**2) * np.sin(3 * x[i]) * np.cos(x[i])
        
        # Global scaling factor with multi-modal influence
        global_scale = 1.0 + 0.4 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.2)
        
        return global_scale * (0.25 * logistic_term + 0.2 * sin_term + 0.25 * sph_harm_term + 0.15 * cross_term + 0.15 * asym_term)