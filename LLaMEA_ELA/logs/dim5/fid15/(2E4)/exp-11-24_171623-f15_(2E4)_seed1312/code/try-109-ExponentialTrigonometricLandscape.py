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
                    decay_sum += np.exp(-distance * 2.5) * np.sin(3 * np.pi * distance)
            exp_term += decay_sum * (x_norm[i]**2 + 0.3)
        
        # Trigonometric coupling with frequency modulation
        trig_term = 0
        for i in range(self.dim):
            freq = 1.5 + 0.4 * np.cos(x_norm[i] * np.pi / 3)
            trig_term += np.cos(freq * x_norm[i] * 6) * np.sin(freq * x_norm[i] * 4)
        
        # Adaptive conditioning based on coordinate magnitude
        cond_term = 0
        for i in range(self.dim):
            cond_term += (1 + 0.4 * np.abs(x_norm[i])) * x_norm[i]**3
        
        # Multi-scale harmonic oscillations with phase shifts
        harm_term = 0
        scales = [1, 2.5, 3.5, 4.5]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            harm_term += np.cos(x_norm[i] * scale * np.pi) * np.sin(x_norm[i] * scale * np.pi / 2.5)
        
        # Cross-dimensional polynomial interactions with mixed degrees
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_norm[i]**4 + x_norm[j]**3) * np.cos(x_norm[i] * x_norm[j])
        
        # Combine all terms with dynamic weighting
        result = 0.3 * exp_term + 0.25 * trig_term + 0.18 * cond_term + \
                 0.2 * harm_term + 0.07 * cross_term
        
        # Add a global scaling factor to adjust difficulty
        return result * (1 + 0.15 * np.sum(x_norm**2))