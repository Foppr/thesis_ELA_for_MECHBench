import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial landscape with varying degrees and coefficients
        polynomial = np.sum((x**4 - 2*x**2 + 1) * (1 + 0.1 * np.sin(5 * x)))
        
        # Sinusoidal components with adaptive frequencies based on dimension
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin((i+1) * x[i]) * np.cos((i+1) * x[i] * 0.5) + \
                         np.cos((i+1) * x[i] * 2) * np.sin((i+1) * x[i] * 0.3)
        
        # Radial basis function components with dynamic centers and widths
        rbf = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                rbf += np.exp(-0.5 * ((x[i] - centers[i]) / (1 + 0.1 * i))**2) * \
                       np.sin(3 * (x[i] - centers[i]))
        
        # Adaptive conditioning with dimension-dependent scaling
        conditioning = 0
        for i in range(self.dim):
            conditioning += (i+1) * x[i]**2 * (1 + 0.05 * np.cos(10 * x[i]))
            
        # Dynamic penalty regions that change based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        penalty = 0
        if dist_from_origin > 4:
            penalty += 10 * (dist_from_origin - 4)**3 * np.sin(dist_from_origin)
        elif dist_from_origin < 1:
            penalty += 5 * (1 - dist_from_origin)**2 * np.cos(2 * dist_from_origin)
            
        # Cross-dimensional coupling with varying interaction strengths
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                cross_coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * \
                                (1 + 0.2 * np.cos(0.5 * (x[i] - x[j])**2))
        
        # Combine all components with adaptive weights
        return 0.8 * polynomial + 0.6 * sinusoidal + 0.7 * rbf + \
               0.5 * conditioning + penalty + 0.4 * cross_coupling