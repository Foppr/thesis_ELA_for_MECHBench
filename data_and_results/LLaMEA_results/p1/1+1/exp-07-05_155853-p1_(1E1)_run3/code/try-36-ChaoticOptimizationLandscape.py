import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractional Brownian motion-inspired fractal noise component
        fbm = 0
        for i in range(self.dim):
            fbm += (0.5 * np.sin(20 * x[i]) * np.cos(15 * x[i]) + 
                   0.3 * np.sin(35 * x[i]) * np.cos(25 * x[i]) + 
                   0.2 * np.sin(50 * x[i]) * np.cos(40 * x[i]) +
                   0.1 * np.sin(70 * x[i]))
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        multi_scale = 0
        for i in range(self.dim):
            multi_scale += (0.8 * np.sin(2 * x[i]) * np.cos(3 * x[i]) + 
                           0.6 * np.sin(5 * x[i]) * np.cos(7 * x[i]) + 
                           0.4 * np.sin(11 * x[i]) * np.cos(13 * x[i]) + 
                           0.2 * np.sin(17 * x[i]) * np.cos(19 * x[i]))
        
        # Higher-order polynomial with chaotic coefficient modulation
        polynomial = 0
        for i in range(self.dim):
            coeff = 0.1 + 0.2 * np.sin(10 * x[i])
            polynomial += coeff * (x[i]**6 + 0.5 * x[i]**5 - 0.3 * x[i]**4 + 
                                 0.1 * x[i]**3 - 0.05 * x[i]**2 + 0.02 * x[i])
        
        # Non-linear cross-dimensional coupling with exponential interaction
        cross_interaction = 0
        for i in range(self.dim - 1):
            diff = x[i] - x[i+1]
            cross_interaction += np.exp(-0.1 * np.abs(diff)) * (x[i]**4 + x[i+1]**4 + 
                                                              0.3 * x[i]**2 * x[i+1]**2 + 
                                                              0.1 * x[i] * x[i+1])
        
        # Dynamic scaling with multi-modal frequency modulation
        freq_mod = np.sin(0.5 * np.sum(x**2)) * np.cos(0.3 * np.sum(x**3))
        global_scale = 2.0 + 1.5 * freq_mod
        
        # Add fractal-like noise with varying intensity
        fractal_noise = 0.02 * np.sum(np.sin(100 * x) * np.cos(80 * x))
        
        # Combine all components with additional chaotic coupling
        chaotic_coupling = 0
        for i in range(self.dim):
            chaotic_coupling += np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.sin(15 * x[i])
        
        return global_scale * (fbm + multi_scale + polynomial + cross_interaction) + fractal_noise + chaotic_coupling