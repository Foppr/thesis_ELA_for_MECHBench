import numpy as np

class AsymmetricRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial landscape with varying degrees and coefficients
        polynomial = np.sum((x**4) * (0.5 + 0.5 * np.sin(2 * np.pi * x)))
        
        # Sinusoidal components with frequency modulation and phase shifts
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                           (1 + 0.3 * np.sin(0.5 * np.pi * x)**2))
        
        # Radial basis function with asymmetric decay rates and shifted centers
        rbf = 0
        centers = np.linspace(-4, 4, self.dim)
        for i in range(self.dim):
            dist = np.abs(x[i] - centers[i])
            rbf += np.exp(-0.5 * dist**2) * np.sin(2 * dist) * (1 + 0.2 * np.cos(3 * dist))
            
        # Asymmetric penalty regions with different scaling factors for positive and negative directions
        penalty = 0
        for i in range(self.dim):
            if x[i] > 0:
                penalty += 10 * (1 - np.exp(-0.1 * x[i]**2)) * np.sin(4 * x[i])**2
            else:
                penalty += 15 * (1 - np.exp(-0.05 * x[i]**2)) * np.cos(3 * x[i])**2
                
        # Cross-dimensional coupling with non-linear interaction terms
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling to reduce complexity
                coupling += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * \
                           np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Global scaling and combination of all components
        return 0.8 * (polynomial + sinusoidal + rbf + penalty + coupling) + 1.5 * np.sum(x**6)