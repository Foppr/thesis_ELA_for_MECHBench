import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos terms with varying exponents
        poly_term = np.sum((x**4 + 0.5 * x**3 + 0.2 * x**2 + 0.1 * x) * np.exp(-0.2 * x**2))
        
        # Sine-wave coupling with adaptive frequency modulation
        sine_coupling = np.sum(np.sin(3.0 * x + np.cos(x)) * np.cos(2.0 * x + np.sin(x)))
        
        # Radial basis functions with adaptive scaling
        radial_basis = np.sum(np.exp(-0.5 * (x**2) / (1.0 + 0.1 * np.abs(x))))
        
        # Cross-dimensional interference with weighted interaction
        if self.dim > 1:
            cross_interaction = np.sum((x[:-1] * x[1:]) / (1.0 + np.abs(x[:-1]) + np.abs(x[1:])))
        else:
            cross_interaction = 0.0
            
        # Combined function with dynamic weights based on dimensionality
        weight_poly = 0.35 + 0.05 * np.log(self.dim + 1)
        weight_sine = 0.30 + 0.03 * np.log(self.dim + 1)
        weight_radial = 0.25 + 0.02 * np.log(self.dim + 1)
        weight_cross = 0.10 + 0.01 * np.log(self.dim + 1)
        
        return weight_poly * poly_term + weight_sine * sine_coupling + weight_radial * radial_basis + weight_cross * cross_interaction