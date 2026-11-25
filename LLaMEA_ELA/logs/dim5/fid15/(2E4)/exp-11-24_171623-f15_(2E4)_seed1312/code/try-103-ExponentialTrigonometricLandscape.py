import numpy as np

class ExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay interactions with adaptive weights
        exp_term = 0
        for i in range(self.dim):
            decay_sum = 0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(x_norm[i] - x_norm[j])
                    # Adaptive weighting based on coordinate values
                    weight = 1.0 + 0.5 * (np.abs(x_norm[i]) + np.abs(x_norm[j]))
                    decay_sum += np.exp(-distance * weight) * np.cos(2 * np.pi * distance)
            exp_term += decay_sum * (x_norm[i]**2 + 0.3)
        
        # Enhanced trigonometric coupling with dynamic frequencies
        trig_term = 0
        for i in range(self.dim):
            # Dynamic frequency modulation based on position
            freq = 1.5 + 0.8 * np.sin(x_norm[i] * np.pi / 4) + 0.3 * np.cos(x_norm[i] * np.pi / 2)
            trig_term += np.sin(freq * x_norm[i] * 5) * np.cos(freq * x_norm[i] * 2) * (1 + 0.1 * np.abs(x_norm[i]))
        
        # Enhanced adaptive conditioning with exponential scaling
        cond_term = 0
        for i in range(self.dim):
            # Exponential conditioning factor
            cond_factor = np.exp(0.5 * np.abs(x_norm[i]))
            cond_term += cond_factor * x_norm[i]**4
        
        # Multi-scale harmonic oscillations with phase shifts and amplitude modulation
        harm_term = 0
        scales = [1, 2, 3, 4, 6]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            # Amplitude modulation based on coordinate magnitude
            amp_mod = 1.0 + 0.2 * np.abs(x_norm[i])
            harm_term += amp_mod * np.sin(x_norm[i] * scale * np.pi) * np.cos(x_norm[i] * scale * np.pi / 4)
        
        # Enhanced cross-dimensional polynomial interactions with mixed degrees and coupling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling strength based on coordinate values
                coupling_strength = 1.0 + 0.3 * (np.abs(x_norm[i]) + np.abs(x_norm[j]))
                cross_term += coupling_strength * (x_norm[i]**3 + x_norm[j]**2) * np.sin(x_norm[i] * x_norm[j])
        
        # Combine all terms with optimized weighting
        result = 0.3 * exp_term + 0.25 * trig_term + 0.15 * cond_term + \
                 0.2 * harm_term + 0.1 * cross_term
        
        # Add global scaling and noise to improve benchmark characteristics
        return result * (1 + 0.05 * np.sum(x_norm**2)) + 0.01 * np.random.rand()