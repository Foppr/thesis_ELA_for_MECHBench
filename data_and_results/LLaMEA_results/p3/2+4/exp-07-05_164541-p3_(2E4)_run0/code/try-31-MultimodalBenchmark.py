import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and widths for stability
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with Hermite polynomials
        chaos_term = np.sum(np.prod(
            [np.exp(-0.5 * x[i]**2) * np.polynomial.hermite.hermval(x[i], [0, 1, 0, 1]) 
             for i in range(self.dim)], axis=0))
        
        # Radial basis function ensemble
        rbf_term = np.sum([
            self.widths[j] * np.exp(-0.5 * np.sum((x - self.centers[j])**2) / (self.widths[j]**2))
            for j in range(10)
        ])
        
        # Temporal coupling through delayed sine waves
        delayed_coupling = np.sum(np.sin(np.pi * (x[:-1] + 0.5 * x[1:]) + 
                                         0.3 * np.sin(2 * np.pi * x[:-1])) * 
                                 np.cos(np.pi * (x[1:] - 0.5 * x[:-1]) + 
                                        0.4 * np.cos(3 * np.pi * x[1:])))
        
        # Fractional Brownian motion inspired term
        fbm_term = np.sum(0.1 * x**3.2 + 0.2 * x**2.1 - 0.3 * x**1.5 + 0.4 * x**0.8)
        
        # Cross-dimensional nonlinear correlation with exponential modulation
        correlation_term = np.sum(np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)) * 
                                 np.sin(np.pi * (x[:-1] * x[1:])))
        
        # Combine all terms with dynamic weights based on dimensionality
        weight_chaos = 0.25 / (1.0 + np.exp(-0.1 * self.dim))
        weight_rbf = 0.30 / (1.0 + np.exp(-0.1 * self.dim))
        weight_coupling = 0.20 / (1.0 + np.exp(-0.1 * self.dim))
        weight_fbm = 0.15 / (1.0 + np.exp(-0.1 * self.dim))
        weight_correlation = 0.10 / (1.0 + np.exp(-0.1 * self.dim))
        
        return (weight_chaos * chaos_term + 
                weight_rbf * rbf_term + 
                weight_coupling * delayed_coupling + 
                weight_fbm * fbm_term + 
                weight_correlation * correlation_term + 
                1.5)