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
            
            # Primary wave interference pattern with multiple frequencies
            wave1 = np.sin(2 * np.pi * xi) + 0.5 * np.sin(4 * np.pi * xi) + 0.3 * np.sin(8 * np.pi * xi)
            wave2 = np.cos(3 * np.pi * xi) + 0.4 * np.cos(6 * np.pi * xi) + 0.2 * np.cos(9 * np.pi * xi)
            
            # Asymmetric saddle point with varying curvature
            saddle = 0.5 * xi**2 - 0.3 * xi**4 + 0.1 * xi**6
            
            # Adaptive dimension-dependent scaling factor
            scale_factor = 1.0 + 0.2 * np.sin(i * 0.5) + 0.1 * np.cos(i * 0.3)
            
            # Cross-dimensional coupling with asymmetric interaction terms
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling += (1.0 / (1.0 + distance**2.5)) * np.sin(2 * xi * x_norm[j] + 0.5 * (i - j))
            
            # Adaptive curvature with dimension-dependent modulation
            curvature = 1.0 + 0.3 * np.sin(self.dim * 0.4 + i * 0.2) + 0.2 * np.cos(self.dim * 0.3 + i * 0.15)
            
            # Periodic modulation with local minima clustering
            modulator = 1.0 + 0.4 * np.sin(5 * xi + i * 0.7) * np.cos(3 * xi - i * 0.5)
            
            # Combined function with varying difficulty levels
            term = scale_factor * curvature * (wave1 * wave2 + saddle + 0.8 * coupling) * modulator
            
            result += term**2
            
        # Global scaling with adaptive dimensionality correction
        global_scale = 1.0 + 0.15 * np.sin(np.log(self.dim + 1) * 1.5) + 0.1 * np.cos(np.log(self.dim + 1) * 2.3)
        return global_scale * result / self.dim