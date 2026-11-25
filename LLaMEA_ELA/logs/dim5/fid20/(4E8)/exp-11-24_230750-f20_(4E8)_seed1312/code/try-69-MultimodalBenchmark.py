import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical basin component with adaptive scaling
        spherical = 0.5 * np.sum(x**2)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_osc = 0.3 * np.sum(np.sin(2 * np.pi * x) + 0.5 * np.sin(4 * np.pi * x) + 
                              0.2 * np.sin(8 * np.pi * x))
        
        # Adaptive penalty landscape with dynamic thresholds
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 3.0:
                penalty += 10 * (abs(x[i]) - 3.0)**2
            elif abs(x[i]) > 1.0:
                penalty += 5 * (abs(x[i]) - 1.0)**2
        
        # Cross-term interactions with exponential weighting
        cross_terms = 0.0
        for i in range(self.dim - 2):
            cross_terms += np.exp(-0.1 * abs(x[i] + x[i+1] + x[i+2])) * \
                          (x[i]**2 + x[i+1]**2 + x[i+2]**2)
        
        # Chaotic component using logistic map dynamics
        chaotic = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                chaotic += np.sin(r * (x[i] / 5.0) * (1 - x[i] / 5.0))
            else:
                chaotic += np.sin(r * (x[i] / 5.0) * (1 - x[i] / 5.0)) * \
                          np.sin(r * (x[i-1] / 5.0) * (1 - x[i-1] / 5.0))
        
        # Combined function value
        return spherical + sin_osc + penalty + cross_terms + chaotic