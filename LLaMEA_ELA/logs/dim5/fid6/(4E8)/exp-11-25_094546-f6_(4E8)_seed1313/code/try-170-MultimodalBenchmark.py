import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal peak structure with quantum-inspired components
            base = np.sin(12.0 * xi) + 0.6 * np.sin(24.0 * xi) + 0.3 * np.sin(36.0 * xi)
            
            # Multi-scale quantum interference patterns
            interference = 0.0
            for scale in [1, 2, 3, 4, 5]:
                phase = np.sin(scale * 3.0 * xi) + 0.5 * np.sin(scale * 6.0 * xi)
                interference += (1.0 / scale**1.2) * np.sin(scale * 7.0 * xi + phase)
            
            # Dynamic basin modulation with spectral coupling
            basin_mod = 0.0
            for k in range(1, min(8, self.dim + 1)):
                coupling = np.cos(k * 4.0 * xi) * np.sin(k * 2.0 * xi)
                basin_mod += (1.0 / k**1.3) * coupling
            
            # Combine components with adaptive weights based on dimension and position
            weight = 1.0 + 0.4 * np.sin(self.dim * 0.3 + i * 0.15) * np.cos(xi * 2.0)
            result += weight * (base + interference + basin_mod)**2
            
        # Apply dynamic scaling factor and normalize
        dynamic_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 0.7) * np.cos(self.dim * 0.1)
        return dynamic_scale * result / self.dim