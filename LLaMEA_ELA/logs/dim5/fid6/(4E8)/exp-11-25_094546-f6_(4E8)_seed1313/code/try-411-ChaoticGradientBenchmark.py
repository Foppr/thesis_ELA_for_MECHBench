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
            
            # Enhanced multi-fractal basin boundary with increased chaotic scaling
            fractal_factor = 1.0 + 0.8 * np.sin(29 * xi) * np.cos(13 * xi) + 0.5 * np.sin(41 * xi**2) + 0.3 * np.sin(47 * xi**3)
            
            # Modified time-variant periodic forcing with altered frequency dynamics
            time_freq = 5.0 + 1.5 * np.sin(self.dim * 0.65 + i * 0.28)
            periodic_term = np.sin(time_freq * xi + 0.6 * i) * np.cos(2.7 * xi - 0.45 * i)
            
            # Enhanced non-linear coupling with modified interaction weights
            coupling_sum = 0.0
            for j in range(max(0, i-5), min(self.dim, i+6)):
                if i != j:
                    coupling_factor = 0.5 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**2.5)
            
            # Enhanced chaotic gradient modulation with increased complexity
            chaos_mod = 0.6 * np.sin(31 * xi + 5.5 * i) * np.cos(21 * xi - 5.1 * i) + \
                       0.3 * np.sin(47 * xi**2 + 3.1 * i) * np.cos(33 * xi**2 - 1.9 * i) + \
                       0.2 * np.sin(53 * xi**3 + 2.7 * i)
            
            # Modified multi-scale interference pattern
            interference = 0.7 * np.sin(11 * xi + 1.3 * i) * np.cos(6 * xi - 0.7 * i) + \
                          0.5 * np.sin(15 * xi + 0.5 * i) * np.cos(12 * xi - 0.35 * i) + \
                          0.35 * np.sin(19 * xi + 0.25 * i)
            
            # Adjusted dynamic curvature with enhanced fractal behavior
            curvature = 1.0 + 0.8 * np.sin(14 * xi + 0.9 * i) * np.cos(7 * xi - 0.55 * i) + \
                       0.5 * np.sin(21 * xi**2 + 1.0 * i) + 0.3 * np.sin(31 * xi**3 + 0.8 * i)
            
            # Modified adaptive weighting scheme
            weight = 1.0 + 0.4 * np.sin(i * 0.68) * np.cos(self.dim * 0.48) + \
                    0.3 * np.cos(i * 0.58) * np.sin(self.dim * 0.42) + \
                    0.25 * np.sin(i * 0.54) * np.cos(self.dim * 0.44)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Modified global chaotic scaling with enhanced multi-fractal correction
        global_scale = 1.0 + 0.7 * np.sin(np.log(self.dim + 5) * 3.5) * np.cos(np.log(self.dim + 5) * 3.1) + \
                      0.5 * np.sin(self.dim * 0.85) * np.cos(self.dim * 0.55) + \
                      0.35 * np.sin(self.dim * 1.0) * np.cos(self.dim * 0.75)
        
        # Enhanced global coupling term
        global_coupling = 0.3 * np.sin(np.sum(x_norm) * 5.2) * np.cos(np.mean(x_norm) * 4.1) + \
                         0.25 * np.sin(np.sum(x_norm**2) * 3.5) * np.cos(np.mean(x_norm**2) * 2.7)
        
        return global_scale * (result / self.dim + global_coupling)