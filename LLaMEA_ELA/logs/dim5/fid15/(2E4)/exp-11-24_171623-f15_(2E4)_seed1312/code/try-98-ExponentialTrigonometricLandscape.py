import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay interactions with distance-dependent weights
        exp_term = 0
        for i in range(self.dim):
            decay_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    decay_sum += np.exp(-distance * 3.0) * np.cos(2 * np.pi * distance)
            exp_term += decay_sum * (x_norm[i]**2 + 0.5)
        
        # Trigonometric coupling with frequency modulation
        trig_term = 0
        for i in range(self.dim):
            freq = 1 + 0.5 * np.sin(x_norm[i] * np.pi / 2)
            trig_term += np.sin(freq * x_norm[i] * 7) * np.cos(freq * x_norm[i] * 3)
        
        # Adaptive conditioning based on coordinate magnitude
        cond_term = 0
        for i in range(self.dim):
            cond_term += (1 + 0.3 * np.abs(x_norm[i])) * x_norm[i]**4
        
        # Multi-scale harmonic oscillations with phase shifts
        harm_term = 0
        scales = [1, 2, 3, 5]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            harm_term += np.sin(x_norm[i] * scale * np.pi) * np.cos(x_norm[i] * scale * np.pi / 3)
        
        # Cross-dimensional polynomial interactions with mixed degrees
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i]**3 + x_norm[j]**2) * np.sin(x_norm[i] * x_norm[j])
        
        # Combine all terms with dynamic weighting
        result = 0.25 * exp_term + 0.2 * trig_term + 0.15 * cond_term + \
                 0.25 * harm_term + 0.15 * cross_term
        
        # Add a global scaling factor to adjust difficulty
        return result * (1 + 0.1 * np.sum(x_norm**2))