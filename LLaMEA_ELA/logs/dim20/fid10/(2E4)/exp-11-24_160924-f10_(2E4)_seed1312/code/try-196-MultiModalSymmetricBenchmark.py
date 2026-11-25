import numpy as np

class MultiModalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for each dimension
        self.poly_exponents = [2 + 0.5 * np.sin(0.3 * i + 1.0) for i in range(dim)]
        self.coupling_strengths = [0.8 + 0.4 * np.cos(0.6 * i + 0.5) for i in range(dim)]
        self.symmetry_orders = [3 + 2 * np.sin(0.4 * i + 0.2) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add polynomial potential terms
        for i in range(self.dim):
            xi = x[i]
            exp = self.poly_exponents[i]
            result += (xi**exp) * (1.0 + 0.2 * np.sin(2.0 * xi))
            
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            xi = x[i]
            strength = self.coupling_strengths[i]
            # Coupling with other dimensions using sine and cosine
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += np.sin(strength * xi * x[j]) + 0.5 * np.cos(strength * xi * x[j])
            result += 0.3 * coupling
            
        # Add radial symmetry components with varying orders
        r_squared = np.sum(x**2)
        for i in range(self.dim):
            xi = x[i]
            order = self.symmetry_orders[i]
            # Radial terms with polynomial and trigonometric components
            radial_term = np.sin(order * np.arctan2(xi, 1.0)) * np.cos(order * np.arctan2(xi, 1.0))
            result += 0.1 * r_squared * radial_term
            
        # Add global scaling factor
        global_scale = 1.0 + 0.1 * np.sin(0.5 * self.dim)
        result *= global_scale
        
        # Add final harmonic modulation for increased complexity
        harmonic_mod = 0.05 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        result += harmonic_mod
        
        return result