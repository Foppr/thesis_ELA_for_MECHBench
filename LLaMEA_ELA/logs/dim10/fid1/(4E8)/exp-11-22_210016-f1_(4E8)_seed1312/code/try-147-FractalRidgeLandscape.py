import numpy as np

class FractalRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with fractal scaling
        base = np.sum(x**2)
        
        # Nested sinusoidal modulations with varying frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)  # Frequencies 2, 4, 8 repeating
            sin_mod += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Power-law scaling with fractal dimension
        power_scale = 0.0
        for i in range(self.dim):
            power_scale += (np.abs(x[i])**1.5 + 0.1 * np.abs(x[i])**3.0) * \
                          np.exp(-0.1 * x[i]**2)
        
        # Asymmetric dimensional coupling with exponential weights
        asym_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric weights based on dimension indices
                weight_i = 1.0 / (1.0 + 0.5 * np.exp(0.2 * i))
                weight_j = 1.0 / (1.0 + 0.5 * np.exp(0.2 * j))
                asym_coupling += weight_i * weight_j * \
                                np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Chaotic ridge structure with logistic map modulation
        chaotic_ridge = 0.0
        for i in range(self.dim):
            # Logistic map-like behavior
            log_term = np.sin(3.14159 * x[i]) * np.exp(-0.5 * x[i]**2)
            chaotic_ridge += log_term * (1.0 + 0.3 * np.sin(2.0 * x[i]))
        
        # Combined function with dynamic weights
        result = 0.5 * base + 0.8 * sin_mod + 0.6 * power_scale + \
                 0.4 * asym_coupling + 0.7 * chaotic_ridge
        
        return result