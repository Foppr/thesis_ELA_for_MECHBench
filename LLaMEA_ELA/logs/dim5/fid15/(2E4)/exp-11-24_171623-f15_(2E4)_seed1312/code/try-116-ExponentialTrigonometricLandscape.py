import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay interactions with chaotic phase couplings
        exp_term = 0
        for i in range(self.dim):
            decay_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    phase = np.sin(x_norm[i] * x_norm[j] * 7.0)
                    decay_sum += np.exp(-distance * 3.0) * np.sin(5 * np.pi * distance + phase)
            exp_term += decay_sum * (x_norm[i]**2 + 0.4)
        
        # Trigonometric coupling with chaotic frequency modulation
        trig_term = 0
        for i in range(self.dim):
            freq = 2.0 + 0.6 * np.sin(x_norm[i] * np.pi * 2.5) * np.cos(x_norm[i] * np.pi / 4)
            trig_term += np.cos(freq * x_norm[i] * 7) * np.sin(freq * x_norm[i] * 5) * np.exp(-np.abs(x_norm[i]))
        
        # Adaptive conditioning with chaotic scaling factors
        cond_term = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(x_norm[i] * np.pi * 3.0)
            cond_term += scale_factor * x_norm[i]**4
        
        # Multi-scale harmonic oscillations with chaotic phase shifts
        harm_term = 0
        scales = [1.2, 2.8, 3.7, 4.9, 5.3]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            phase_shift = np.sin(x_norm[i] * scale * np.pi * 1.5)
            harm_term += np.cos(x_norm[i] * scale * np.pi + phase_shift) * np.sin(x_norm[i] * scale * np.pi / 3.0)
        
        # Cross-dimensional polynomial interactions with chaotic weights
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.3 * np.sin(x_norm[i] * x_norm[j] * 8.0)
                cross_term += (x_norm[i]**5 + x_norm[j]**4) * np.cos(x_norm[i] * x_norm[j]) * weight
        
        # Add chaotic radial basis function components
        rbf_term = 0
        centers = np.random.uniform(-1, 1, (self.dim, 3))
        for i in range(self.dim):
            rbf_sum = 0
            for c in centers[i]:
                rbf_sum += np.exp(-np.abs(x_norm[i] - c) * 4.0) * np.sin(2 * np.pi * (x_norm[i] - c))
            rbf_term += rbf_sum
        
        # Combine all terms with dynamic weighting and chaotic scaling
        result = 0.25 * exp_term + 0.22 * trig_term + 0.15 * cond_term + \
                 0.18 * harm_term + 0.12 * cross_term + 0.08 * rbf_term
        
        # Add chaotic global scaling factor
        chaotic_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm**2) * 5.0)
        return result * chaotic_factor * (1 + 0.2 * np.sum(x_norm**2))