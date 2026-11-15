import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Composite sinusoidal interference with varying frequencies
        interference = 0
        for i in range(self.dim):
            interference += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) + \
                          np.sin(5 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) + \
                          np.sin(11 * np.pi * x[i]) * np.cos(13 * np.pi * x[i])
        
        # Polynomial saddle point structure with asymmetric coefficients
        saddles = 0
        for i in range(self.dim):
            saddles += (x[i]**4 - 2 * x[i]**3 + x[i]**2) * np.exp(-0.1 * x[i]**2) + \
                       (x[i]**5 - 3 * x[i]**4 + 3 * x[i]**3 - x[i]**2) * np.sin(0.2 * x[i])
        
        # Cross-dimensional exponential coupling with varying decay rates
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.05 * (x[i] - x[j])**2) * \
                           np.sin(0.5 * x[i] * x[j]) * \
                           np.cos(0.3 * x[i] + 0.4 * x[j]) * \
                           np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        # Chaotic modulation with logistic map-like behavior
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(10 * np.pi * x[i]) * np.cos(15 * np.pi * x[i]) * \
                       np.exp(-0.2 * np.abs(x[i])) * \
                       np.sin(0.1 * x[i]**4)
        
        # Enhanced hyperbolic component with exponential scaling
        hyperbolic = 0
        for i in range(self.dim):
            hyperbolic += np.sinh(0.5 * x[i]) * np.cosh(0.3 * x[i]) * \
                         np.exp(-0.1 * x[i]**2) + \
                         np.tanh(0.4 * x[i]) * np.sin(0.6 * x[i]) * \
                         np.exp(-0.05 * np.abs(x[i]))
        
        # Quadratic base with sinusoidal perturbation
        base = np.sum(x**2) + 0.2 * np.sum(np.sin(5 * x)**2) + \
               0.1 * np.sum(np.cos(3 * x)**2)
        
        return base + interference + saddles + coupling + chaotic + hyperbolic