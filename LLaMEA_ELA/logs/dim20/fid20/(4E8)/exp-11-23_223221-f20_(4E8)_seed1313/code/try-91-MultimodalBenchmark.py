import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar polynomial potentials with fractal scaling and chaotic modulations
        poly_term = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.abs(x[i]))
            poly_term += 0.3 * (x[i] ** 3) * scale * np.exp(-0.1 * x[i]**2) * np.sin(2.5 * x[i])
        
        # Logarithmic coupling with adaptive noise
        log_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                noise = 0.05 * np.sin(x[i] * x[j] * 3.0) * np.cos(0.5 * (x[i] + x[j]))
                log_coupling += 0.15 * np.log(1.0 + dist) * np.sin(x[i] * x[j]) * (1.0 + noise)
        
        # Enhanced quaternion-inspired rotational symmetry with multi-frequency components
        rot_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                freqs = [1.0, 2.0, 3.0]
                rot_contrib = 0.0
                for f in freqs:
                    rot_contrib += np.sin(f * x[i] + f * x[j]) * np.cos(f * x[i] - f * x[j])
                rot_term += 0.1 * rot_contrib
        
        # Multi-scale exponential decay with chaotic frequencies and irregular amplitudes
        decay_term = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.5, 4.0, 6.5, 8.0]
            amplitudes = [0.1, 0.15, 0.12, 0.08, 0.05]
            decay = 0.0
            for f, a in zip(freqs, amplitudes):
                decay += a * np.exp(-f * np.abs(x[i])) * np.sin(f * x[i] + 0.3 * np.cos(2.0 * x[i]))
            decay_term += decay
        
        # Basin boundary irregularity with chaotic piecewise polynomial and sine-wave perturbations
        basin_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) < 2.0:
                basin_term += 0.05 * x[i]**4 * (1.0 + 0.2 * np.sin(5.0 * x[i]))
            else:
                basin_term += 0.1 * np.abs(x[i])**1.5 * (1.0 + 0.15 * np.cos(3.0 * x[i]))
        
        # Chaotic sine-wave modulation to increase landscape ruggedness
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += 0.2 * np.sin(10.0 * x[i] + np.sin(7.0 * x[i])) * np.cos(3.0 * x[i])
        
        return poly_term + log_coupling + rot_term + decay_term + basin_term + chaos_term