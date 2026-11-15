import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute random perturbations for stochastic elements
        self.perturbations = np.random.uniform(-0.1, 0.1, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Asymmetric hyperbolic tangent components with varying scales
        tanh_component = np.sum(np.tanh(3.0 * x) * np.exp(-0.5 * x**2)) + \
                         np.sum(np.tanh(2.0 * x) * np.exp(-0.3 * x**2)) + \
                         np.sum(np.tanh(0.5 * x) * np.exp(-0.1 * x**2))
        
        # Cross-dimensional coupling with sine modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Stochastic perturbation component
        stochastic = np.sum(np.sin(x + self.perturbations) * np.cos(x + self.perturbations))
        
        # Polynomial with chaotic coefficients
        poly = 0
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * np.sin(10 * x[i])
            poly += coeff * x[i]**7
        
        # Rugged landscape with multiple local minima
        rugged = 0
        for i in range(self.dim):
            rugged += np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Combined landscape with dynamic scaling
        return 0.4 * tanh_component + 0.3 * coupling + 0.15 * stochastic + 0.1 * poly + 0.05 * rugged