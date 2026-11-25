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
            scale = 1.0 / (1.0 + 0.15 * np.abs(x[i]))
            poly_term += 0.35 * (x[i] ** 5) * scale * np.exp(-0.25 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.25 * (1.0 + np.sin(0.35 * x[i]))
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j])
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling
                freq = 2.5 + 1.2 * np.sin(0.35 * x[i]) + 0.9 * np.cos(0.5 * x[j])
                # Slight chaotic phase shift addition
                phase = 0.6 * np.sin(0.25 * x[i] + 0.6 * x[j]) + 0.1 * np.sin(3.0 * x[i] * x[j])
                rot_term += 0.18 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.4, 1.3, 2.9, 6.1, 7.8]
            decay = 0.0
            for f in freqs:
                # Slight adjustment to frequency modulation
                mod_freq = f * (1.0 + 0.35 * np.sin(1.0 * x[i]) * np.cos(0.8 * x[i]) + 0.1 * np.sin(2.0 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.22 * decay
        
        # Basin boundary with irregular fractal-like irregularities and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.2:
                basin_term += 0.09 * x[i]**5 + 0.035 * np.sin(16 * x[i]) + 0.025 * np.random.rand()
            else:
                basin_term += 0.14 * np.abs(x[i])**2.4 + 0.045 * np.cos(8 * x[i]) + 0.015 * np.random.rand()
        
        # Chaotic sine-wave component with adaptive amplitude
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.55 + 0.25 * np.sin(0.75 * x[i])
            chaos_term += amp * np.sin(140 * x[i]) * np.exp(-0.75 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term