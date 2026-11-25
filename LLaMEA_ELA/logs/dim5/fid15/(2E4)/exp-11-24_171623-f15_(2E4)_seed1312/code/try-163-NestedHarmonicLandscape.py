import numpy as np

class NestedHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-scale harmonic oscillations with nested frequencies and phase shifts
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq_scale = 2**(i % 5)
            base_freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            phase_shift = np.cos(i * np.pi / (self.dim + 3))
            harmonic_sum += np.sin(freq_scale * base_freq * x_norm[i] + phase_shift) * np.cos(freq_scale * base_freq * x_norm[i] + phase_shift)
        
        # Adaptive radial basis functions with dynamic bandwidths and dimension-specific centers
        rb_sum = 0.0
        for i in range(min(6, self.dim)):
            center = np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 4))
            # Dynamic bandwidth based on dimension index and frequency
            bandwidth = 0.15 + 0.35 * (i % 4) / 3.0
            rb_sum += np.exp(-0.5 * np.sum((x_norm - center)**2) / (bandwidth**2)) * np.sin(i * x_norm[i] + i * 0.1)
        
        # Fractal-like gradient modulation with recursive scaling and dimension coupling
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = 1.0
            mod_sum = 0.0
            for j in range(4):  # Four levels of recursion
                mod_sum += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i])
                scale *= 1.5
            fractal_mod += mod_sum
        
        # Nested valley structure with varying curvature and dimension-specific parameters
        valley_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                valley_sum += (x_norm[i]**3 - 0.4 * x_norm[i]**2) * np.exp(-0.4 * x_norm[i]**2)
            else:
                valley_sum += (x_norm[i]**5 - 0.6 * x_norm[i]**4 + 0.3 * x_norm[i]**3) * np.exp(-0.2 * x_norm[i]**2)
        
        # Cross-dimensional coupling with adaptive weights and interaction terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                weight = np.sin(i * np.pi / (self.dim + 2)) * np.cos(j * np.pi / (self.dim + 3))
                coupling = np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                cross_coupling += weight * coupling * (1.0 + 0.1 * np.abs(x_norm[i] - x_norm[j]))
        
        # Exponential conditioning based on dimensionality and harmonic complexity
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Combine components with varying weights for improved benchmark performance
        result = 0.3 * harmonic_sum + 0.25 * rb_sum + 0.1 * fractal_mod + 0.25 * valley_sum + 0.1 * cross_coupling
        
        return result * condition_factor * (1.0 + 0.25 * np.sum(np.abs(x_norm)))