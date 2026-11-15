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
            width = 0.3 + 0.7 * np.sin(i * 0.5)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Sinusoidal oscillations in multiple dimensions with adaptive frequencies
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += np.sin(1.5 * x[i]) + 0.7 * np.sin(4.0 * x[i]) + 0.3 * np.sin(7.0 * x[i])
        
        # Cross-dimensional coupling with mixed polynomial and trigonometric interaction
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += 0.5 * (x[i] * x[i+1])**2 + 0.2 * np.sin(x[i] + x[i+1]) + 0.1 * (x[i] + x[i+1])**4
        
        # Higher-order polynomial terms with adaptive coefficients
        poly_terms = 0
        for i in range(self.dim):
            poly_terms += 0.02 * x[i]**9 - 0.08 * x[i]**8 + 0.15 * x[i]**7 - 0.1 * x[i]**6
        
        # Global periodic modulation with variable amplitude
        periodic_mod = np.cos(0.2 * np.sum(x**2)) * np.sin(0.15 * np.sum(x)) * (1.0 + 0.2 * np.sin(0.5 * np.sum(x**2)))
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with adjusted weights
        return scale_factor * (1.2 * rbf_sum + 0.9 * sin_sum + 0.4 * poly_coupling + 0.3 * poly_terms + 0.15 * periodic_mod)