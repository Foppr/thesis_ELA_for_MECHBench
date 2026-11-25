import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillation component using sine and cosine combinations
        chaotic_osc = 0
        for i in range(self.dim):
            chaotic_osc += np.sin(x[i]) * np.cos(x[i] * np.pi / (i + 1)) * np.exp(-0.05 * x[i]**2)
        
        # Radial basis function component to create multiple attraction basins
        rbf = 0
        for i in range(self.dim):
            rbf += np.exp(-0.5 * (x[i] - 2 * np.sin(i))**2 / (1 + i * 0.1))
        
        # Modified polynomial penalty with higher-order terms
        poly_penalty = np.sum((x**4 - 6 * x**3 + 11 * x**2 - 6 * x)**2)
        
        # Combined function with adaptive scaling factors
        return 0.2 * chaotic_osc + 0.3 * rbf + 0.005 * poly_penalty + 5 * self.dim