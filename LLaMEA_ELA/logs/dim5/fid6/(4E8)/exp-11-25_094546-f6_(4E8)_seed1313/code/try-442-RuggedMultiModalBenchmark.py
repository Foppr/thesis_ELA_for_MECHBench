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
            
            # Radial basis function with enhanced sinusoidal modulation
            rb_factor = np.exp(-2.0 * xi**2) * (1.0 + 0.6 * np.sin(19 * xi))
            
            # Adaptive frequency modulation with slight shift
            freq = 3.5 + 1.8 * np.sin(i * 0.75) * np.cos(i * 0.45)
            
            # Multi-scale sinusoidal contribution with altered weights
            sin_term = np.sin(freq * xi + i * 0.35) * np.cos(2.7 * xi - i * 0.25) + \
                      0.8 * np.sin(2.3 * freq * xi + i * 0.55) * np.cos(1.9 * xi - i * 0.45) + \
                      0.3 * np.sin(3.5 * freq * xi + i * 0.65)
            
            # Cross-dimensional interaction with modified coupling strength
            cross_term = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling = 0.45 * np.sin(xi + x_norm[j]) * np.cos(xi - x_norm[j])
                    distance = abs(xi - x_norm[j])
                    cross_term += coupling / (1.0 + distance**1.8)
            
            # Modified conditioning factor with different phase
            cond_factor = 1.0 + 0.9 * np.sin(i * 0.95) * np.cos(i * 0.65) + \
                         0.3 * np.sin(i * 1.25) * np.cos(i * 0.85)
            
            # Combined contribution
            term = cond_factor * (rb_factor * sin_term + cross_term)**2
            result += term
            
        # Enhanced global ruggedness modifier
        global_rug = 0.6 * np.sin(np.sum(x_norm**3) * 2.5) * np.cos(np.mean(x_norm**2) * 1.9) + \
                   0.4 * np.sin(np.sum(np.abs(x_norm)) * 3.3) * np.cos(np.mean(np.abs(x_norm)) * 3.1)
        
        # Modified dimension-dependent scaling
        scale = 1.0 + 0.7 * np.sin(self.dim * 0.85) * np.cos(self.dim * 0.55) + \
               0.3 * np.sin(self.dim * 1.25) * np.cos(self.dim * 0.95)
        
        return scale * (result / self.dim + global_rug)