import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with nested exponential oscillations
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.15 * r) * np.sin(10 * r) * np.cos(4 * r)
        
        # Multi-scale sinusoidal modulations with dynamic frequencies and amplitudes
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 2.5 + 3.0 * np.sin(i * 0.6)
            amp = 1.5 + 0.5 * np.cos(i * 0.4)
            sin_mod += amp * np.sin(freq * x[i] + 1.2) * np.cos(freq * x[i] + 0.8)
        
        # Adaptive exponential decay with multi-modal scaling
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 1.0)) * (1.0 + 0.6 * np.sin(2.5 * x[i]))
            exp_decay += scale * np.exp(-0.4 * (x[i] - 1.2)**2) * np.sin(6.0 * x[i]) * np.cos(2.5 * x[i])
        
        # Complex cross-dimensional interaction with polynomial and trigonometric coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += (np.exp(-0.3 * (x[i]**2 + x[j]**2)) * 
                             np.cos(4.0 * x[i] * x[j]) * 
                             (1.0 + 0.4 * np.sin(x[i] + x[j])))
        
        # Harmonic landscape with frequency modulation and amplitude scaling
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.8 * np.sin(i * 0.5)
            amp = 1.2 + 0.4 * np.cos(i * 0.6)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + 0.6) * np.exp(-0.25 * np.abs(x[i]))
        
        # Multi-scale oscillatory behavior with radial dependence and varying decay rates
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += (np.sin(15 * x[i]) * np.cos(13 * x[i]) * 
                           np.exp(-0.2 * np.abs(x[i])) * 
                           (1.0 + 0.3 * np.sin(4 * x[i])))
        
        # Asymmetric potential wells with multiple local minima and varying depths
        wells = 0.0
        for i in range(self.dim):
            wells += ((x[i]**2 - 2.2 * x[i] + 1.3) * 
                     np.exp(-0.4 * (x[i] - 1.1)**2) * 
                     (1.0 + 0.5 * np.cos(2.5 * x[i])))
        
        # Additional complex interaction term with cubic and quartic components
        cubic_interaction = 0.0
        for i in range(self.dim):
            cubic_interaction += (x[i]**3 - 2.0 * x[i]**2 + 1.0 * x[i]) * np.exp(-0.35 * x[i]**2)
        
        # Final combination with increased complexity and varied weights
        return (0.5 * radial + 0.6 * sin_mod + 0.7 * exp_decay + 0.8 * cross_exp + 
                0.9 * harmonic + 1.0 * oscillatory + 1.1 * wells + 0.4 * cubic_interaction)