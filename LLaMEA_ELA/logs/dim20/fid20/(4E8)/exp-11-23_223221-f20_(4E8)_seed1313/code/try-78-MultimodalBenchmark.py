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
        
        # Quaternion-inspired rotational symmetry terms
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                rot_term += 0.08 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Multi-scale exponential decay with irregular frequencies
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 4.0, 6.5]
            decay = 0.0
            for f in freqs:
                decay += np.exp(-f * np.abs(x[i])) * np.sin(f * x[i])
            decay_term += 0.12 * decay
        
        # Basin boundary irregularity with piecewise polynomial
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.05 * x[i]**4
            else:
                basin_term += 0.1 * np.abs(x[i])**1.5
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term