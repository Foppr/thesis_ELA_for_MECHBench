import numpy as np

class NestedHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-scale harmonic oscillations with nested frequencies
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq_scale = 2**(i % 4)
            base_freq = 1.0 + 3.0 * np.sin(i * np.pi / (self.dim + 1))
            harmonic_sum += np.sin(freq_scale * base_freq * x_norm[i]) * np.cos(freq_scale * base_freq * x_norm[i])
        
        # Adaptive radial basis functions with dynamic bandwidths
        rb_sum = 0.0
        for i in range(min(8, self.dim)):
            center = np.sin(i * np.pi / (self.dim + 2)) * np.cos(i * np.pi / (self.dim + 3))
            # Dynamic bandwidth based on dimension index
            bandwidth = 0.1 + 0.4 * (i % 3) / 2.0
            rb_sum += np.exp(-0.5 * np.sum((x_norm - center)**2) / (bandwidth**2)) * np.sin(i * x_norm[i])
        
        # Fractal-like gradient modulation with recursive scaling
        fractal_mod = 0.0
        for i in range(self.dim):
            scale = 1.0
            mod_sum = 0.0
            for j in range(3):  # Three levels of recursion
                mod_sum += np.sin(scale * x_norm[i]) * np.cos(scale * x_norm[i])
                scale *= 2.0
            fractal_mod += mod_sum
        
        # Nested valley structure with varying curvature
        valley_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                valley_sum += (x_norm[i]**3 - 0.5 * x_norm[i]**2) * np.exp(-0.5 * x_norm[i]**2)
            else:
                valley_sum += (x_norm[i]**4 - 0.7 * x_norm[i]**3 + 0.2 * x_norm[i]**2) * np.exp(-0.3 * x_norm[i]**2)
        
        # Cross-dimensional coupling with harmonic weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                weight = np.sin(i * np.pi / (self.dim + 1)) * np.cos(j * np.pi / (self.dim + 2))
                coupling = np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                cross_coupling += weight * coupling
        
        # Exponential conditioning based on dimensionality
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine components with varying weights
        result = 0.25 * harmonic_sum + 0.3 * rb_sum + 0.15 * fractal_mod + 0.2 * valley_sum + 0.1 * cross_coupling
        
        return result * condition_factor * (1.0 + 0.3 * np.sum(np.abs(x_norm)))