import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal ridge structure with self-similar curvature
            ridge = np.sin(xi * 10.0) * np.exp(-0.5 * xi**2)
            
            # Adaptive curvature field that changes with dimension
            curvature = 1.0 + 0.5 * np.sin(self.dim * 0.5 + i * 0.3) * np.cos(xi * 2.0)
            
            # Cross-dimensional coupling with fractal interference
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    coupling += (1.0 / (1.0 + distance**3)) * np.sin(xi * x_norm[j] * 5.0 + i * j * 0.1)
            
            # Multi-scale fractal pattern with varying frequencies
            fractal = 0.0
            for k in range(1, 6):
                fractal += (1.0 / k**1.5) * np.sin(xi * k**2.0 + k * i * 0.2)
            
            # Combined components with dimension-dependent weighting
            weight = 1.0 + 0.3 * np.cos(self.dim * 0.4 + i * 0.1)
            result += weight * (curvature * ridge + coupling + 0.7 * fractal)**2
            
        # Global scaling factor with fractal dimension correction
        fractal_correction = 1.0 + 0.1 * np.sin(np.log(self.dim + 1) * 2.0)
        return fractal_correction * result / self.dim