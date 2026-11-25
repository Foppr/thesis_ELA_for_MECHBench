import numpy as np

class RadialChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis centers and widths for stability
        np.random.seed(42)
        self.centers = np.random.uniform(-1, 1, (15, dim)) * 5.0
        self.widths = np.random.uniform(0.5, 2.0, 15)
        
    def f(self, x):
        x_norm = x / 5.0
        # Radial basis function component with adaptive widths
        rb_value = 0.0
        for i in range(len(self.centers)):
            center = self.centers[i] / 5.0
            diff = x_norm - center
            distance_sq = np.sum(diff**2)
            rb_value += np.exp(-self.widths[i] * distance_sq) * np.cos(3.0 * distance_sq)
        
        # Chaotic sine coupling between dimensions with varying frequencies
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2.0 + 0.5 * np.sin(i * 0.7)
                freq_j = 2.0 + 0.5 * np.cos(j * 0.7)
                coupling_term += np.sin(x_norm[i] * freq_i) * np.cos(x_norm[j] * freq_j) * \
                                np.sin((x_norm[i] + x_norm[j]) * 3.0)
        
        # Adaptive conditioning based on position
        condition_factor = 1.0 + 0.3 * np.sum(np.abs(x_norm)) + 0.2 * np.sum(x_norm**2)
        
        # Fractal-like self-similarity with multiple scales
        fractal_term = 0.0
        scales = [1.0, 2.5, 4.0, 6.0]
        for scale in scales:
            fractal_term += np.sin(x_norm[0] * scale) * np.cos(x_norm[1] * scale) * \
                           np.sin(np.sum(x_norm**2) * 0.5 * scale)
        
        # Global chaotic modulation
        chaos_mod = 1.0 + 0.25 * np.sin(np.sum(x_norm**3)) * np.cos(np.sum(x_norm**4))
        
        # Combine all components with dynamic weights
        result = 0.4 * rb_value + 0.3 * coupling_term + 0.2 * fractal_term
        
        return result * chaos_mod * condition_factor