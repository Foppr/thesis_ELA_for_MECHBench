import numpy as np

class MultiScaleFractalLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like nested harmonic components
        fractal_harmonic = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.3 * x[i])
            fractal_harmonic += scale * (np.sin(2.0 * x[i]) + 0.3 * np.cos(4.0 * x[i])) * \
                               np.exp(-0.1 * x[i]**2)
        
        # Power-law cross-dimensional coupling
        power_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                power_coupling += (1.0 / (1.0 + distance**1.5)) * \
                                 np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        # Time-varying exponential modulation
        exp_modulation = 0.0
        for i in range(self.dim):
            t_var = 1.0 + 0.2 * np.sin(0.7 * x[i])
            exp_modulation += np.exp(-t_var * x[i]**2) * (x[i]**4 + 0.5 * x[i]**6)
        
        # Multi-scale oscillatory component
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (np.sin(1.0 * x[i]) + 0.5 * np.cos(3.0 * x[i]) + 
                           0.2 * np.sin(7.0 * x[i])) * \
                          np.exp(-0.05 * x[i]**2)
        
        # Fractional power interactions
        fractional_power = 0.0
        for i in range(self.dim):
            fractional_power += (np.abs(x[i])**1.3 + 0.1 * np.abs(x[i])**2.7) * \
                               np.cos(0.5 * x[i])
        
        # Combined landscape with adaptive weights
        result = 0.4 * fractal_harmonic + 0.6 * power_coupling + 0.5 * exp_modulation + \
                 0.3 * multi_scale + 0.7 * fractional_power
        
        return result