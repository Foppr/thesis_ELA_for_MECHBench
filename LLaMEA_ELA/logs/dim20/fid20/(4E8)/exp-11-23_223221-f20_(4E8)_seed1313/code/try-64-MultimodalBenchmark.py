import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced chaotic sine oscillations with dynamic frequencies
        for i in range(self.dim):
            freq = 1.5 + 0.5 * np.sin(i * np.pi / 3.0) + 0.3 * np.cos(i * np.pi / 2.0)
            result += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.15 * np.sin(7 * x[i]) + 0.05 * np.sin(11 * x[i])
        
        # Higher-order polynomial interaction terms with cross-dimension coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased cross-dimension interaction
                result += 0.08 * (x[i]**4) * (x[j]**3) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Multi-scale exponential decay with trigonometric modulation
        decay_term = 0.0
        for i in range(self.dim):
            decay_term += (np.exp(-0.3 * x[i]**2) * np.cos(3 * np.pi * x[i]) + 
                          0.5 * np.exp(-0.7 * x[i]**2) * np.sin(4 * np.pi * x[i]))
        result += 0.4 * decay_term
        
        # Noise-like perturbations with varying amplitudes
        noise = 0.0
        for i in range(self.dim):
            noise += 0.03 * np.sin(12 * x[i]) * np.cos(9 * x[i]) + 0.02 * np.sin(15 * x[i])
        result += noise
        
        # Add a global scaling factor to control the overall landscape difficulty
        result *= (1.0 + 0.1 * np.sin(np.sum(x**2) / self.dim))
        
        # Normalize and return
        return result / self.dim