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
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            sin_sum += np.sin(freq * x[i]) + 0.3 * np.sin(3.0 * freq * x[i])
        
        # Cross-dimensional coupling with enhanced interaction terms
        poly_coupling = 0
        for i in range(self.dim - 1):
            poly_coupling += 0.5 * (x[i] * x[i+1])**3 + 0.2 * (x[i] + x[i+1])**4
        
        # Higher-order polynomial terms with adaptive coefficients
        poly_terms = 0
        for i in range(self.dim):
            coeff = 0.02 + 0.03 * np.sin(i * 0.4)
            poly_terms += coeff * x[i]**9 - 0.08 * x[i]**8 + 0.15 * x[i]**7
        
        # Global periodic modulation with dynamic amplitude
        amp = 0.5 + 0.5 * np.cos(0.2 * np.sum(x))
        periodic_mod = amp * np.cos(0.4 * np.sum(x**2)) * np.sin(0.3 * np.sum(x))
        
        # Add correlation between dimensions through interaction terms
        corr_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_term += 0.1 * np.sin(0.5 * (x[i] - x[j])) * np.cos(0.3 * (x[i] + x[j]))
        
        # Combine all components with optimized weights
        return 1.2 * rbf_sum + 0.9 * sin_sum + 0.4 * poly_coupling + 0.3 * poly_terms + 0.15 * periodic_mod + 0.2 * corr_term