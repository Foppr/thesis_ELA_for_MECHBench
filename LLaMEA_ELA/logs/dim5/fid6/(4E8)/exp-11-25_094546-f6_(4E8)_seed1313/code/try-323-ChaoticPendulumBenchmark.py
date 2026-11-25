import numpy as np

class ChaoticPendulumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Chaotic pendulum-like oscillation with multiple frequencies
            pendulum1 = np.sin(3 * xi) + 0.7 * np.sin(7 * xi) + 0.3 * np.sin(11 * xi)
            pendulum2 = np.cos(4 * xi) + 0.5 * np.cos(9 * xi) + 0.2 * np.cos(13 * xi)
            
            # Asymmetric gradient field with fractal-like behavior
            grad_field = 0.5 * xi**3 - 0.2 * xi**5 + 0.1 * xi**7
            
            # Fractal basin boundary modulation with dimension-dependent scaling
            basin_scale = 1.0 + 0.3 * np.sin(i * 0.8) + 0.2 * np.cos(i * 0.6)
            
            # Cross-dimensional coupling with chaotic interaction terms
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling += (1.0 / (1.0 + distance**3.0)) * np.sin(3 * xi * x_norm[j] + 0.4 * (i - j)**2)
            
            # Asymmetric curvature with chaotic modulation
            curvature = 1.0 + 0.4 * np.sin(self.dim * 0.5 + i * 0.3) + 0.3 * np.cos(self.dim * 0.4 + i * 0.25)
            
            # Fractal basin clustering with periodic modulation
            basin_modulator = 1.0 + 0.5 * np.sin(7 * xi + i * 0.9) * np.cos(4 * xi - i * 0.6)
            
            # Combined function with chaotic dynamics and varying difficulty
            term = basin_scale * curvature * (pendulum1 * pendulum2 + grad_field + 0.7 * coupling) * basin_modulator
            
            result += term**2
            
        # Global scaling with fractal dimension correction
        global_scale = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 2.0) + 0.15 * np.cos(np.log(self.dim + 1) * 3.0)
        return global_scale * result / self.dim