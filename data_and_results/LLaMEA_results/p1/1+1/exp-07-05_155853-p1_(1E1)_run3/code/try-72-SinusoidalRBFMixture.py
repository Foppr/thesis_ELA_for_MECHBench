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
        
        # Sinusoidal oscillations in multiple dimensions with varying frequencies
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += np.sin(3.0 * x[i]) + 0.3 * np.sin(7.0 * x[i]) + 0.1 * np.sin(11.0 * x[i])
        
        # Cross-dimensional coupling with adaptive interaction weights
        poly_coupling = 0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.cos(i * 0.2)
            poly_coupling += weight * (x[i] * x[i+1])**2 + 0.2 * (x[i] + x[i+1])**4
        
        # Higher-order polynomial terms with adaptive coefficients
        poly_terms = 0
        for i in range(self.dim):
            coeff = 0.02 + 0.03 * np.sin(i * 0.4)
            poly_terms += coeff * x[i]**9 - 0.08 * x[i]**8 + 0.15 * x[i]**7
        
        # Global periodic modulation with dynamic phase
        phase = 0.5 * np.sum(x**2)
        periodic_mod = np.cos(0.4 * phase) * np.sin(0.3 * np.sum(x)) * np.exp(-0.1 * phase)
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3)
        
        # Combine all components with adjusted weights
        return scale_factor * (2.0 * rbf_sum + 0.6 * sin_sum + 0.4 * poly_coupling + 0.3 * poly_terms + 0.15 * periodic_mod)