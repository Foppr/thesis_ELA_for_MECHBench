import numpy as np

class PolynomialRBFChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Polynomial chaos component with dynamic exponents
            poly_chaos = 0.0
            for k in range(1, 6):
                exponent = 2 + 0.3 * np.sin(i * 0.7 + k * 0.5)
                poly_chaos += (0.2 * k) * xi**exponent
            
            # Radial basis function component with adaptive width
            rbf_sum = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    dist = abs(xi - x_norm[j])
                    width = 0.5 + 0.3 * np.sin(i * 0.4 + j * 0.3)
                    rbf_sum += np.exp(-dist**2 / (2 * width**2))
            
            # Dynamic coupling with time-varying weights
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    weight = 0.4 + 0.2 * np.sin(i * 0.6 + j * 0.5 + self.dim * 0.3)
                    coupling += weight * (xi - x_norm[j])**2
            
            # Multi-scale sinusoidal modulation
            mod_freq = 1.0 + 0.8 * np.sin(i * 0.5)
            modulation = np.sin(mod_freq * xi) * np.cos(2 * mod_freq * xi) + \
                        0.5 * np.sin(3 * mod_freq * xi) * np.cos(4 * mod_freq * xi)
            
            # Adaptive conditioning factor
            cond_factor = 1.0 + 0.5 * np.sin(i * 0.8 + self.dim * 0.4)
            
            # Combine components with dynamic weights
            weight_i = 0.3 + 0.2 * np.sin(i * 0.6) + 0.1 * np.cos(i * 0.4)
            result += weight_i * cond_factor * (poly_chaos + rbf_sum + coupling + modulation)**2
        
        # Global scaling with multi-fractal behavior
        global_scale = 1.0 + 0.4 * np.sin(self.dim * 0.3) * np.cos(self.dim * 0.2) + \
                      0.3 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.4) + \
                      0.2 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.6)
        
        # Additional global interference term
        global_interference = 0.15 * np.sin(np.sum(x_norm)**2) * np.cos(np.mean(x_norm)**2) + \
                            0.1 * np.sin(np.std(x_norm)) * np.cos(np.var(x_norm))
        
        return global_scale * (result / self.dim + global_interference)