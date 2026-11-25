import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Self-similar fractal peak structure with multi-scale harmonics
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Base harmonic component with fractal scaling
            base = np.sin(12.0 * xi) + 0.6 * np.sin(24.0 * xi) + 0.25 * np.sin(36.0 * xi)
            
            # Multi-scale interference patterns with asymmetric coupling
            interference = 0.0
            for scale in [1, 2, 3, 4]:
                interference += (1.0 / scale**1.2) * np.sin(scale * 6.0 * xi + 0.5 * np.sin(scale * 2.5 * xi))
            
            # Dimensionally adaptive ruggedness with asymmetric terms
            ruggedness = 0.0
            for k in range(1, min(7, self.dim + 1)):
                ruggedness += (1.0 / k**1.7) * np.cos(k * 3.5 * xi + 0.7 * np.sin(k * 1.8 * xi))
            
            # Asymmetric coupling between dimensions
            coupling = 0.0
            if i > 0:
                coupling = 0.3 * np.sin(2.0 * (xi - x_norm[i-1])) * np.cos(1.5 * (xi - x_norm[i-1]))
            
            # Combine components with dynamic weights
            weight = 1.0 + 0.4 * np.sin(self.dim * 0.25 + i * 0.15)
            result += weight * (base + interference + ruggedness + coupling)**2
            
        # Normalize by dimension and add fractal scaling factor with modified coefficient
        fractal_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 0.6)
        return fractal_scale * result / self.dim