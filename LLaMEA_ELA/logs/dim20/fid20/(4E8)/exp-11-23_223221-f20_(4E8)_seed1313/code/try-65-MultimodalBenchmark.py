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
            freq = 1.5 + 0.3 * np.sin(i * np.pi / 3.0)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.15 * np.sin(6 * x[i])
        
        # Enhanced polynomial interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended cross-dimension interaction
                result += 0.08 * (x[i]**2) * (x[j]**3) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Modified exponential decay with sinusoidal modulation
        decay_term = 0.0
        for i in range(self.dim):
            decay_term += np.exp(-0.6 * x[i]**2) * np.cos(3 * np.pi * x[i])
        result += 0.4 * decay_term
        
        # Add noise-like perturbations with higher frequency components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(12 * x[i]) * np.cos(8 * x[i])
        result += noise
        
        # Normalize and return
        return result / self.dim