import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar polynomial potentials with fractal scaling and adaptive exponents
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.abs(x[i]))
            exp_factor = 2.0 + 0.5 * np.sin(0.5 * x[i])
            poly_term += 0.4 * (x[i] ** exp_factor) * scale * np.exp(-0.15 * x[i]**2)
        
        # Logarithmic coupling with adaptive weights based on dimensionality
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                weight = 0.2 * (1.0 + np.sin(0.3 * (i + j)))
                log_coupling += weight * np.log(1.0 + dist) * np.sin(x[i] * x[j])
        
        # Enhanced quaternion-inspired rotational symmetry terms with dynamic phase
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                phase = 0.5 * np.sin(0.2 * (i + j))
                rot_term += 0.1 * np.sin(x[i] + x[j] + phase) * np.cos(x[i] - x[j] + phase)
        
        # Multi-scale exponential decay with chaotic frequency modulation
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.8, 4.2, 6.7, 8.1]
            decay = 0.0
            for f in freqs:
                mod_freq = f * (1.0 + 0.3 * np.sin(0.4 * x[i]))
                decay += np.exp(-mod_freq * np.abs(x[i])) * np.sin(mod_freq * x[i])
            decay_term += 0.15 * decay
        
        # Basin boundary irregularity with chaotic polynomial transitions
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 1.5:
                basin_term += 0.07 * x[i]**5
            elif np.abs(x[i]) < 3.0:
                basin_term += 0.12 * np.abs(x[i])**2.3
            else:
                basin_term += 0.18 * np.abs(x[i])**1.7
        
        # Adaptive noise coupling term to increase landscape ruggedness
        noise_coupling = 0.0
        for i in range(self.dim):
            noise = 0.05 * np.random.normal(0, 1)
            noise_coupling += noise * np.exp(-0.2 * x[i]**2)
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + noise_coupling