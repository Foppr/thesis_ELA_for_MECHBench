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
            
            # Enhanced fractal basin boundary with increased chaotic scaling
            fractal_factor = 1.0 + 0.5 * np.sin(15 * xi) * np.cos(8 * xi) + 0.3 * np.sin(25 * xi**2)
            
            # Modified time-variant periodic forcing with altered frequency dynamics
            time_freq = 2.8 + 0.7 * np.sin(self.dim * 0.4 + i * 0.15)
            periodic_term = np.sin(time_freq * xi + 0.4 * i) * np.cos(1.9 * xi - 0.3 * i)
            
            # Enhanced non-linear coupling with modified interaction weights
            coupling_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling_factor = 0.25 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**1.8)
            
            # Enhanced chaotic gradient modulation with increased complexity
            chaos_mod = 0.35 * np.sin(19 * xi + 4.0 * i) * np.cos(13 * xi - 3.5 * i) + \
                       0.2 * np.sin(31 * xi**2 + 1.7 * i) * np.cos(21 * xi**2 - 1.1 * i)
            
            # Modified multi-scale interference pattern
            interference = 0.5 * np.sin(6 * xi + 0.8 * i) * np.cos(4 * xi - 0.5 * i) + \
                          0.4 * np.sin(10 * xi + 0.3 * i) * np.cos(7 * xi - 0.2 * i)
            
            # Adjusted dynamic curvature with enhanced fractal behavior
            curvature = 1.0 + 0.6 * np.sin(9 * xi + 0.6 * i) * np.cos(5 * xi - 0.4 * i) + \
                       0.3 * np.sin(14 * xi**2 + 0.7 * i)
            
            # Modified adaptive weighting scheme
            weight = 1.0 + 0.25 * np.sin(i * 0.45) * np.cos(self.dim * 0.25) + \
                    0.2 * np.cos(i * 0.35) * np.sin(self.dim * 0.18)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Modified global chaotic scaling with enhanced multi-fractal correction
        global_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 2) * 2.5) * np.cos(np.log(self.dim + 2) * 2.0) + \
                      0.3 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        
        # Enhanced global coupling term
        global_coupling = 0.2 * np.sin(np.sum(x_norm) * 3.5) * np.cos(np.mean(x_norm) * 2.5)
        
        return global_scale * (result / self.dim + global_coupling)