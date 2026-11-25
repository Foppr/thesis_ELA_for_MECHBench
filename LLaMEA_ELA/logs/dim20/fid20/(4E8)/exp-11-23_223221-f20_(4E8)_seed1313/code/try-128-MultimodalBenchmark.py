import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-order polynomial with chaotic scaling factors and dynamic exponents
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.3 * np.abs(x[i]))
            exp_factor = 1.0 + 0.5 * np.sin(0.7 * x[i])
            poly_term += 0.5 * (x[i] ** (4.0 + exp_factor)) * scale * np.exp(-0.2 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights and phase shifts
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.4 * (1.0 + np.cos(0.5 * x[i]) * np.sin(0.3 * x[j]))
                phase_shift = 0.5 * np.sin(0.6 * x[i] + 0.4 * x[j])
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j] + phase_shift)
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation and frequency coupling
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling
                freq_i = 2.5 + 1.2 * np.sin(0.5 * x[i])
                freq_j = 3.1 + 0.9 * np.cos(0.6 * x[j])
                phase = 0.8 * np.sin(0.4 * x[i] + 0.5 * x[j]) + 0.3 * np.cos(0.7 * x[i] - 0.2 * x[j])
                rot_term += 0.25 * np.sin(freq_i * (x[i] + x[j]) + phase) * np.cos(freq_j * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation and time-varying coefficients
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.4, 1.3, 2.8, 5.7, 7.9, 9.2]
            decay = 0.0
            for f in freqs:
                # Chaotic frequency modulation based on position and time-like parameter
                mod_freq = f * (1.0 + 0.3 * np.sin(1.1 * x[i]) * np.cos(0.8 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i] + 0.5 * np.sin(0.9 * x[i]))
            decay_term += 0.3 * decay
        
        # Basin boundary with irregular fractal-like irregularities, noise, and multi-scale features
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.5:
                basin_term += 0.12 * x[i]**6 + 0.05 * np.sin(20 * x[i]) + 0.04 * np.random.rand()
            else:
                basin_term += 0.18 * np.abs(x[i])**2.8 + 0.06 * np.cos(10 * x[i]) + 0.03 * np.random.rand()
        
        # Chaotic sine-wave component with adaptive amplitude and frequency modulation
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.7 + 0.25 * np.sin(0.9 * x[i]) + 0.15 * np.cos(0.4 * x[i])
            freq_mod = 160 + 20 * np.sin(0.5 * x[i])
            chaos_term += amp * np.sin(freq_mod * x[i]) * np.exp(-0.7 * x[i]**2)
        
        # Add additional ridge structure with multi-scale harmonics and irregularity
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.15 * np.sin(3.5 * x[i]) * np.cos(2.8 * x[i]) + 0.07 * np.sin(7.5 * x[i]) + 0.03 * np.sin(12.0 * x[i])
        
        # Add global scaling factor and noise injection
        total = poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term + ridge_term
        return total * (1.0 + 0.1 * np.random.rand())