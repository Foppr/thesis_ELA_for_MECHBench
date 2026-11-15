import numpy as np

class SinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with varying centers and widths
        rbf_sum = 0
        centers = np.linspace(-4.0, 4.0, min(8, self.dim))
        for i in range(min(8, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.5 + 0.5 * np.sin(i * 0.3)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Sinusoidal oscillations in multiple dimensions
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += np.sin(2.0 * x[i]) + 0.5 * np.sin(5.0 * x[i])
        
        # Cross-dimensional coupling with polynomial interaction
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += (x[i] * x[i+1])**2 + 0.1 * (x[i] + x[i+1])**3
        
        # Higher-order polynomial terms
        poly_terms = 0
        for i in range(self.dim):
            poly_terms += 0.01 * x[i]**8 - 0.05 * x[i]**7 + 0.1 * x[i]**6
        
        # Global periodic modulation
        periodic_mod = np.cos(0.3 * np.sum(x**2)) * np.sin(0.2 * np.sum(x))
        
        # Combine all components
        return 1.5 * rbf_sum + 0.8 * sin_sum + 0.3 * poly_coupling + 0.2 * poly_terms + 0.1 * periodic_mod