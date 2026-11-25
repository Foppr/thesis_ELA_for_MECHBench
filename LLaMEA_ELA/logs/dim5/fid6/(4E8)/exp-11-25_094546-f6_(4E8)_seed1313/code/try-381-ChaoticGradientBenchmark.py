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
            
            # Fractal basin boundary with enhanced chaotic scaling
            fractal_factor = 1.0 + 0.4 * np.sin(13 * xi) * np.cos(7 * xi) + 0.25 * np.sin(23 * xi**2)
            
            # Time-variant periodic forcing with modified frequency
            time_freq = 2.5 + 0.6 * np.sin(self.dim * 0.35 + i * 0.12)
            periodic_term = np.sin(time_freq * xi + 0.35 * i) * np.cos(1.7 * xi - 0.25 * i)
            
            # Non-linear coupling with stronger neighboring influence
            coupling_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling_factor = 0.2 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**1.7)
            
            # Chaotic gradient modulation with enhanced complexity
            chaos_mod = 0.3 * np.sin(17 * xi + 3.2 * i) * np.cos(11 * xi - 2.8 * i) + \
                       0.15 * np.sin(29 * xi**2 + 1.4 * i) * np.cos(19 * xi**2 - 0.9 * i)
            
            # Multi-scale interference pattern with altered frequencies
            interference = 0.5 * np.sin(5.5 * xi + 0.75 * i) * np.cos(3.5 * xi - 0.45 * i) + \
                          0.35 * np.sin(9.5 * xi + 0.25 * i) * np.cos(6.5 * xi - 0.15 * i)
            
            # Dynamic curvature with enhanced fractal behavior
            curvature = 1.0 + 0.5 * np.sin(8 * xi + 0.55 * i) * np.cos(4 * xi - 0.35 * i) + \
                       0.25 * np.sin(12 * xi**2 + 0.65 * i)
            
            # Combine all terms with modified weighting
            weight = 1.0 + 0.2 * np.sin(i * 0.42) * np.cos(self.dim * 0.22) + \
                    0.15 * np.cos(i * 0.32) * np.sin(self.dim * 0.17)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Global chaotic scaling with enhanced multi-fractal correction
        global_scale = 1.0 + 0.35 * np.sin(np.log(self.dim + 2) * 2.2) * np.cos(np.log(self.dim + 2) * 1.8) + \
                      0.25 * np.sin(self.dim * 0.55) * np.cos(self.dim * 0.35)
        
        # Add modified global coupling term
        global_coupling = 0.12 * np.sin(np.sum(x_norm) * 3.2) * np.cos(np.mean(x_norm) * 2.2)
        
        return global_scale * (result / self.dim + global_coupling)