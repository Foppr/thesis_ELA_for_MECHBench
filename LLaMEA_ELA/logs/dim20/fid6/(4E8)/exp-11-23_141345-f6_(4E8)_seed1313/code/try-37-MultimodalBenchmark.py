import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay terms with radial symmetry
        exp_term = np.sum(np.exp(-0.1 * x**2) * np.cos(2.0 * x))
        
        # Trigonometric interactions with varying frequencies
        trig_term = np.sum(np.sin(3.0 * x) * np.cos(1.5 * x) * np.sin(0.5 * x))
        
        # Radial component with polynomial scaling
        radial_term = np.sum(x**2 * np.exp(-0.05 * np.sum(x**2)))
        
        # Enhanced cross-term interactions with sinusoidal modulation and increased complexity
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (np.sin(x[i] + x[i+1]) * 
                          (x[i]**3 + x[i+1]**3) * 
                          np.cos(0.3 * (x[i]**2 + x[i+1]**2)))
        
        # Additional chaotic component for increased multimodality
        chaotic_term = np.sum(np.sin(5.0 * x) * np.cos(2.5 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combined function with adjusted weights
        return 0.2 * exp_term + 0.3 * trig_term + 0.2 * radial_term + 0.25 * cross_term + 0.05 * chaotic_term