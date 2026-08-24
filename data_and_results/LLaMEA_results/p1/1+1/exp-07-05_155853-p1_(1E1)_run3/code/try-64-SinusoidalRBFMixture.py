import numpy as np

class SinusoidalRBFMixture:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis functions with varying centers and widths
        rbf_sum = 0
        centers = np.linspace(-3.5, 3.5, min(8, self.dim)) + 0.2 * np.sin(np.arange(min(8, self.dim)) * 0.5)
        for i in range(min(8, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.3 + 0.7 * np.sin(i * 0.4)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Sinusoidal oscillations in multiple dimensions
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += 1.2 * np.sin(2.5 * x[i]) + 0.3 * np.sin(6.0 * x[i])
        
        # Cross-dimensional coupling with stronger polynomial interaction
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += 0.8 * (x[i] * x[i+1])**2 + 0.15 * (x[i] + x[i+1])**4
        
        # Higher-order polynomial terms with increased nonlinearity
        poly_terms = 0
        for i in range(self.dim):
            poly_terms += 0.02 * x[i]**9 - 0.06 * x[i]**8 + 0.15 * x[i]**5
        
        # Global periodic modulation with different frequency
        periodic_mod = np.cos(0.4 * np.sum(x**2)) * np.sin(0.25 * np.sum(x))
        
        # Combine all components
        return 1.2 * rbf_sum + 0.9 * sin_sum + 0.4 * poly_coupling + 0.25 * poly_terms + 0.15 * periodic_mod