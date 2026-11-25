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
            
            # Base fractal peak with quantum interference
            base = np.sin(15.0 * xi) + 0.6 * np.sin(25.0 * xi) + 0.3 * np.sin(35.0 * xi)
            
            # Enhanced multi-scale harmonic interference with phase coupling
            interference = 0.0
            for scale in [1, 2, 3, 4, 5]:
                phase = np.sin(scale * 3.0 * xi) * np.cos(scale * 1.5 * xi)
                interference += (1.0 / scale**1.2) * np.sin(scale * 7.0 * xi + phase)
            
            # Cross-scale energy coupling with adaptive ruggedness
            ruggedness = 0.0
            for k in range(1, min(8, self.dim + 1)):
                coupling = np.sin(k * 2.0 * xi) * np.cos(k * 0.5 * xi)
                ruggedness += (1.0 / k**1.8) * np.cos(k * 4.0 * xi + coupling)
            
            # Quantum-inspired curvature modulation
            curvature = 0.5 * np.sin(2.0 * xi)**2 + 0.3 * np.cos(3.0 * xi)**2
            
            # Combine all components with dynamic weighting based on dimension and position
            weight = 1.0 + 0.4 * np.sin(self.dim * 0.3 + i * 0.15) + 0.2 * np.cos(xi * 2.0)
            result += weight * (base + interference + ruggedness + curvature)**2
            
        # Enhanced fractal scaling with hyperchaotic modulation
        fractal_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 0.7) * np.cos(np.sqrt(self.dim) * 0.4)
        return fractal_scale * result / self.dim