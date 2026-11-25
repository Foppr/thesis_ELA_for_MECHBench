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
            base = np.sin(10.0 * xi) + 0.5 * np.sin(20.0 * xi) + 0.2 * np.sin(30.0 * xi)
            
            # Multi-scale interference patterns
            interference = 0.0
            for scale in [1, 2, 3, 4]:
                interference += (1.0 / scale) * np.sin(scale * 5.0 * xi + np.sin(scale * 2.0 * xi))
            
            # Dimensionally adaptive ruggedness
            ruggedness = 0.0
            for k in range(1, min(6, self.dim + 1)):
                ruggedness += (1.0 / k**1.5) * np.cos(k * 3.0 * xi + np.sin(k * 1.5 * xi))
            
            # Combine components with dynamic weights
            weight = 1.0 + 0.3 * np.sin(self.dim * 0.2 + i * 0.1)
            result += weight * (base + interference + ruggedness)**2
            
        # Normalize by dimension and add fractal scaling factor
        fractal_scale = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 0.5)
        return fractal_scale * result / self.dim