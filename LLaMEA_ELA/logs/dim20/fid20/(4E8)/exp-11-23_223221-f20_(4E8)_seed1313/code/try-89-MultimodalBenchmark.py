import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar polynomial potentials with fractal scaling
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.abs(x[i]))
            poly_term += 0.3 * (x[i] ** 3) * scale * np.exp(-0.1 * x[i]**2)
        
        # Logarithmic coupling between dimensions
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                log_coupling += 0.15 * np.log(1.0 + dist) * np.sin(x[i] * x[j])
        
        # Enhanced quaternion-inspired rotational symmetry terms with adaptive coupling
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                freq = 1.0 + 0.5 * np.sin(0.5 * x[i])
                rot_term += 0.1 * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
        
        # Multi-scale exponential decay with irregular frequencies and adaptive scaling
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 4.0, 6.5]
            decay = 0.0
            for f in freqs:
                # Adaptive frequency modulation based on position
                mod_freq = f * (1.0 + 0.3 * np.sin(0.7 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.12 * decay
        
        # Improved basin boundary irregularity with piecewise polynomial and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.05 * x[i]**4 + 0.02 * np.sin(10 * x[i])
            else:
                basin_term += 0.1 * np.abs(x[i])**1.5 + 0.03 * np.cos(5 * x[i])
        
        # Add a small chaotic component to increase landscape irregularity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.01 * np.sin(100 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term