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
            
            # Enhanced fractal basin boundary with increased chaotic scaling and multi-frequency modulation
            fractal_factor = 1.0 + 0.6 * np.sin(17 * xi) * np.cos(9 * xi) + \
                            0.35 * np.sin(29 * xi**2) * np.cos(13 * xi) + \
                            0.2 * np.sin(37 * xi**3) * np.cos(23 * xi)
            
            # Modified time-variant periodic forcing with altered frequency dynamics and phase coupling
            time_freq = 3.0 + 0.8 * np.sin(self.dim * 0.45 + i * 0.18)
            periodic_term = np.sin(time_freq * xi + 0.4 * i) * np.cos(2.1 * xi - 0.3 * i) + \
                           0.3 * np.sin(1.7 * xi + 0.25 * i) * np.cos(1.3 * xi - 0.18 * i)
            
            # Enhanced non-linear coupling with modified interaction weights and cross-dimensional resonance
            coupling_sum = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling_factor = 0.25 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j]) + \
                                    0.15 * np.sin(2 * xi + 3 * x_norm[j]) * np.cos(3 * xi - 2 * x_norm[j])
                    coupling_sum += coupling_factor / (1.0 + abs(xi - x_norm[j])**2.1)
            
            # Enhanced chaotic gradient modulation with increased complexity and multi-scale resonance
            chaos_mod = 0.4 * np.sin(21 * xi + 4.2 * i) * np.cos(15 * xi - 3.8 * i) + \
                       0.2 * np.sin(33 * xi**2 + 2.1 * i) * np.cos(25 * xi**2 - 1.3 * i) + \
                       0.15 * np.sin(41 * xi**3 + 1.7 * i) * np.cos(31 * xi**3 - 0.8 * i)
            
            # Modified multi-scale interference pattern with enhanced cross-dimensional coupling
            interference = 0.5 * np.sin(6 * xi + 0.8 * i) * np.cos(4 * xi - 0.5 * i) + \
                          0.4 * np.sin(11 * xi + 0.3 * i) * np.cos(7 * xi - 0.2 * i) + \
                          0.25 * np.sin(15 * xi + 0.1 * i) * np.cos(9 * xi - 0.05 * i)
            
            # Adjusted dynamic curvature with enhanced fractal behavior and multi-scale modulation
            curvature = 1.0 + 0.6 * np.sin(10 * xi + 0.6 * i) * np.cos(5 * xi - 0.4 * i) + \
                       0.3 * np.sin(15 * xi**2 + 0.7 * i) * np.cos(8 * xi**2 - 0.5 * i) + \
                       0.2 * np.sin(20 * xi**3 + 0.3 * i)
            
            # Modified adaptive weighting scheme with enhanced multi-dimensional resonance
            weight = 1.0 + 0.3 * np.sin(i * 0.5) * np.cos(self.dim * 0.28) + \
                    0.2 * np.cos(i * 0.4) * np.sin(self.dim * 0.2) + \
                    0.15 * np.sin(2 * i * 0.3) * np.cos(2 * self.dim * 0.15)
            
            # Final contribution for this dimension
            term = weight * (curvature * xi**2 + periodic_term + coupling_sum + chaos_mod + interference)**2
            result += fractal_factor * term
            
        # Modified global chaotic scaling with enhanced multi-fractal correction and resonance
        global_scale = 1.0 + 0.45 * np.sin(np.log(self.dim + 3) * 2.8) * np.cos(np.log(self.dim + 3) * 2.2) + \
                      0.35 * np.sin(self.dim * 0.65) * np.cos(self.dim * 0.45) + \
                      0.25 * np.sin(2 * self.dim * 0.3) * np.cos(3 * self.dim * 0.2)
        
        # Enhanced global coupling term with multi-scale resonance and fractal interference
        global_coupling = 0.2 * np.sin(np.sum(x_norm) * 4.1) * np.cos(np.mean(x_norm) * 2.8) + \
                         0.15 * np.sin(np.sum(x_norm**2) * 3.7) * np.cos(np.mean(x_norm**2) * 2.4)
        
        return global_scale * (result / self.dim + global_coupling)