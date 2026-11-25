import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_component = np.sum(np.sin(5 * x) * np.cos(3 * x) * np.exp(-0.1 * x**2))
        
        # Polynomial conditioning with mixed degrees and cross-terms
        poly_component = np.sum(x**4 + 0.5 * x**3 - 2 * x**2 + 3 * x)
        
        # Radial basis functions with multiple centers and varying widths
        rbfs = 0
        centers = np.linspace(-3, 3, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                rbfs += np.exp(-0.5 * ((x[i] - centers[i]) / (1 + 0.2 * i))**2)
                
        # Cross-dimensional coupling with exponential interactions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross_coupling += np.exp(-0.3 * (x[i] - x[j])**2) * \
                                np.sin(2 * np.pi * (x[i] + x[j]))
                
        # Adaptive penalty based on distance from corners and center
        corner_penalty = np.sum(np.minimum(0, x + 5)**4)
        center_penalty = np.sum((x**2 - 1)**2)
        
        # Combine all components with dynamic weights
        return 1.2 * sin_component + 0.8 * poly_component + 0.5 * rbfs + \
               0.3 * cross_coupling + 0.7 * corner_penalty + 0.4 * center_penalty