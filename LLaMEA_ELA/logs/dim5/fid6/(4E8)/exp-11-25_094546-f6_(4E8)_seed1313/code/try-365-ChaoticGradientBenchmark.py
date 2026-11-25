import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal basin boundary with chaotic scaling
            fractal_factor = 1.0 + 0.3 * np.sin(13 * xi) * np.cos(7 * xi) + 0.2 * np.sin(23 * xi**2)
            
            # Time-variant periodic forcing with dynamic frequency
            time_freq = 2.0 + 0.5 * np.sin(self.dim * 0.3 + i * 0.1)
            periodic_term = np.sin(time_freq * xi + 0.3 * i) * np.cos(1.5 * xi - 0.2 * i)
            
            # Non-linear coupling with neighboring dimensions
            coupling_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling_factor = 0.15 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**1.5)
            
            # Chaotic gradient modulation with dimension-dependent chaos
            chaos_mod = 0.25 * np.sin(17 * xi + 3.1 * i) * np.cos(11 * xi - 2.7 * i) + \
                       0.1 * np.sin(29 * xi**2 + 1.3 * i) * np.cos(19 * xi**2 - 0.8 * i)
            
            # Multi-scale interference pattern
            interference = 0.4 * np.sin(5 * xi + 0.7 * i) * np.cos(3 * xi - 0.4 * i) + \
                          0.3 * np.sin(9 * xi + 0.2 * i) * np.cos(6 * xi - 0.1 * i)
            
            # Dynamic curvature with fractal-like behavior
            curvature = 1.0 + 0.4 * np.sin(8 * xi + 0.5 * i) * np.cos(4 * xi - 0.3 * i) + \
                       0.2 * np.sin(12 * xi**2 + 0.6 * i)
            
            # Combine all terms with adaptive weighting
            weight = 1.0 + 0.15 * np.sin(i * 0.4) * np.cos(self.dim * 0.2) + \
                    0.1 * np.cos(i * 0.3) * np.sin(self.dim * 0.15)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Global chaotic scaling with multi-fractal correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 2) * 2.1) * np.cos(np.log(self.dim + 2) * 1.7) + \
                      0.2 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.3)
        
        # Add global coupling term
        global_coupling = 0.1 * np.sin(np.sum(x_norm) * 3.0) * np.cos(np.mean(x_norm) * 2.0)
        
        return global_scale * (result / self.dim + global_coupling)