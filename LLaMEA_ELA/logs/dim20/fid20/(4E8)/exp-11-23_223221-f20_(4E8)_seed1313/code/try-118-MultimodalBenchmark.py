import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-order polynomial with chaotic scaling factors
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.18 * np.abs(x[i]))
            poly_term += 0.32 * (x[i] ** 5) * scale * np.exp(-0.28 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.28 * (1.0 + np.sin(0.38 * x[i]))
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j])
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling
                freq = 2.7 + 1.1 * np.sin(0.38 * x[i]) + 0.8 * np.cos(0.52 * x[j])
                phase = 0.65 * np.sin(0.28 * x[i] + 0.62 * x[j])
                rot_term += 0.19 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.45, 1.25, 2.85, 6.05, 7.75]
            decay = 0.0
            for f in freqs:
                # Chaotic frequency modulation based on position
                mod_freq = f * (1.0 + 0.32 * np.sin(1.02 * x[i]) * np.cos(0.82 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.21 * decay
        
        # Basin boundary with irregular fractal-like irregularities and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.1:
                basin_term += 0.085 * x[i]**5 + 0.032 * np.sin(16.5 * x[i]) + 0.023 * np.random.rand()
            else:
                basin_term += 0.135 * np.abs(x[i])**2.35 + 0.043 * np.cos(8.2 * x[i]) + 0.013 * np.random.rand()
        
        # Chaotic sine-wave component with adaptive amplitude
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.58 + 0.24 * np.sin(0.78 * x[i])
            chaos_term += amp * np.sin(138 * x[i]) * np.exp(-0.78 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term