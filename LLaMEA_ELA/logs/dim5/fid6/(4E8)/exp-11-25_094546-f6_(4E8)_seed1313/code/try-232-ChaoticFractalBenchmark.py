import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for stability
        self.chaotic_params = np.random.rand(dim) * 2.0 + 1.0
        self.fractal_dims = np.random.rand(dim) * 0.5 + 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Hyperchaotic dynamics with multiple attractor basins
            chaotic_term = np.sin(xi * self.chaotic_params[i]) * np.cos(xi * self.chaotic_params[i] * 1.7)
            
            # Fractal basin boundaries with adaptive dimensionality
            fractal_boundary = 0.0
            for k in range(1, min(20, self.dim + 5)):
                fractal_boundary += (1.0 / k**1.8) * np.sin(k * xi * (1.0 + 0.3 * np.sin(self.fractal_dims[i] * k)))
            
            # Adaptive stiffness gradient with local curvature modulation
            stiffness = 1.0 + 0.5 * np.sin(xi * 3.0) * np.cos(xi * 2.0)
            
            # Multi-modal potential with varying depth and width
            multimodal = (np.sin(xi * 4.0)**2 + 0.3 * np.cos(xi * 7.0)**2 + 
                         0.1 * np.sin(xi * 11.0)**2 + 0.05 * np.cos(xi * 13.0)**2)
            
            # Cross-dimensional coupling with fractal interference
            coupling = 0.0
            for j in range(max(0, i-2), min(self.dim, i+3)):
                if i != j:
                    coupling += (1.0 / (1.0 + np.abs(xi - x_norm[j])**1.5)) * \
                               np.sin(xi + x_norm[j] + 0.2 * np.sin(i * j))
            
            # Combine all terms with adaptive weighting
            weight = 1.0 + 0.2 * np.sin(i * 0.5) * np.cos(self.dim * 0.1)
            result += weight * (stiffness * (multimodal + fractal_boundary + chaotic_term) + 
                               0.3 * coupling)**2
            
        # Global scaling with hyperchaotic correction factor
        global_scale = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.14) + \
                      0.1 * np.cos(np.log(self.dim + 1) * 2.71)
        
        return global_scale * result / self.dim