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
        
        # Sinusoidal oscillations in multiple dimensions
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += np.sin(3.0 * x[i]) + 0.3 * np.sin(7.0 * x[i]) + 0.1 * np.sin(11.0 * x[i])
        
        # Cross-dimensional coupling with higher-order polynomial interaction
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += (x[i] * x[i+1])**3 + 0.15 * (x[i] + x[i+1])**4
        
        # Higher-order polynomial terms with varying coefficients
        poly_terms = 0
        for i in range(self.dim):
            poly_terms += 0.02 * x[i]**9 - 0.06 * x[i]**8 + 0.12 * x[i]**7 - 0.08 * x[i]**6
        
        # Global periodic modulation with multiple frequencies
        periodic_mod = np.cos(0.4 * np.sum(x**2)) * np.sin(0.3 * np.sum(x)) + 0.5 * np.cos(0.1 * np.sum(x**3))
        
        # Additional harmonic coupling between dimensions
        harmonic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_coupling += 0.2 * np.sin(2.0 * (x[i] - x[j])) * np.cos(1.5 * (x[i] + x[j]))
        
        # Combine all components
        return 2.0 * rbf_sum + 1.0 * sin_sum + 0.4 * poly_coupling + 0.3 * poly_terms + 0.15 * periodic_mod + 0.25 * harmonic_coupling