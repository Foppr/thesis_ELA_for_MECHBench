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
            fractal_factor = 1.0 + 0.6 * np.sin(17 * xi) * np.cos(9 * xi) + 0.35 * np.sin(29 * xi**2) + \
                            0.2 * np.sin(37 * xi**3)
            
            # Modified time-variant periodic forcing with altered frequency dynamics
            time_freq = 3.5 + 0.9 * np.sin(self.dim * 0.48 + i * 0.21)
            periodic_term = np.sin(time_freq * xi + 0.5 * i) * np.cos(2.3 * xi - 0.38 * i)
            
            # Enhanced non-linear coupling with modified interaction weights
            coupling_sum = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling_factor = 0.3 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**2.2)
            
            # Enhanced chaotic gradient modulation with increased complexity
            chaos_mod = 0.45 * np.sin(23 * xi + 4.5 * i) * np.cos(15 * xi - 4.0 * i) + \
                       0.25 * np.sin(37 * xi**2 + 2.3 * i) * np.cos(25 * xi**2 - 1.4 * i) + \
                       0.15 * np.sin(41 * xi**3 + 2.0 * i)
            
            # Modified multi-scale interference pattern
            interference = 0.55 * np.sin(7 * xi + 0.9 * i) * np.cos(5 * xi - 0.6 * i) + \
                          0.45 * np.sin(11 * xi + 0.4 * i) * np.cos(8 * xi - 0.3 * i) + \
                          0.3 * np.sin(15 * xi**2 + 0.5 * i)
            
            # Adjusted dynamic curvature with enhanced fractal behavior
            curvature = 1.0 + 0.65 * np.sin(10 * xi + 0.7 * i) * np.cos(5 * xi - 0.5 * i) + \
                       0.35 * np.sin(15 * xi**2 + 0.8 * i) + 0.25 * np.sin(20 * xi**3 + 0.55 * i)
            
            # Modified adaptive weighting scheme with enhanced complexity
            weight = 1.0 + 0.35 * np.sin(i * 0.55) * np.cos(self.dim * 0.3) + \
                    0.25 * np.cos(i * 0.45) * np.sin(self.dim * 0.25) + \
                    0.2 * np.sin(i * 0.4) * np.cos(self.dim * 0.2)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Modified global chaotic scaling with enhanced multi-fractal correction
        global_scale = 1.0 + 0.55 * np.sin(np.log(self.dim + 3) * 2.9) * np.cos(np.log(self.dim + 3) * 2.5) + \
                      0.4 * np.sin(self.dim * 0.68) * np.cos(self.dim * 0.48) + \
                      0.25 * np.sin(self.dim * 0.78) * np.cos(self.dim * 0.32)
        
        # Enhanced global coupling term with additional resonance effects
        global_coupling = 0.25 * np.sin(np.sum(x_norm) * 4.3) * np.cos(np.mean(x_norm) * 3.3) + \
                         0.2 * np.sin(np.std(x_norm) * 2.9) * np.cos(np.var(x_norm) * 2.1)
        
        return global_scale * (result / self.dim + global_coupling)