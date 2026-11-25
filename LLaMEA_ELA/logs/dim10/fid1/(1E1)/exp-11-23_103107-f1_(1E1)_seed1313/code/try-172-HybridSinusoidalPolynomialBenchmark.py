import numpy as np

class HybridSinusoidalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.exp(-0.1 * x**2))
        
        # Polynomial corruption with high-degree terms and mixed signs
        polynomial = np.sum(x**4 - 6 * x**2 + 8 * x)
        
        # Radial symmetry component with multiple local minima at different radii
        radius = np.sqrt(np.sum(x**2))
        radial = 5 * np.sin(4 * radius) * np.cos(2 * radius) + \
                 3 * np.exp(-0.5 * (radius - 2)**2) * np.sin(6 * radius)
        
        # Cross-dimensional coupling with interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * \
                                np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Combined fitness function with weighted components
        return 0.8 * sinusoidal + 0.6 * polynomial + 0.7 * radial + 0.9 * cross_coupling