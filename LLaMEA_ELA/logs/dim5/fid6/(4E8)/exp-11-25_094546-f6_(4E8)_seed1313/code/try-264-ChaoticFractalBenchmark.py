import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for stability
        self.chaotic_params = np.random.rand(dim) * 3.0 + 1.0
        self.fractal_dims = np.random.rand(dim) * 0.8 + 0.2
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced hyperchaotic dynamics with multiple attractor basins
            chaotic_term = np.sin(xi * self.chaotic_params[i]) * np.cos(xi * self.chaotic_params[i] * 2.1) + \
                          0.3 * np.sin(xi * self.chaotic_params[i] * 3.7)
            
            # Improved fractal basin boundaries with adaptive dimensionality
            fractal_boundary = 0.0
            for k in range(1, min(25, self.dim + 8)):
                fractal_boundary += (1.0 / (k**2.1)) * np.sin(k * xi * (1.0 + 0.4 * np.sin(self.fractal_dims[i] * k)))
            
            # Modified stiffness gradient with enhanced local curvature modulation
            stiffness = 1.0 + 0.6 * np.sin(xi * 4.0) * np.cos(xi * 2.5) + \
                       0.2 * np.cos(xi * 6.0) * np.sin(xi * 3.2)
            
            # Enhanced multi-modal potential with varying depth and width
            multimodal = (np.sin(xi * 3.5)**2 + 0.4 * np.cos(xi * 8.0)**2 + 
                         0.15 * np.sin(xi * 12.0)**2 + 0.08 * np.cos(xi * 15.0)**2 + \
                         0.05 * np.sin(xi * 20.0)**2)
            
            # Improved cross-dimensional coupling with fractal interference
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling += (1.0 / (1.0 + np.abs(xi - x_norm[j])**2.0)) * \
                               np.sin(xi + x_norm[j] + 0.3 * np.sin(i * j) + 0.1 * np.cos(i + j))
            
            # Combine all terms with adaptive weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.7) * np.cos(self.dim * 0.15)
            result += weight * (stiffness * (multimodal + fractal_boundary + chaotic_term) + 
                               0.4 * coupling)**2
            
        # Global scaling with enhanced hyperchaotic correction factor
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 4.2) + \
                      0.15 * np.cos(np.log(self.dim + 1) * 3.14)
        
        return global_scale * result / self.dim