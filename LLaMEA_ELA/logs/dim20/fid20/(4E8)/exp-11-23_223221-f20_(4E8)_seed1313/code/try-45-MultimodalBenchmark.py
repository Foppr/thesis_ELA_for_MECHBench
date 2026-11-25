import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced chaotic sine oscillations with higher frequency modulation
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * np.pi / 3.0) + 0.3 * np.cos(i * np.pi / 2.0)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]**1.5) + 0.15 * np.sin(7 * x[i])
        
        # Stronger polynomial interaction terms with cubic and quartic couplings
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended cross-dimension interaction
                result += 0.1 * (x[i]**2) * (x[j]**3) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Additional exponential decay with enhanced sinusoidal coupling
        decay_term = 0.0
        for i in range(self.dim):
            decay_term += np.exp(-0.3 * x[i]**2) * np.cos(3 * np.pi * x[i]) + 0.05 * np.sin(4 * x[i])
        result += 0.4 * decay_term
        
        # Novel cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.08 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j]) * (x[i]**2 + x[j]**2)
        result += cross_term
        
        # Add chaotic noise-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(12 * x[i]) * np.cos(9 * x[i]) + 0.02 * np.tan(0.5 * x[i])
        result += noise
        
        # Normalize and return
        return result / self.dim