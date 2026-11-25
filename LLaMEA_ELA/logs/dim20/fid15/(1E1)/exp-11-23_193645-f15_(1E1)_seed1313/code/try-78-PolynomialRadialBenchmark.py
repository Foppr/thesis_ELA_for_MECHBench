import numpy as np

class PolynomialRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial interaction terms with varying degrees
        poly_term = np.sum(x_norm ** 4 + 0.5 * x_norm ** 3 + 0.2 * x_norm ** 2)
        
        # Radial basis function component with varying widths and centers
        rbfs = []
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.logspace(-1, 1, min(5, self.dim))
        for i, (center, width) in enumerate(zip(centers, widths)):
            if i < len(x_norm):
                rbf = np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2)
                rbfs.append(rbf)
        radial_term = np.sum(rbfs) if rbfs else 0.0
        
        # Asymmetric cross-dimensional coupling with polynomial weights
        asym_coupling = 0.0
        for i in range(self.dim - 1):
            weight_i = 1.0 + 0.3 * (i / self.dim)
            weight_j = 1.0 + 0.2 * ((self.dim - i) / self.dim)
            asym_coupling += weight_i * weight_j * (x_norm[i] ** 2 + x_norm[i+1] ** 2) * \
                           np.sin(3 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Mixed sine-cosine modulation with polynomial scaling
        mod_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) + 
                         0.5 * np.sin(6 * np.pi * x_norm))
        
        # Combined function with different weights and asymmetric scaling
        result = 2.0 * poly_term + 0.7 * radial_term + 0.6 * asym_coupling + 0.3 * mod_term
        
        return result