import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        chaotic = 0
        for i in range(self.dim):
            r = self.r_values[i]
            xi = (x[i] + 5.0) / 10.0  # Normalize to [0, 1]
            chaotic += np.log(1.0 + r * xi * (1 - xi))
        
        # Polynomial chaos expansion with mixed terms
        poly_expansion = 0
        for i in range(self.dim):
            poly_expansion += (x[i]**2 + x[i]**3 + 0.5 * x[i]**4) * np.cos(0.5 * i)
            
        # Spherical symmetry with multiple local minima
        r_squared = np.sum(x**2)
        spherical = np.sin(10.0 * np.sqrt(r_squared)) * np.exp(-0.1 * r_squared)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                cross_coupling += np.exp(-0.5 * (diff / (1.0 + abs(x[i]) + abs(x[j])))**2)
        
        # Fractal-like component using sine and cosine series
        fractal = 0
        for i in range(self.dim):
            for k in range(1, 6):
                fractal += np.sin(k * x[i]) * np.cos(k * x[i] / 2.0) / (k**1.5)
        
        # Combine all components with different weights
        return 0.8 * chaotic + 1.2 * poly_expansion + 0.6 * spherical + 0.4 * cross_coupling + 0.3 * fractal + 3.0 * self.dim