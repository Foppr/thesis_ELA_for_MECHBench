import numpy as np

class WaveInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Primary wave interference term with periodicity and amplitude modulation
            wave_term = np.sin(3 * xi) * np.cos(5 * xi) + 0.5 * np.sin(7 * xi) * np.cos(2 * xi)
            
            # Asymmetric saddle point contribution with directional bias
            saddle_term = 0.3 * xi**3 - 0.4 * xi**2 + 0.1 * xi
            
            # Adaptive curvature term that changes with dimensionality
            curvature = 1.0 + 0.5 * np.sin(self.dim * 0.2 + i * 0.3) * np.cos(self.dim * 0.15 + i * 0.25)
            
            # Cross-dimensional interaction with asymmetric coupling
            cross_term = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling = 1.0 / (1.0 + distance**2.5)
                    cross_term += coupling * np.sin(xi + x_norm[j] + 0.2 * np.sin(i * j))
            
            # Periodic modulation with dimension-dependent frequency
            mod_freq = 1.0 + 0.3 * np.sin(self.dim * 0.4 + i * 0.2)
            periodic_mod = np.sin(mod_freq * xi + 0.5 * i) * np.cos(mod_freq * xi - 0.3 * i)
            
            # Nonlinear scaling with dimension-dependent factor
            dim_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3) * np.cos(self.dim * 0.2)
            
            # Add all components together with appropriate weights
            result += (curvature * (wave_term + saddle_term + cross_term + periodic_mod)**2) * dim_factor
            
        # Global scaling factor that increases with dimension for added difficulty
        global_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        return global_scale * result / self.dim