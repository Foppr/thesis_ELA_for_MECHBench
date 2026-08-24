import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive widths and centers
        rbfs = np.sum(np.exp(-np.sum((x.reshape(1, -1) - np.linspace(-5, 5, self.dim).reshape(-1, 1))**2, axis=1) / (2 * 0.5**2)))
        
        # Sinusoidal chaotic component with varying frequencies and amplitudes
        chaotic = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(5 * np.pi * x) * np.cos(7 * np.pi * x))
        
        # Adaptive polynomial coupling with dimensionally dependent exponents
        poly_coupling = np.sum((x**3 + 0.5 * x**2 - 2 * x + 1) * np.sin(np.pi * x) * np.cos(2 * np.pi * x))
        
        # Cross-dimensional interaction with dynamic phase shifts
        cross_term = np.sum(np.sin(np.pi * x[:-1] * x[1:]) * np.cos(2 * np.pi * x[:-1] * x[1:]) * 
                           np.sin(3 * np.pi * x[:-1] * x[1:]) * np.cos(4 * np.pi * x[:-1] * x[1:]))
        
        # Nonlinear scaling and mixing of components
        return 0.3 * rbfs + 0.4 * chaotic + 0.2 * poly_coupling + 0.1 * cross_term + 2.1