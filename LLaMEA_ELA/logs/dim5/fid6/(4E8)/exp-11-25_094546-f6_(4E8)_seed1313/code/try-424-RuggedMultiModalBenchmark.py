import numpy as np

class RuggedMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Radial basis function with sinusoidal modulation
            rb_factor = np.exp(-2.0 * xi**2) * (1.0 + 0.5 * np.sin(17 * xi))
            
            # Adaptive frequency modulation based on dimension
            freq = 3.0 + 2.0 * np.sin(i * 0.7) * np.cos(i * 0.4)
            
            # Multi-scale sinusoidal contribution
            sin_term = np.sin(freq * xi + i * 0.3) * np.cos(2.5 * xi - i * 0.2) + \
                      0.7 * np.sin(2.1 * freq * xi + i * 0.5) * np.cos(1.8 * xi - i * 0.4) + \
                      0.4 * np.sin(3.2 * freq * xi + i * 0.6)
            
            # Cross-dimensional interaction with adaptive coupling
            cross_term = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling = 0.3 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    distance = abs(xi - x_norm[j])
                    cross_term += coupling / (1.0 + distance**1.5)
            
            # Adaptive conditioning factor
            cond_factor = 1.0 + 0.8 * np.sin(i * 0.9) * np.cos(i * 0.6) + \
                         0.4 * np.sin(i * 1.2) * np.cos(i * 0.8)
            
            # Combined contribution
            term = cond_factor * (rb_factor * sin_term + cross_term)**2
            result += term
            
        # Global ruggedness modifier
        global_rug = 0.5 * np.sin(np.sum(x_norm**3) * 2.3) * np.cos(np.mean(x_norm**2) * 1.7) + \
                   0.3 * np.sin(np.sum(np.abs(x_norm)) * 3.1) * np.cos(np.mean(np.abs(x_norm)) * 2.9)
        
        # Dimension-dependent scaling
        scale = 1.0 + 0.6 * np.sin(self.dim * 0.8) * np.cos(self.dim * 0.5) + \
               0.4 * np.sin(self.dim * 1.2) * np.cos(self.dim * 0.9)
        
        return scale * (result / self.dim + global_rug)