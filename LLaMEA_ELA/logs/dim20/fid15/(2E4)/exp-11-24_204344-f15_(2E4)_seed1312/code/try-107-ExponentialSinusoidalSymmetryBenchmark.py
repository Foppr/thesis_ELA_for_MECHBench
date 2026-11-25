import numpy as np

class ExponentialSinusoidalSymmetryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial component with nested exponential oscillations
        r = np.sqrt(np.sum(x**2))
        radial = np.exp(-0.2 * r) * np.sin(8 * r) * np.cos(3 * r)
        
        # Multi-scale sinusoidal modulations with dynamic frequencies and amplitudes
        sin_mod = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(i * 0.5)
            amp = 1.2 + 0.8 * np.cos(i * 0.3)
            sin_mod += amp * np.sin(freq * x[i] + 1.5) * np.cos(freq * x[i] + 0.7)
        
        # Adaptive exponential decay with multi-modal scaling
        exp_decay = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i] + 0.8)) * (1.0 + 0.5 * np.sin(2 * x[i]))
            exp_decay += scale * np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(5.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Complex cross-dimensional interaction with polynomial and trigonometric coupling
        cross_exp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_exp += (np.exp(-0.4 * (x[i]**2 + x[j]**2)) * 
                             np.cos(3.0 * x[i] * x[j]) * 
                             (1.0 + 0.3 * np.sin(x[i] + x[j])))
        
        # Harmonic landscape with frequency modulation and amplitude scaling
        harmonic = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.7 * np.sin(i * 0.4)
            amp = 1.0 + 0.3 * np.cos(i * 0.5)
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + 0.5) * np.exp(-0.2 * np.abs(x[i]))
        
        # Multi-scale oscillatory behavior with radial dependence and varying decay rates
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += (np.sin(13 * x[i]) * np.cos(11 * x[i]) * 
                           np.exp(-0.15 * np.abs(x[i])) * 
                           (1.0 + 0.2 * np.sin(3 * x[i])))
        
        # Asymmetric potential wells with multiple local minima and varying depths
        wells = 0.0
        for i in range(self.dim):
            wells += ((x[i]**2 - 2.5 * x[i] + 1.5) * 
                     np.exp(-0.5 * (x[i] - 1.3)**2) * 
                     (1.0 + 0.4 * np.cos(2 * x[i])))
        
        # Additional complex interaction term with cubic and quartic components
        cubic_interaction = 0.0
        for i in range(self.dim):
            cubic_interaction += (x[i]**3 - 1.8 * x[i]**2 + 0.9 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Final combination with increased complexity and varied weights
        return (0.4 * radial + 0.5 * sin_mod + 0.6 * exp_decay + 0.7 * cross_exp + 
                0.8 * harmonic + 0.9 * oscillatory + 1.0 * wells + 0.3 * cubic_interaction)