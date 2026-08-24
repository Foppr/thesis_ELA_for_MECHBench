import numpy as np

class ExponentialSinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with varying rates
        exp_term = np.sum(np.exp(-0.5 * x**2) * np.exp(-0.1 * np.abs(x)))
        
        # Sinusoidal modulation with multiple frequencies and amplitudes
        sin_term = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * 
                         np.sin(5.0 * np.pi * x) * np.cos(7.0 * np.pi * x))
        
        # Radial interaction with distance-dependent weights
        radial_term = 0.0
        for i in range(self.dim):
            dist = np.sum((x - x[i])**2)
            radial_term += np.exp(-dist / (2.0 * (i + 1))) * np.sin(2.0 * np.pi * x[i])
        
        # Cross-dimensional coupling with polynomial interaction
        cross_term = np.sum((x[:-1] * x[1:])**(1.5) * np.sin(4.0 * np.pi * (x[:-1] + x[1:])))
        
        # Fractional power and logarithmic scaling for added complexity
        frac_term = np.sum(np.abs(x)**1.7 * np.log(np.abs(x) + 1.0))
        
        # Chaotic-like component with feedback and non-linearity
        chaotic_term = np.sum(np.sin(10.0 * x + np.sin(5.0 * x)) * np.exp(-0.3 * x**2))
        
        # Combined function with dynamic weights and normalization
        return 0.25 * exp_term + 0.20 * sin_term + 0.18 * radial_term + 0.15 * cross_term + 0.12 * frac_term + 0.10 * chaotic_term