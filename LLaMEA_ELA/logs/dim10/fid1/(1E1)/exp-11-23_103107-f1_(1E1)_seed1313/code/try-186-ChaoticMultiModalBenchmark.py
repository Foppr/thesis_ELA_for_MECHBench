import numpy as np

class ChaoticMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Radial component with chaotic sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial = r * (1 + 0.3 * np.sin(5 * r) * np.cos(3 * r))
        
        # Sinusoidal perturbations with varying frequencies and amplitudes
        sin_perturb = 0
        for i in range(self.dim):
            sin_perturb += np.sin(2 * np.pi * x[i] + i * 0.5) * \
                          np.cos(3 * np.pi * x[i] + i * 0.3) * \
                          (1 + 0.2 * np.sin(7 * x[i]))
            
        # Cross-dimensional coupling with chaotic interaction terms
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction based on product of coordinates and their distances
                dist_ij = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += (np.sin(x[i] * x[j]) * 
                                 np.cos(x[i] + x[j]) * 
                                 np.exp(-0.1 * dist_ij**2) *
                                 (1 + 0.1 * np.sin(4 * dist_ij)))
                
        # Multi-scale penalty with multiple local minima
        penalty = 0
        for i in range(self.dim):
            xi = x[i]
            # Multiple penalty regions with different scales and shapes
            penalty += (10 * np.exp(-0.2 * (xi - 2)**2) * np.sin(3 * xi)**2 +
                       5 * np.exp(-0.1 * (xi + 3)**2) * np.cos(2 * xi)**2 +
                       3 * np.exp(-0.05 * xi**2) * np.sin(5 * xi)**2)
        
        # Combine all components with different weights
        return 0.8 * radial + 0.6 * sin_perturb + 0.4 * cross_coupling + penalty