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
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                freq = 1.0 + 0.6 * np.sin(0.6 * x[i])  # Increased frequency modulation
                rot_term += 0.12 * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
        
        # Multi-scale exponential decay with irregular frequencies and adaptive scaling
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [1.5, 3.0, 5.0, 7.0]  # Changed frequencies
            decay = 0.0
            for f in freqs:
                # Adaptive frequency modulation based on position
                mod_freq = f * (1.0 + 0.4 * np.sin(0.8 * x[i]))  # Increased modulation
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.15 * decay  # Increased coefficient
        
        # Improved basin boundary irregularity with piecewise polynomial and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.06 * x[i]**4 + 0.03 * np.sin(10 * x[i])  # Increased coefficients
            else:
                basin_term += 0.12 * np.abs(x[i])**1.5 + 0.04 * np.cos(5 * x[i])  # Increased coefficients
        
        # Add a small chaotic component to increase landscape irregularity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.015 * np.sin(120 * x[i]) * np.exp(-0.5 * x[i]**2)  # Increased frequency
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term