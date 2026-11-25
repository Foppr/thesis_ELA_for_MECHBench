import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with chaotic phase couplings and fractal scaling
        exp_term = 0
        for i in range(self.dim):
            decay_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    phase = np.sin(x_norm[i] * x_norm[j] * 11.0 + np.pi * np.sin(x_norm[i] * 3.0))
                    fractal_scale = 1.0 + 0.3 * np.sin(x_norm[i] * x_norm[j] * 7.0) * np.cos(x_norm[i] * 5.0)
                    decay_sum += np.exp(-distance * 4.0 * fractal_scale) * np.sin(7 * np.pi * distance + phase)
            exp_term += decay_sum * (x_norm[i]**2 + 0.3)
        
        # Enhanced trigonometric coupling with chaotic frequency modulation and multi-scale harmonics
        trig_term = 0
        for i in range(self.dim):
            freq = 3.0 + 0.8 * np.sin(x_norm[i] * np.pi * 3.5) * np.cos(x_norm[i] * np.pi / 3.0)
            multi_harmonic = np.cos(freq * x_norm[i] * 9) * np.sin(freq * x_norm[i] * 7) * np.exp(-np.abs(x_norm[i]))
            trig_term += multi_harmonic
        
        # Enhanced adaptive conditioning with fractal-like scaling factors
        cond_term = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.6 * np.sin(x_norm[i] * np.pi * 4.0) * np.cos(x_norm[i] * np.pi / 2.0)
            cond_term += scale_factor * x_norm[i]**5
        
        # Multi-scale harmonic oscillations with fractal phase shifts and chaotic resonance
        harm_term = 0
        scales = [1.5, 3.2, 4.1, 5.7, 6.3, 7.9]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            phase_shift = np.sin(x_norm[i] * scale * np.pi * 2.0 + np.pi * np.cos(x_norm[i] * 2.5))
            harm_term += np.cos(x_norm[i] * scale * np.pi + phase_shift) * np.sin(x_norm[i] * scale * np.pi / 4.0)
        
        # Cross-dimensional polynomial interactions with fractal weights and chaotic resonance
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.4 * np.sin(x_norm[i] * x_norm[j] * 10.0 + np.pi * np.sin(x_norm[i] * 2.0))
                cross_term += (x_norm[i]**6 + x_norm[j]**5) * np.cos(x_norm[i] * x_norm[j]) * weight
        
        # Enhanced chaotic radial basis function components with fractal centers
        rbf_term = 0
        centers = np.random.uniform(-1, 1, (self.dim, 5))
        for i in range(self.dim):
            rbf_sum = 0
            for c in centers[i]:
                fractal_factor = 1.0 + 0.2 * np.sin(c * 7.0) * np.cos(c * 3.0)
                rbf_sum += np.exp(-np.abs(x_norm[i] - c) * 5.0 * fractal_factor) * np.sin(3 * np.pi * (x_norm[i] - c))
            rbf_term += rbf_sum
        
        # Add fractal-like self-similarity patterns
        self_sim_term = 0
        for i in range(self.dim):
            self_sim_term += np.sin(x_norm[i] * 12.0) * np.cos(x_norm[i] * 8.0) * np.exp(-np.abs(x_norm[i]) * 2.0)
        
        # Combine all terms with dynamic weighting and chaotic scaling
        result = 0.20 * exp_term + 0.20 * trig_term + 0.15 * cond_term + \
                 0.15 * harm_term + 0.13 * cross_term + 0.07 * rbf_term + 0.10 * self_sim_term
        
        # Add chaotic global scaling factor with fractal characteristics
        chaotic_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm**2) * 7.0 + np.pi * np.cos(np.sum(x_norm)))
        return result * chaotic_factor * (1 + 0.3 * np.sum(x_norm**2))