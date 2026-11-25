import numpy as np

class SinusoidalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = (x - self.bounds.lb) / (self.bounds.ub - self.bounds.lb) * 2 - 1
        
        # Base quadratic term with variable weights
        weights = np.linspace(0.5, 1.5, self.dim)
        f_val = np.sum(weights * x_norm**2)
        
        # Add chaotic sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Varying frequencies: 2, 4, 8, 16
            amp = 0.3 + 0.2 * np.sin(i)  # Varying amplitudes
            f_val += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i] / 2)
            
        # Add nested oscillations with different phase shifts
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-dimension interactions
                phase_shift = np.pi * (i + j) / (self.dim + 1)
                f_val += 0.2 * np.sin(5 * np.pi * (x_norm[i] + x_norm[j]) + phase_shift) * \
                         np.cos(3 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Add asymmetric basin terms to create non-uniform landscape
        asymmetry = 0.1 * np.sum(np.abs(x_norm)**3)
        f_val += asymmetry
        
        # Add a small chaotic component for increased complexity
        chaotic_term = 0.05 * np.sum(np.sin(100 * x_norm) * np.cos(77 * x_norm))
        f_val += chaotic_term
        
        return f_val