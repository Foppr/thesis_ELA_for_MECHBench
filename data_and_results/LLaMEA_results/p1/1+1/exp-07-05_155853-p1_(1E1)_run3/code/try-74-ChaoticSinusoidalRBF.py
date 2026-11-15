import numpy as np

class ChaoticSinusoidalRBF:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sinusoidal components with dynamic frequencies
        chaotic_sum = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7) + 0.3 * np.cos(i * 0.4)
            chaotic_sum += np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + 0.2 * np.sin(3.0 * freq * x[i])
        
        # Adaptive radial basis functions with chaotic centers and widths
        rbf_sum = 0
        for i in range(min(12, self.dim)):
            center = -4.0 + 8.0 * (i / (self.dim - 1) if self.dim > 1 else 0.5)
            center += 0.5 * np.sin(i * 0.5) * np.cos(i * 0.3)
            width = 0.3 + 0.4 * np.sin(i * 0.6) + 0.1 * np.cos(i * 0.2)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Higher-order polynomial coupling with chaotic interaction coefficients
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.5 + 0.3 * np.sin(i * 0.8) + 0.2 * np.cos(i * 0.5)
            poly_coupling += coeff * (x[i]**3 * x[i+1]**2 + x[i]**2 * x[i+1]**3)
        
        # Multifractal-like polynomial terms with dynamic exponents
        poly_terms = 0
        for i in range(self.dim):
            exp = 6.0 + 2.0 * np.sin(i * 0.4) + 1.0 * np.cos(i * 0.3)
            poly_terms += 0.02 * x[i]**exp - 0.03 * x[i]**(exp - 1) + 0.01 * x[i]**(exp - 2)
        
        # Dynamic cross-dimensional coupling with time-like modulation
        cross_coupling = 0
        for i in range(self.dim - 2):
            mod = 1.0 + 0.2 * np.sin(i * 0.5 + np.sum(x)**0.5)
            cross_coupling += mod * (x[i] * x[i+1] * x[i+2])**1.5
        
        # Global chaotic modulation with multiple frequencies
        global_mod = np.sin(0.4 * np.sum(x**2)) * np.cos(0.3 * np.sum(x)) * np.sin(0.1 * np.sum(x**3))
        
        # Combine all components with varying weights
        return 2.0 * chaotic_sum + 0.7 * rbf_sum + 0.5 * poly_coupling + 0.3 * poly_terms + 0.2 * cross_coupling + 0.1 * global_mod