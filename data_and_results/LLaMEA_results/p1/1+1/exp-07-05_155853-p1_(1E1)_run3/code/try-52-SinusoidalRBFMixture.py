import numpy as np

class SinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with varying centers and widths
        rbf_sum = 0
        centers = np.linspace(-4.5, 4.5, min(8, self.dim))
        for i in range(min(8, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.3 + 0.7 * np.sin(i * 0.5)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Sinusoidal oscillations in multiple dimensions
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += np.sin(2.5 * x[i]) + 0.6 * np.sin(4.0 * x[i])
        
        # Cross-dimensional coupling with polynomial interaction
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += (x[i] * x[i+1])**2.5 + 0.15 * (x[i] + x[i+1])**3.5
        
        # Higher-order polynomial terms
        poly_terms = 0
        for i in range(self.dim):
            poly_terms += 0.015 * x[i]**9 - 0.06 * x[i]**8 + 0.12 * x[i]**7
        
        # Global periodic modulation
        periodic_mod = np.cos(0.4 * np.sum(x**2)) * np.sin(0.25 * np.sum(x))
        
        # Combine all components
        return 1.8 * rbf_sum + 0.9 * sin_sum + 0.4 * poly_coupling + 0.25 * poly_terms + 0.15 * periodic_mod