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
            freq = 1.2 + 0.4 * np.sin(i * np.pi / 2.5)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]**2.5) + 0.2 * np.sin(7 * x[i])
        
        # Enhanced polynomial interaction terms with modified exponents
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced cross-dimension interaction
                result += 0.1 * (x[i]**2.5) * (x[j]**2.8) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Modified exponential decay with sinusoidal modulation
        decay_term = 0.0
        for i in range(self.dim):
            decay_term += np.exp(-0.7 * x[i]**2) * np.cos(2.5 * np.pi * x[i])
        result += 0.35 * decay_term
        
        # Add noise-like perturbations with higher frequency components and altered coupling
        noise = 0.0
        for i in range(self.dim):
            noise += 0.04 * np.sin(10 * x[i]) * np.cos(9 * x[i])
        result += noise
        
        # Normalize and return
        return result / self.dim