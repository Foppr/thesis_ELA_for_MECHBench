import numpy as np

class AdaptivePolynomialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Adaptive polynomial potential with dynamic exponent
            poly_exp = 2.0 + 1.5 * np.sin(self.dim * 0.8 + i * 0.6)
            poly_term = np.abs(xi)**poly_exp
            
            # Dynamic harmonic coupling with time-variant frequencies
            harmonic_coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    freq = 1.0 + 0.5 * np.sin(i * 0.4 + j * 0.3 + self.dim * 0.2)
                    coupling = np.sin(freq * (xi - x_norm[j]) + i * 0.5) * np.cos(freq * (xi - x_norm[j]) + j * 0.3)
                    harmonic_coupling += coupling * (1.0 / (1.0 + abs(xi - x_norm[j])**3.0))
            
            # Time-variant conditioning factor with chaotic modulation
            condition_factor = 1.0 + 0.8 * np.sin(self.dim * 0.7 + i * 0.5) * np.cos(xi * 4.0 + self.dim * 0.3)
            
            # Nested basin structure with multi-scale harmonic interference
            basin_structure = 0.0
            for k in range(1, 8):
                scale = 1.0 / (k**1.5)
                freq = k * (1.0 + 0.3 * np.sin(i * 0.6 + k * 0.4))
                phase = k * 0.8 + 0.2 * np.cos(i * 0.5 + k * 0.3)
                basin_structure += scale * np.sin(freq * xi + phase) * np.cos(freq * xi + phase * 0.7)
            
            # Adaptive gradient modulation with multi-fractal scaling
            grad_mod = 1.0 + 0.4 * np.sin(6 * xi + i * 0.4) * np.cos(4 * xi + i * 0.3) * np.sin(2 * xi + i * 0.2)
            
            # Add all components together with adaptive scaling
            result += condition_factor * (poly_term + harmonic_coupling + basin_structure) * grad_mod
            
        # Global time-variant scaling with dimension-dependent correction
        global_scale = 1.0 + 0.6 * np.sin(np.log(self.dim + 2) * 1.8) * np.cos(self.dim * 0.4)
        
        # Add chaotic noise for additional complexity
        noise = 0.03 * np.sum(np.sin(x_norm * 8.0 + self.dim * 0.15))
        
        return (global_scale * result / self.dim) + noise