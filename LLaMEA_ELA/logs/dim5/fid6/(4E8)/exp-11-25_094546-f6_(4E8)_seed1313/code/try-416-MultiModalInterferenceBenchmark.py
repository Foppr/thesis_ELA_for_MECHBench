import numpy as np

class MultiModalInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced multi-fractal basin boundary with increased chaotic scaling
            fractal_factor = 1.0 + 0.8 * np.sin(23 * xi) * np.cos(11 * xi) + 0.5 * np.sin(37 * xi**2) + \
                            0.4 * np.sin(41 * xi**3) + 0.3 * np.sin(19 * xi**4)
            
            # Modified time-variant periodic forcing with altered frequency dynamics
            time_freq = 4.2 + 1.1 * np.sin(self.dim * 0.52 + i * 0.25)
            periodic_term = np.sin(time_freq * xi + 0.6 * i) * np.cos(2.7 * xi - 0.42 * i)
            
            # Enhanced non-linear coupling with modified interaction weights
            coupling_sum = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    coupling_factor = 0.4 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**2.5)
            
            # Enhanced chaotic gradient modulation with increased complexity
            chaos_mod = 0.5 * np.sin(29 * xi + 5.2 * i) * np.cos(19 * xi - 4.8 * i) + \
                       0.3 * np.sin(43 * xi**2 + 2.7 * i) * np.cos(31 * xi**2 - 1.7 * i) + \
                       0.2 * np.sin(47 * xi**3 + 2.4 * i) + 0.15 * np.sin(53 * xi**4 + 2.1 * i)
            
            # Modified multi-scale interference pattern
            interference = 0.6 * np.sin(9 * xi + 1.1 * i) * np.cos(7 * xi - 0.7 * i) + \
                          0.5 * np.sin(13 * xi + 0.5 * i) * np.cos(10 * xi - 0.4 * i) + \
                          0.4 * np.sin(17 * xi**2 + 0.6 * i) + 0.3 * np.sin(23 * xi**3 + 0.5 * i)
            
            # Adjusted dynamic curvature with enhanced fractal behavior
            curvature = 1.0 + 0.7 * np.sin(12 * xi + 0.8 * i) * np.cos(6 * xi - 0.6 * i) + \
                       0.4 * np.sin(18 * xi**2 + 0.9 * i) + 0.3 * np.sin(24 * xi**3 + 0.65 * i) + \
                       0.2 * np.sin(30 * xi**4 + 0.5 * i)
            
            # Modified adaptive weighting scheme with enhanced complexity
            weight = 1.0 + 0.4 * np.sin(i * 0.6) * np.cos(self.dim * 0.35) + \
                    0.3 * np.cos(i * 0.5) * np.sin(self.dim * 0.3) + \
                    0.25 * np.sin(i * 0.45) * np.cos(self.dim * 0.25) + \
                    0.2 * np.cos(i * 0.4) * np.sin(self.dim * 0.2)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Modified global chaotic scaling with enhanced multi-fractal correction
        global_scale = 1.0 + 0.6 * np.sin(np.log(self.dim + 4) * 3.1) * np.cos(np.log(self.dim + 4) * 2.7) + \
                      0.45 * np.sin(self.dim * 0.72) * np.cos(self.dim * 0.52) + \
                      0.3 * np.sin(self.dim * 0.82) * np.cos(self.dim * 0.36) + \
                      0.2 * np.sin(self.dim * 0.92) * np.cos(self.dim * 0.28)
        
        # Enhanced global coupling term with additional resonance effects
        global_coupling = 0.3 * np.sin(np.sum(x_norm) * 5.1) * np.cos(np.mean(x_norm) * 3.7) + \
                         0.25 * np.sin(np.std(x_norm) * 3.3) * np.cos(np.var(x_norm) * 2.5) + \
                         0.2 * np.sin(np.max(x_norm) * 4.0) * np.cos(np.min(x_norm) * 3.0)
        
        return global_scale * (result / self.dim + global_coupling)