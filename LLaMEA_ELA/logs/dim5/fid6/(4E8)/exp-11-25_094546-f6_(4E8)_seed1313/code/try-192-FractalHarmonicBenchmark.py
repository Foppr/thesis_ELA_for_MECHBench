import numpy as np

class FractalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Fractal harmonic potential with self-similar structure
            harmonic = np.sin(xi) + 0.5 * np.sin(3 * xi) + 0.1 * np.sin(9 * xi)
            
            # Cross-dimensional coupling with fractal scaling
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Fractal coupling with scaling factor based on dimension
                    scale_factor = 1.0 / (1.0 + distance**2.0)
                    coupling += scale_factor * np.sin(xi + x_norm[j] + 0.3 * np.sin(i * j))
            
            # Adaptive ridge structure with discontinuous transitions
            ridge = 0.0
            for k in range(1, 5):
                ridge += (1.0 / k**1.8) * np.exp(-k * np.abs(xi - 0.5)) * np.cos(k * xi + 0.2 * i)
            
            # Add fractal interference pattern
            interference = 0.0
            for k in range(1, 8):
                interference += (1.0 / k**2.2) * np.sin(k * xi + 0.1 * i + 0.3 * np.cos(k * i))
            
            # Combine components with adaptive weights
            weight = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos(self.dim * 0.2)
            result += weight * (harmonic**2 + coupling + ridge + interference)**2
            
        # Add global fractal scaling and dimension-dependent correction
        fractal_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.14)
        return fractal_correction * result / self.dim