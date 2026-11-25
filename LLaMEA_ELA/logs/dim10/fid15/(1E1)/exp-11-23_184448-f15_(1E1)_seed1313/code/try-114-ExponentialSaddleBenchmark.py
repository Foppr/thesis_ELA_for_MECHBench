import numpy as np

class ExponentialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial attraction term
        poly_term = np.sum(x**4) * 0.1
        
        # Trigonometric saddle points with varying frequencies
        saddle_term = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 1))
            saddle_term += np.cos(x[i] * freq) * np.sin(x[i] * freq)
        
        # Cross-dimensional coupling with radial symmetry
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling_term += (x[i]**2 + x[j]**2) * np.exp(-dist) * np.sin(dist)
        
        # Polynomial local minima with radial positioning
        local_minima = 0.0
        for i in range(self.dim):
            center = 1.5 * np.cos(i * np.pi / (self.dim + 2))
            weight = np.exp(-0.3 * (x[i] - center)**2)
            local_minima += weight * (x[i]**4 - 2*x[i]**2)**2
        
        # Radial symmetry with multi-scale cosine modulation
        symmetry_term = 0.0
        for scale in [0.5, 1.0, 2.0]:
            symmetry_term += np.cos(r_squared / scale) * np.sin(r_squared / scale)
        
        # Dimensionality-dependent scaling and mixing
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_factor * (0.4 * poly_term + 0.3 * saddle_term + 
                            0.2 * coupling_term + 0.3 * local_minima + 
                            0.1 * symmetry_term)