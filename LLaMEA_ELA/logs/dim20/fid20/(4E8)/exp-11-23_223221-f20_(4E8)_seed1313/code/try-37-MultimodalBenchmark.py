import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Chaotic sine oscillations with varying frequencies
        for i in range(self.dim):
            freq = 1.0 + 0.2 * np.sin(i * np.pi / 4.0)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.1 * np.sin(5 * x[i])
        
        # Polynomial interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimension interaction
                result += 0.05 * (x[i]**3) * (x[j]**2) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Exponential decay with sinusoidal modulation
        decay_term = 0.0
        for i in range(self.dim):
            decay_term += np.exp(-0.5 * x[i]**2) * np.cos(2 * np.pi * x[i])
        result += 0.3 * decay_term
        
        # Add noise-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(10 * x[i]) * np.cos(7 * x[i])
        result += noise
        
        # Normalize and return
        return result / self.dim