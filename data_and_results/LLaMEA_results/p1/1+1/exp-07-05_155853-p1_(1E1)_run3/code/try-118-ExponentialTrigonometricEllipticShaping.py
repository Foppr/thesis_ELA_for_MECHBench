import numpy as np

class ExponentialTrigonometricEllipticShaping:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay components with dynamic rates
        exp_decay_sum = 0
        for i in range(self.dim):
            rate = 0.5 + 0.5 * np.sin(i * 0.6)
            exp_decay_sum += np.exp(-rate * np.abs(x[i])) * np.cos(rate * x[i]**2)
        
        # Trigonometric wave interactions with varying amplitudes and frequencies
        trig_wave_sum = 0
        for i in range(self.dim):
            amp = 1.0 + 0.3 * np.sin(i * 0.4)
            freq = 1.0 + 0.4 * np.cos(i * 0.5)
            trig_wave_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Adaptive elliptic shaping with dynamic eccentricity
        elliptic_sum = 0
        for i in range(self.dim - 1):
            eccentricity = 0.2 + 0.8 * np.abs(np.sin(i * 0.3))
            elliptic_sum += (x[i]**2 / (1.0 + eccentricity)**2 + x[i+1]**2 / (1.0 + eccentricity)**2) * np.exp(-0.1 * (x[i] + x[i+1])**2)
        
        # Dynamic conditioning with chaotic scaling factors
        cond_sum = 0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            cond_sum += scale * x[i]**2 * np.exp(-0.05 * x[i]**2)
        
        # Saddle-point distribution with alternating signs
        saddle_sum = 0
        for i in range(self.dim):
            sign = (-1)**i
            saddle_sum += sign * x[i]**2 * np.sin(0.5 * x[i]**2)
        
        # Cross-dimensional coupling with dynamic weights
        cross_sum = 0
        for i in range(self.dim - 2):
            weight = 0.3 + 0.7 * np.abs(np.sin(i * 0.8))
            cross_sum += weight * (x[i] * x[i+1] * x[i+2])**2
        
        # Global modulation with multiple harmonic components
        global_mod = np.sin(0.3 * np.sum(x)) * np.cos(0.2 * np.sum(x**2)) * np.exp(-0.1 * np.sum(np.abs(x)))
        
        # Add a new exponential interaction term for enhanced ruggedness
        new_exp = 0
        for i in range(self.dim - 1):
            new_exp += 0.02 * np.exp(-0.5 * (x[i]**2 + x[i+1]**2)) * np.sin(2.0 * x[i] * x[i+1])
        
        # Combine all components with refined scaling factors
        return 1.5 * exp_decay_sum + 1.2 * trig_wave_sum + 0.8 * elliptic_sum + 0.6 * cond_sum + 0.4 * saddle_sum + 0.3 * cross_sum + 0.2 * global_mod + 0.1 * new_exp