import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Modified exponential decay terms with radial symmetry
        exp_term = np.sum(np.exp(-0.15 * x**2) * np.cos(2.5 * x))
        
        # Enhanced trigonometric interactions with varying frequencies
        trig_term = np.sum(np.sin(3.5 * x) * np.cos(1.8 * x) * np.sin(0.6 * x))
        
        # Augmented radial component with polynomial scaling
        radial_term = np.sum(x**2 * np.exp(-0.07 * np.sum(x**2)))
        
        # Enhanced cross-term interactions with sinusoidal modulation and increased complexity
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (np.sin(x[i] + x[i+1]) * 
                          (x[i]**3 + x[i+1]**3) * 
                          np.cos(0.4 * (x[i]**2 + x[i+1]**2)))
        
        # Additional chaotic component for increased multimodality
        chaotic_term = np.sum(np.sin(5.5 * x) * np.cos(2.8 * x) * np.exp(-0.12 * np.abs(x)))
        
        # Combined function with adjusted weights
        return 0.25 * exp_term + 0.35 * trig_term + 0.15 * radial_term + 0.2 * cross_term + 0.05 * chaotic_term