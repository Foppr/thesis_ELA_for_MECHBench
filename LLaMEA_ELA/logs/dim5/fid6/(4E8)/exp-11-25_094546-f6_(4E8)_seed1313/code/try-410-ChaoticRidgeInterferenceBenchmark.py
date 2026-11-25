import numpy as np

class ChaoticRidgeInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Chaotic phase modulation with dimension-dependent frequency
            phase = np.sin(xi * 7.0 + self.dim * 0.8 + i * 0.3) * np.cos(xi * 5.0 + self.dim * 0.6 + i * 0.4)
            
            # Adaptive ridge structure with chaotic curvature
            ridge_height = 0.5 * xi**2 + 0.3 * np.sin(3 * xi + i * 0.5) * np.cos(2 * xi + i * 0.3)
            
            # Multi-scale harmonic interference with dynamic amplitudes
            interference = 0.0
            for k in range(1, 6):
                freq = k * (1.5 + 0.5 * np.sin(i * 0.7 + self.dim * 0.4))
                amp = 0.6 / (k**1.2) * (1.0 + 0.2 * np.sin(i * 0.8 + k * 0.3))
                interference += amp * np.sin(freq * xi + k * 0.4 + phase)
            
            # Cross-dimensional gradient coupling with exponential interaction
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    diff = xi - x_norm[j]
                    coupling += np.exp(-0.5 * diff**2) * np.sin(3 * xi + 2 * x_norm[j] + i * 0.2 + j * 0.1)
            
            # Adaptive conditioning with chaotic modulation
            condition = 1.0 + 0.5 * np.sin(self.dim * 0.9 + i * 0.6) * np.cos(xi * 4.0 + i * 0.3)
            
            # Fractal-like ridge scaling with dimension interaction
            scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5 + i * 0.7) * np.cos(xi * 2.0)
            
            # Add all components together
            result += condition * (ridge_height + interference + coupling) * scale_factor
            
        # Global chaotic scaling with multi-dimensional modulation
        global_mod = 1.0 + 0.4 * np.sin(np.log(self.dim + 1) * 2.0) * np.cos(self.dim * 0.8)
        
        # Add noise component for additional challenge
        noise = 0.1 * np.sum(np.sin(x_norm * 13.0 + np.arange(self.dim) * 0.5))
        
        return global_mod * result / self.dim + noise