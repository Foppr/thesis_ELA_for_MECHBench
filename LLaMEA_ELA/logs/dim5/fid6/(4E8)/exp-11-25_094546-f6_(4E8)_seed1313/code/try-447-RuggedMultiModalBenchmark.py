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
            
            # Enhanced radial basis function with fractal-like properties
            rb_factor = np.exp(-2.5 * xi**2) * (1.0 + 0.7 * np.sin(23 * xi) * np.cos(13 * xi))
            
            # Dynamic frequency modulation with chaotic coupling
            freq = 4.0 + 2.2 * np.sin(i * 0.85 + np.sin(i * 0.3)) * np.cos(i * 0.5 + np.cos(i * 0.4))
            
            # Multi-scale sinusoidal contribution with fractal interference
            sin_term = np.sin(freq * xi + i * 0.4) * np.cos(3.1 * xi - i * 0.3) + \
                      0.9 * np.sin(2.7 * freq * xi + i * 0.5) * np.cos(2.3 * xi - i * 0.4) + \
                      0.4 * np.sin(4.1 * freq * xi + i * 0.6) * np.cos(1.7 * xi - i * 0.5) + \
                      0.2 * np.sin(5.3 * freq * xi + i * 0.7)
            
            # Enhanced cross-dimensional interaction with fractal coupling
            cross_term = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling = 0.5 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j]) * \
                              np.exp(-0.5 * (xi - x_norm[j])**2)
                    distance = abs(xi - x_norm[j])
                    cross_term += coupling / (1.0 + distance**2.2)
            
            # Adaptive conditioning factor with chaotic phase modulation
            cond_factor = 1.0 + 1.1 * np.sin(i * 1.1 + np.sin(i * 0.6)) * np.cos(i * 0.7 + np.cos(i * 0.5)) + \
                         0.4 * np.sin(i * 1.5 + np.sin(i * 0.8)) * np.cos(i * 1.0 + np.cos(i * 0.9))
            
            # Combined contribution with enhanced nonlinearity
            term = cond_factor * (rb_factor * sin_term + cross_term)**2.3
            result += term
            
        # Fractal global ruggedness modifier
        global_rug = 0.7 * np.sin(np.sum(x_norm**4) * 3.0) * np.cos(np.mean(x_norm**3) * 2.2) + \
                   0.5 * np.sin(np.sum(np.abs(x_norm)**1.5) * 4.0) * np.cos(np.mean(np.abs(x_norm)**1.7) * 3.5) + \
                   0.3 * np.sin(np.sum(x_norm**2.5) * 2.5)
        
        # Enhanced dimension-dependent scaling with fractal properties
        scale = 1.0 + 0.8 * np.sin(self.dim * 0.95 + np.sin(self.dim * 0.4)) * np.cos(self.dim * 0.65 + np.cos(self.dim * 0.3)) + \
               0.4 * np.sin(self.dim * 1.35 + np.sin(self.dim * 0.7)) * np.cos(self.dim * 1.15 + np.cos(self.dim * 0.8))
        
        return scale * (result / self.dim + global_rug)