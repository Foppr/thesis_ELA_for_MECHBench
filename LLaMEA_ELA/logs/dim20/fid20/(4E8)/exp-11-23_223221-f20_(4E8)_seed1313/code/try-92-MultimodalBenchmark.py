import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial potentials with fractal scaling and cross-term interactions
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + 0.5 * np.abs(x[i]))
            poly_term += 0.4 * x[i]**3 * scale * np.exp(-0.15 * x[i]**2)
        
        # Logarithmic coupling with improved dimensionality interaction
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                log_coupling += 0.2 * np.log(1.0 + dist) * np.sin(x[i] * x[j] * 0.5)
        
        # Quaternion-inspired rotational symmetry with stronger coupling and adaptive modulation
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling for better conditioning
                freq = 1.0 + 0.4 * np.sin(0.6 * x[i])
                rot_term += 0.15 * np.sin(freq * (x[i] + x[j])) * np.cos(freq * (x[i] - x[j]))
        
        # Multi-scale exponential decay with enhanced frequency diversity
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [1.0, 3.0, 5.0, 7.0]
            decay = 0.0
            for f in freqs:
                mod_freq = f * (1.0 + 0.4 * np.sin(0.8 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.15 * decay
        
        # Basin boundary irregularity with enhanced nonlinearity and noise
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.5:
                basin_term += 0.06 * x[i]**4 + 0.03 * np.sin(12 * x[i])
            else:
                basin_term += 0.12 * np.abs(x[i])**1.7 + 0.04 * np.cos(6 * x[i])
        
        # Chaotic component with increased irregularity and reduced bias
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.02 * np.sin(150 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term