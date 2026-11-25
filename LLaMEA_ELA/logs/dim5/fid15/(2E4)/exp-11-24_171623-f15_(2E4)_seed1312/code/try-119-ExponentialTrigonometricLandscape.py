import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with chaotic phase couplings and dynamic weights
        exp_term = 0
        for i in range(self.dim):
            decay_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    phase = np.sin(x_norm[i] * x_norm[j] * 8.0 + np.pi * i / self.dim)
                    weight = 1.0 + 0.4 * np.sin(x_norm[i] * x_norm[j] * 5.0)
                    decay_sum += np.exp(-distance * 2.0) * np.sin(7 * np.pi * distance + phase) * weight
            exp_term += decay_sum * (x_norm[i]**2 + 0.3)
        
        # Improved trigonometric coupling with dynamic frequency modulation
        trig_term = 0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(x_norm[i] * np.pi * 3.0) * np.cos(x_norm[i] * np.pi / 3)
            trig_term += np.cos(freq * x_norm[i] * 6) * np.sin(freq * x_norm[i] * 4) * np.exp(-np.abs(x_norm[i]))
        
        # Enhanced adaptive conditioning with chaotic scaling factors
        cond_term = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(x_norm[i] * np.pi * 4.0)
            cond_term += scale_factor * x_norm[i]**5
        
        # Multi-scale harmonic oscillations with enhanced chaotic phase shifts
        harm_term = 0
        scales = [1.5, 3.2, 4.1, 5.7, 6.3]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            phase_shift = np.sin(x_norm[i] * scale * np.pi * 2.0 + np.pi * i / self.dim)
            harm_term += np.cos(x_norm[i] * scale * np.pi + phase_shift) * np.sin(x_norm[i] * scale * np.pi / 4.0)
        
        # Enhanced cross-dimensional polynomial interactions with chaotic weights
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.5 * np.sin(x_norm[i] * x_norm[j] * 9.0 + np.pi * (i+j) / self.dim)
                cross_term += (x_norm[i]**6 + x_norm[j]**5) * np.cos(x_norm[i] * x_norm[j]) * weight
        
        # Enhanced chaotic radial basis function components
        rbf_term = 0
        centers = np.random.uniform(-1, 1, (self.dim, 4))
        for i in range(self.dim):
            rbf_sum = 0
            for c in centers[i]:
                rbf_sum += np.exp(-np.abs(x_norm[i] - c) * 3.5) * np.sin(3 * np.pi * (x_norm[i] - c))
            rbf_term += rbf_sum
        
        # Combine all terms with refined dynamic weighting
        result = 0.28 * exp_term + 0.20 * trig_term + 0.18 * cond_term + \
                 0.16 * harm_term + 0.10 * cross_term + 0.08 * rbf_term
        
        # Enhanced chaotic global scaling factor
        chaotic_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm**2) * 6.0)
        return result * chaotic_factor * (1 + 0.15 * np.sum(x_norm**2))