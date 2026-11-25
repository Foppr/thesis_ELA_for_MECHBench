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
            
            # Enhanced radial basis function with fractal-like behavior
            rb_factor = np.exp(-2.5 * xi**2) * (1.0 + 0.7 * np.sin(23 * xi) * np.cos(13 * xi))
            
            # Dynamic frequency modulation with chaotic coupling
            freq = 4.0 + 2.2 * np.sin(i * 0.85) * np.cos(i * 0.55) * np.sin(xi * 2.0)
            
            # Multi-scale sinusoidal contribution with fractal interference
            sin_term = np.sin(freq * xi + i * 0.4) * np.cos(3.1 * xi - i * 0.3) + \
                      0.9 * np.sin(2.7 * freq * xi + i * 0.6) * np.cos(2.3 * xi - i * 0.5) + \
                      0.4 * np.sin(4.1 * freq * xi + i * 0.7) * np.cos(1.7 * xi - i * 0.6)
            
            # Cross-dimensional interaction with fractal coupling strength
            cross_term = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling = 0.5 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    distance = abs(xi - x_norm[j])
                    # Fractal distance weighting
                    cross_term += coupling / (1.0 + distance**2.2)
            
            # Adaptive conditioning factor with chaotic modulation
            cond_factor = 1.0 + 1.1 * np.sin(i * 1.1) * np.cos(i * 0.7) + \
                         0.4 * np.sin(i * 1.5) * np.cos(i * 1.0) + \
                         0.2 * np.sin(i * 2.3) * np.cos(i * 1.8)
            
            # Combined contribution with enhanced nonlinearity
            term = cond_factor * (rb_factor * sin_term + cross_term)**2
            result += term
            
        # Enhanced global ruggedness with fractal interference patterns
        global_rug = 0.7 * np.sin(np.sum(x_norm**3) * 3.0) * np.cos(np.mean(x_norm**2) * 2.1) + \
                   0.5 * np.sin(np.sum(np.abs(x_norm)) * 3.8) * np.cos(np.mean(np.abs(x_norm)) * 3.5) + \
                   0.3 * np.sin(np.sum(x_norm**4) * 2.7) * np.cos(np.mean(x_norm**3) * 1.8)
        
        # Fractal dimension-dependent scaling
        scale = 1.0 + 0.8 * np.sin(self.dim * 0.95) * np.cos(self.dim * 0.65) + \
               0.4 * np.sin(self.dim * 1.35) * np.cos(self.dim * 1.05) + \
               0.2 * np.sin(self.dim * 2.1) * np.cos(self.dim * 1.5)
        
        return scale * (result / self.dim + global_rug)