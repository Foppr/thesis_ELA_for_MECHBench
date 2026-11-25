import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Fractal-like structure using recursive trigonometric components
        f2 = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Nested sinusoidal terms with increasing frequency
            f2 += (np.sin(2**i * np.pi * xi) + 0.5 * np.sin(2**(i+1) * np.pi * xi))**2
        
        # Radial basis function component for multi-scale peaks
        rbf = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                rbf += np.exp(-((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2) / 2)
        f3 = rbf
        
        # Chaotic perturbation using logistic map modulation
        chaotic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Logistic map with parameter control
            r = 3.9
            chaotic += np.sin(r * xi * (1 - xi))**2
        
        # Cross-dimensional coupling with varying strength
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.cos(3 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Asymmetric saddle and peak structure
        asym = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            asym += (xi**5 - 0.7 * xi**3 + 0.2 * xi) ** 2
        
        # Combine all components with different weights
        return 0.1 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * chaotic + 0.1 * coupling + 0.1 * asym