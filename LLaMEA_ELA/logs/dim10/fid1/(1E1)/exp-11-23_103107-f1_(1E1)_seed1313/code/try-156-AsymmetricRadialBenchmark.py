import numpy as np

class AsymmetricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial base with mixed degrees and asymmetric coefficients
        polynomial = np.sum(0.5 * x**4 + 2.0 * x**3 - 1.5 * x**2 + 0.8 * x)
        
        # Sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) + \
                         np.cos(4 * np.pi * x[i]) * np.sin(5 * np.pi * x[i])
        
        # Radial basis function with Gaussian-like behavior and varying centers
        radial = 0
        centers = np.linspace(-3, 3, min(self.dim, 6))
        for i in range(min(self.dim, 6)):
            if i < len(centers):
                radial += np.exp(-0.5 * (x[i] - centers[i])**2) * np.sin(2 * np.pi * x[i])
        
        # Asymmetric penalty regions with different scaling factors
        penalty = 0
        for i in range(self.dim):
            if x[i] > 0:
                penalty += 10 * (x[i]**2 + 0.5 * x[i]**4) * np.exp(-0.1 * x[i])
            else:
                penalty += 5 * (x[i]**3 + 0.3 * x[i]**5) * np.exp(-0.05 * abs(x[i]))
        
        # Cross-dimensional coupling with non-symmetric interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    cross_coupling += (x[i]**2 + x[j]**2) * np.sin(0.5 * x[i] * x[j]) * \
                                    np.cos(0.3 * (x[i] + x[j]))
        
        # Combine all components with different weights
        return 0.7 * polynomial + 0.8 * sinusoidal + 0.6 * radial + 0.9 * penalty + 0.5 * cross_coupling