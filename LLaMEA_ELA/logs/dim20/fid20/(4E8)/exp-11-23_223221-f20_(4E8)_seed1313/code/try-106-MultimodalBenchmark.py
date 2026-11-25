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
            scale = 1.0 / (1.0 + 0.2 * np.abs(x[i]))
            poly_term += 0.5 * (x[i] ** 6) * scale * np.exp(-0.3 * x[i]**2)
        
        # Multi-scale logarithmic coupling with variable weights
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                weight = 0.3 * (1.0 + np.sin(0.4 * x[i]) * np.cos(0.3 * x[j]))
                log_coupling += weight * np.log(1.0 + dist) * np.cos(x[i] * x[j])
        
        # Quaternion-inspired rotational symmetry with dynamic phase modulation
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                freq = 2.5 + 2.0 * np.sin(0.5 * x[i]) + 1.0 * np.cos(0.7 * x[j])
                phase = 0.6 * np.sin(0.4 * x[i] + 0.8 * x[j])
                rot_term += 0.2 * np.sin(freq * (x[i] + x[j]) + phase) * np.cos(freq * (x[i] - x[j]) + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [0.4, 1.0, 2.8, 5.2, 7.9, 10.1]
            decay = 0.0
            for f in freqs:
                # Chaotic frequency modulation based on position
                mod_freq = f * (1.0 + 0.5 * np.sin(1.2 * x[i]) * np.cos(1.0 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.25 * decay
        
        # Basin boundary with irregular fractal-like irregularities and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.1 * x[i]**6 + 0.04 * np.sin(20 * x[i]) + 0.03 * np.random.rand()
            else:
                basin_term += 0.2 * np.abs(x[i])**2.7 + 0.05 * np.cos(9 * x[i]) + 0.02 * np.random.rand()
        
        # Chaotic sine-wave component with adaptive amplitude
        chaos_term = 0.0
        for i in range(self.dim):
            amp = 0.6 + 0.4 * np.sin(1.0 * x[i])
            chaos_term += amp * np.sin(200 * x[i]) * np.exp(-0.8 * x[i]**2)
        
        # Add a new chaotic cross-term interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.15 * np.sin(3.0 * x[i] + 2.0 * x[j]) * np.cos(2.5 * x[i] - 1.5 * x[j])
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term + cross_term