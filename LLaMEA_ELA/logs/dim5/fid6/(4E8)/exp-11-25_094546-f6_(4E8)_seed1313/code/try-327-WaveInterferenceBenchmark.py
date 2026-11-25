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
            
            # Enhanced wave interference with fractal-like frequency progression
            wave1 = np.sin(2 * np.pi * xi) + 0.5 * np.sin(6 * np.pi * xi) + 0.3 * np.sin(18 * np.pi * xi) + 0.1 * np.sin(54 * np.pi * xi)
            wave2 = np.cos(3 * np.pi * xi) + 0.4 * np.cos(9 * np.pi * xi) + 0.2 * np.cos(27 * np.pi * xi) + 0.05 * np.cos(81 * np.pi * xi)
            
            # Enhanced asymmetric saddle point with higher-order terms
            saddle = 0.5 * xi**2 - 0.3 * xi**4 + 0.1 * xi**6 - 0.02 * xi**8
            
            # Improved dimension-dependent scaling with fractal characteristics
            scale_factor = 1.0 + 0.3 * np.sin(i * 0.7) + 0.15 * np.cos(i * 0.4) + 0.05 * np.sin(i * 2.0)
            
            # Stronger cross-dimensional coupling with fractal interaction patterns
            coupling = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Fractal coupling strength with power-law decay
                    coupling_strength = 1.0 / (1.0 + distance**3.0)
                    coupling += coupling_strength * np.sin(3 * xi * x_norm[j] + 0.7 * (i - j) + 0.3 * np.sin(i + j))
            
            # Enhanced adaptive curvature with multi-scale modulation
            curvature = 1.0 + 0.4 * np.sin(self.dim * 0.5 + i * 0.25) + 0.25 * np.cos(self.dim * 0.35 + i * 0.2) + 0.1 * np.sin(self.dim * 0.8 + i * 0.15)
            
            # Advanced periodic modulation with multi-fractal characteristics
            modulator = 1.0 + 0.5 * np.sin(7 * xi + i * 0.9) * np.cos(4 * xi - i * 0.6) + 0.2 * np.sin(13 * xi + i * 0.4)
            
            # Combined function with enhanced difficulty and conditioning
            term = scale_factor * curvature * (wave1 * wave2 + saddle + coupling) * modulator
            
            result += term**2
            
        # Improved global scaling with enhanced dimensionality correction
        global_scale = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 2.0) + 0.15 * np.cos(np.log(self.dim + 1) * 3.0) + 0.08 * np.sin(np.log(self.dim + 1) * 5.0)
        return global_scale * result / self.dim