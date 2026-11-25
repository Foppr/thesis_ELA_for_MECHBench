import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-order polynomial with enhanced chaotic scaling factors
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.2 * np.abs(x[i]))
            poly_term += 0.4 * (x[i] ** 5) * scale * np.exp(-0.3 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.3 * (1.0 + np.sin(0.4 * x[i]))
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j])
        
        # Quaternion-inspired rotational symmetry with enhanced chaotic phase shift
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling
                freq = 2.8 + 1.5 * np.sin(0.4 * x[i]) + 1.1 * np.cos(0.6 * x[j])
                # Enhanced chaotic phase shift addition
                phase = 0.7 * np.sin(0.3 * x[i] + 0.7 * x[j]) + 0.15 * np.sin(3.5 * x[i] * x[j])
                rot_term += 0.2 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with enhanced frequency modulation
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.5, 1.5, 3.2, 6.8, 8.5]
            decay = 0.0
            for f in freqs:
                # Enhanced frequency modulation adjustment
                mod_freq = f * (1.0 + 0.4 * np.sin(1.2 * x[i]) * np.cos(0.9 * x[i]) + 0.15 * np.sin(2.5 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.25 * decay
        
        # Basin boundary with enhanced fractal-like irregularities and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.3:
                basin_term += 0.1 * x[i]**5 + 0.04 * np.sin(18 * x[i]) + 0.03 * np.random.rand()
            else:
                basin_term += 0.16 * np.abs(x[i])**2.5 + 0.05 * np.cos(9 * x[i]) + 0.02 * np.random.rand()
        
        # Enhanced chaotic sine-wave component with adaptive amplitude
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.6 + 0.3 * np.sin(0.8 * x[i])
            chaos_term += amp * np.sin(150 * x[i]) * np.exp(-0.8 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term