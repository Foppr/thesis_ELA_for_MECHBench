import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos component with varying degrees
        poly_chaos = np.sum((x_norm**2 + 0.1 * x_norm**4 + 0.01 * x_norm**6) * 
                           (1.0 + 0.3 * np.sin(13 * x_norm) * np.cos(7 * x_norm)))
        
        # Trigonometric wave interference with fractal frequency scaling
        wave_interference = 0.0
        for i in range(1, min(8, self.dim + 1)):
            freq = 2 ** i
            wave_interference += (np.sin(freq * x_norm) * np.cos(freq * x_norm) + 
                                0.5 * np.sin(2 * freq * x_norm) * np.cos(2 * freq * x_norm))
        
        # Hierarchical basin structure with self-similarity
        basin_structure = 0.0
        for i in range(min(4, self.dim)):
            scale = 2 ** (i + 1)
            basin_structure += 0.1 * np.sin(scale * x_norm) * np.cos(scale * x_norm) * \
                              np.exp(-0.1 * scale * np.abs(x_norm))
        
        # Cross-term interactions with asymmetric coupling
        cross_terms = 0.0
        for i in range(self.dim - 1):
            cross_terms += (0.2 * x_norm[i] ** 3 * x_norm[i + 1] + 
                           0.1 * np.abs(x_norm[i]) * x_norm[i + 1]**2)
        
        # Fractal dimensionality scaling component
        fractal_dim = np.log(self.dim + 1) / np.log(2) if self.dim > 0 else 1.0
        fractal_component = 0.3 * np.sin(fractal_dim * np.sum(x_norm**2)) * \
                           np.cos(fractal_dim * np.sum(x_norm**3))
        
        # Global ruggedness modifier
        ruggedness = 0.05 * np.sum(np.sin(25 * x_norm) * np.cos(23 * x_norm))
        
        return poly_chaos + 0.4 * wave_interference + 0.2 * basin_structure + \
               0.1 * cross_terms + 0.15 * fractal_component + ruggedness