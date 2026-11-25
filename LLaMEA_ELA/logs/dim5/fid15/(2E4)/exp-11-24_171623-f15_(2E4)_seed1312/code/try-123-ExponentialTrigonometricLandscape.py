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
                    phase_shift = np.sin(x_norm[i] * x_norm[j] * 7.0)
                    decay_sum += np.exp(-distance * 3.0) * np.sin(4 * np.pi * distance + phase_shift)
            exp_term += decay_sum * (np.tanh(x_norm[i]) ** 2 + 0.5)
        
        # Trigonometric coupling with hyperbolic tangent conditioning
        trig_term = 0
        for i in range(self.dim):
            freq = 2.0 + 0.6 * np.tanh(x_norm[i] * 2.0)
            trig_term += np.cos(freq * x_norm[i] * 8) * np.sin(freq * x_norm[i] * 5) * np.tanh(x_norm[i])
        
        # Adaptive conditioning with hyperbolic tangent and fractal scaling
        cond_term = 0
        for i in range(self.dim):
            cond_term += (1 + 0.5 * np.abs(np.tanh(x_norm[i]))) * x_norm[i]**4
        
        # Multi-scale harmonic oscillations with fractal self-similarity
        harm_term = 0
        scales = [1, 3.2, 5.1, 7.3]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            harm_term += np.cos(x_norm[i] * scale * np.pi) * np.sin(x_norm[i] * scale * np.pi / 3.0) * np.tanh(x_norm[i])
        
        # Cross-dimensional polynomial interactions with resonance and chaotic weights
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(x_norm[i] * x_norm[j] * 9.0) + 0.5
                cross_term += (x_norm[i]**3 + x_norm[j]**2) * np.cos(x_norm[i] * x_norm[j]) * weight
        
        # Add fractal-like self-similarity pattern with dynamic scaling
        fractal_term = 0
        for i in range(self.dim):
            fractal_term += np.sin(x_norm[i] * 10.0) * np.cos(x_norm[i] * 5.0) * (1 + 0.3 * np.sin(x_norm[i] * 15.0))
        
        # Combine all terms with dynamic weighting and global scaling
        result = 0.28 * exp_term + 0.22 * trig_term + 0.15 * cond_term + \
                 0.18 * harm_term + 0.12 * cross_term + 0.05 * fractal_term
        
        # Add global scaling factor with chaotic modulation
        chaos_factor = 1 + 0.2 * np.sin(np.sum(x_norm**3))
        return result * chaos_factor * (1 + 0.2 * np.sum(x_norm**2))