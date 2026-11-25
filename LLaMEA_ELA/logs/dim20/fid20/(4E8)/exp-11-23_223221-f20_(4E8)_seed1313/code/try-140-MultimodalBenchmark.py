import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-order polynomial with chaotic scaling factors and fractal modulation
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.4 * np.abs(x[i]))
            poly_term += 0.6 * (x[i] ** 5) * scale * np.exp(-0.3 * x[i]**2) * (1.0 + 0.3 * np.sin(2.5 * x[i]))
        
        # Multi-scale logarithmic coupling with variable weights and phase modulation
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.5 * (1.0 + np.sin(0.6 * x[i]) * np.cos(0.4 * x[j]))
                phase = 0.6 * np.sin(0.5 * x[i] + 0.7 * x[j])
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j] + phase)
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation and chaos injection
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling
                freq = 5.0 + 2.5 * np.sin(0.6 * x[i]) + 2.0 * np.cos(0.8 * x[j])
                phase = 0.9 * np.sin(0.5 * x[i] + 0.9 * x[j]) + 0.4 * np.random.rand()
                rot_term += 0.3 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation and noise injection
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.5, 1.5, 3.1, 6.2, 8.3, 10.1]
            decay = 0.0
            for f in freqs:
                # Chaotic frequency modulation based on position with added noise
                mod_freq = f * (1.0 + 0.6 * np.sin(1.5 * x[i]) * np.cos(1.2 * x[i]) + 0.3 * np.random.rand())
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.4 * decay
        
        # Basin boundary with irregular fractal-like irregularities, noise injection and adaptive scaling
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.5:
                basin_term += 0.2 * x[i]**5 + 0.08 * np.sin(25 * x[i]) + 0.05 * np.random.rand()
            else:
                basin_term += 0.25 * np.abs(x[i])**3.1 + 0.08 * np.cos(12 * x[i]) + 0.04 * np.random.rand()
        
        # Chaotic sine-wave component with adaptive amplitude and multi-frequency mixing
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.8 + 0.5 * np.sin(1.1 * x[i]) + 0.3 * np.cos(1.3 * x[i])
            chaos_term += amp * (np.sin(250 * x[i]) * np.exp(-1.0 * x[i]**2) + 0.4 * np.sin(120 * x[i]))
        
        # Enhanced ridge structure with multiple harmonic components and adaptive scaling
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_term += 0.2 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) + 0.1 * np.sin(10.0 * x[i]) + 0.08 * np.sin(15.0 * x[i])
        
        # Add a novel fractal-like noise component for increased complexity
        fractal_noise = 0.0
        for i in range(self.dim):
            fractal_noise += 0.1 * np.sin(30 * x[i]) * np.cos(20 * x[i]) * np.exp(-0.7 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term + ridge_term + fractal_noise