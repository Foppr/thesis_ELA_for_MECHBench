import numpy as np

class DynamicHarmonicCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Dynamic harmonic base with fractal-like modulation
            base_freq = 2.0 + 1.5 * np.sin(i * 0.6) * np.cos(i * 0.4)
            harmonic = np.sin(base_freq * xi) + 0.7 * np.sin(3 * base_freq * xi) + 0.3 * np.sin(5 * base_freq * xi)
            
            # Adaptive coupling strength with fractal interference
            coupling_strength = 1.0 + 0.5 * np.sin(i * 0.8) * np.cos(i * 0.6)
            
            # Cross-dimensional interactions with dynamic weights
            cross_term = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    # Fractal interference pattern
                    interference = np.sin(10 * (xi - x_norm[j]) * (i + j + 1)) * \
                                  np.cos(7 * (xi + x_norm[j]) * (i - j + 1))
                    weight = coupling_strength * np.exp(-0.5 * (xi - x_norm[j])**2)
                    cross_term += weight * interference
            
            # Spectral conditioning factor with dynamic phase
            spectral_cond = 1.0 + 0.8 * np.sin(i * 0.7) * np.cos(i * 0.5) + \
                           0.4 * np.sin(2 * i * 0.9) * np.cos(2 * i * 0.6)
            
            # Combined contribution with dynamic scaling
            term = spectral_cond * (harmonic + cross_term)**2
            result += term
            
        # Global fractal interference pattern
        global_pattern = 0.0
        for k in range(1, 6):
            phase = k * np.pi / 5.0
            global_pattern += np.sin(k * np.sum(x_norm**2) + phase) * \
                             np.cos(k * np.mean(np.abs(x_norm)) + phase)
        
        # Adaptive dimension scaling with harmonic progression
        dim_scale = 1.0 + 0.6 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.3) + \
                   0.3 * np.sin(2 * self.dim * 0.7) * np.cos(2 * self.dim * 0.4)
        
        # Final landscape modification with multi-scale harmonic interference
        final_factor = 1.0 + 0.5 * np.sin(np.sum(np.abs(x_norm)) * 3.0) * \
                      np.cos(np.mean(x_norm**2) * 2.0)
        
        return dim_scale * (result / self.dim + 0.3 * global_pattern) * final_factor