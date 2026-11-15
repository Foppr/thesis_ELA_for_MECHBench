import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(10 * x) * np.cos(8 * x) * np.sin(6 * x) * np.cos(4 * x) * 
                         np.sin(2 * x) * np.cos(1 * x))
        
        # Polynomial chaos expansion with mixed monomials and cross-terms
        poly_term = np.sum(0.5 * x**6 + 1.2 * x**5 - 2.5 * x**4 + 3.1 * x**3 - 1.8 * x**2 + 
                          0.9 * x + 0.1 * x**2 * x**3 + 0.05 * x**4 * x**2)
        
        # Radial basis function components with varying centers and widths
        rbfs = []
        centers = np.linspace(-5, 5, min(10, self.dim))
        for i, c in enumerate(centers):
            if i < len(x):
                rbfs.append(np.exp(-0.5 * ((x[i] - c) / (1.5 + 0.1 * i))**2))
        rbf_term = np.sum(rbfs)
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross_term = 0
        for i in range(self.dim - 1):
            cross_term += (x[i] - x[i+1])**4 * np.sin(5 * np.pi * (x[i] + x[i+1]))
            cross_term += (x[i] * x[i+1])**2 * np.cos(3 * np.pi * (x[i] - x[i+1]))
        
        # High-frequency chaotic modulation with dynamic amplitude
        chaotic_mod = np.sum(np.sin(50 * x) * np.cos(45 * x) * np.sin(40 * x) * 
                            np.cos(35 * x) * np.sin(30 * x) * np.cos(25 * x))
        
        # Combined fitness with weighted components and global offset
        return 0.3 * sin_term + 0.25 * poly_term + 0.15 * rbf_term + 0.2 * cross_term + 0.1 * chaotic_mod + 2.5