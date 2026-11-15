import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random shifts for global minimum and frequency modulation
        self.shifts = np.random.uniform(-0.5, 0.5, dim)
        self.freq_mod = np.random.uniform(1.0, 10.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic multimodal components with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(self.freq_mod * np.pi * x_norm)**12 * np.exp(-0.5 * x_norm**2))
        f3 = 0.4 * np.sum(np.cos(4 * np.pi * x_norm + self.shifts)**10 * np.exp(-0.3 * x_norm**2))
        f4 = 0.3 * np.sum(np.sin(7 * np.pi * x_norm)**8 * np.exp(-0.7 * x_norm**2))
        f5 = 0.2 * np.sum((x_norm + 0.3)**8 * np.exp(-0.4 * x_norm**2))
        f6 = 0.15 * np.sum(np.cos(6 * np.pi * x_norm)**6 * np.exp(-0.6 * x_norm**2))
        
        # Exponentially weighted cross-terms with chaotic phase shifts
        cross_term = 0.08 * np.sum(np.exp(-5 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                                  np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:]) + self.shifts[:-1]) * 
                                  np.cos(2 * np.pi * (x_norm[:-1] - x_norm[1:]) + self.shifts[1:]))
        
        # Dynamic global minimum shift component
        shift_component = 0.1 * np.sum((x_norm - self.shifts)**4)
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5 + f6 + cross_term + shift_component